import pandas as pd

filename = 'NYC_taxi_2013_01.csv'
for chunk in pd.read_csv(filename, chunksize=50000):
  print('type: %s shape %s' % (type(chunk), chunk.shape))
# type: <class 'pandas.core.frame.DataFrame'> shape (50000, 14)
# type: <class 'pandas.core.frame.DataFrame'> shape (50000, 14)
# type: <class 'pandas.core.frame.DataFrame'> shape (50000, 14)
# type: <class 'pandas.core.frame.DataFrame'> shape (49999, 14)
# The last line is the header line

chunk.shape
# (49999, 14)

chunk.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 49999 entries, 150000 to 199998
# Data columns (total 14 columns):
# medallion             49999 non-null object
# hack_license          49999 non-null object
# vendor_id             49999 non-null object
# rate_code             49999 non-null int64
# store_and_fwd_flag    162 non-null object
# pickup_datetime       49999 non-null object
# dropoff_datetime      49999 non-null object
# passenger_count       49999 non-null int64
# trip_time_in_secs     49999 non-null int64
# trip_distance         49999 non-null float64
# pickup_longitude      49999 non-null float64
# pickup_latitude       49999 non-null float64
# dropoff_longitude     49999 non-null float64
# dropoff_latitude      49999 non-null float64
# dtypes: float64(5), int64(3), object(6)

is_long_trip = (chunk.trip_time_in_secs > 1200)
chunk.loc[is_long_trip].shape
# (5565, 14)
# About 5500 taxi rides longer than 20 minutes in duration

def filter_is_long_trip(data):
  "Returns DataFrame filtering trips longer than 20 minutes"
  is_long_trip = (data.trip_time_in_secs > 1200)
  return data.loc[is_long_trip]

chunks = []

# build with a for loop:
for chunk in pd.read_csv(filename, chunksize=1000):
    chunks.append(filter_is_long_trip(chunk))

# or with a list comprehension:
chunks = [filter_is_long_trip(chunk)
          for chunk in pd.read_csv(filename,
          chunksize=1000) ]


len(chunks)
# 200

lengths = [len(chunk) for chunk in chunks]

lengths[-5:]
# each has ~100 rows
# [115, 147, 137, 109, 119]

long_trips_df = pd.concat(chunks)
long_trips_df.shape
# (21661, 14)


# Plot
import matplotlib.pyplot as plt

long_trips_df.plot.scatter(x='trip_time_in_secs',
                           y='trip_distance');
plt.xlabel('Trip duration [seconds]')
plt.ylabel('Trip distance [miles]')
plt.title('NYC Taxi rides over 20 minutes (2013-01-01 to 2013-01-14)')
plt.show()


