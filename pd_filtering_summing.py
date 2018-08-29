import pandas as pd

filename = 'NYC_taxi_2013_01.csv'

def filter_is_long_trip(data):
    "Returns DataFrame filtering trips longer than 20 minutes"
    is_long_trip = (data.trip_time_in_secs > 1200)
    return data.loc[is_long_trip]

# Filtering with a list comprehension
chunks = [filter_is_long_trip(chunk)
             for chunk in pd.read_csv(filename, chunksize=1000)]

# Filtering with a generator
# Uses lazy evaluation
chunks = (filter_is_long_trip(chunk)
             for chunk in pd.read_csv(filename, chunksize=1000))

# Lazy sum with a generator
# No computation is done until we iterate over it
distances = (chunk['trip_distance'].sum() for chunk in chunks)

# Computation done here
sum(distances)
# 230909.56000000003

distances
# <generator object <genexpr> at 0x10766f9e8>
# The generator still exists, but it has been exhausted after the computation.

# Calling next() generates a StopIteration
next(distances)
# StopIteration                             Traceback (most recent call last)
# <ipython-input-10-9995a5373b05> in <module>()

