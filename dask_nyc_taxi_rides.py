
import pandas as pd

df = pd.read_csv('yellow_tripdata_2015-01.csv')
df.shape
# (12748986, 19)
df.columns
# Index(['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
#        'passenger_count', 'trip_distance', 'pickup_longitude',
#        'pickup_latitude', 'RateCodeID', 'store_and_fwd_flag',
#        'dropoff_longitude', 'dropoff_latitude', 'payment_type', 'fare_amount',
#        'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
#        'improvement_surcharge', 'total_amount'],
#       dtype='object')

df['payment_type'].value_counts()
# 1    7881388
# 2    4816992
# 3      38632
# 4      11972
# 5          2
# Name: payment_type, dtype: int64


# Read all .csv files
df = dd.read_csv('taxi/*.csv', assume_missing=True)
# Create column 'tip_fraction'
df['tip_fraction'] = df['tip_amount'] / (df['total_amount'] - df['tip_amount'])
# Convert 'tpep_dropoff_datetime' column to datetime objects
df['tpep_dropoff_datetime'] = dd.to_datetime(df['tpep_dropoff_datetime'])
# Create column 'hour'
df['hour'] = df['tpep_dropoff_datetime'].dt.hour

# Filter rows where payment_type == 1
credit = df['payment_type'] == 1
# Group by 'hour' column
hourly = df.loc[credit].groupby('hour')
# Aggregate mean 'tip_fraction' and print its data type
result = hourly['tip_fraction'].mean()
print(type(result))

tip_frac = result.compute()
print(type(tip_frac))
tip_frac.plot.line()
plt.ylabel('Tip fraction')
plt.show()

