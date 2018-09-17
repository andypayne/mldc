
# Pandas, for comparison
import time, pandas as pd

t_start = time.time(); \
df = pd.read_csv('yellow_tripdata_2015-01.csv'); \
t_end = time.time(); \
print('pd.read_csv(): {} s'.format(t_end-t_start)) # time [s]
# pd.read_csv: 43.820565938949585 s

t_start = time.time(); \
m = df['trip_distance'].mean(); \
t_end = time.time(); \
print('.mean(): {} ms'.format((t_end-t_start)*1000)) # time [ms]
# .mean(): 17.752885818481445 ms
# 43sec vs 17msec - disk vs memory


# Dask version
import dask.dataframe as dd, time
t_start = time.time();\
df = dd.read_csv('yellow_tripdata_2015-*.csv');\
t_end = time.time();\
print('dd.read_csv: {} ms'.format((t_end-t_start)*1000))  # time [ms]
# dd.read_csv: 404.7999382019043 ms

t_start = time.time();\
m = df['trip_distance'].mean();\
t_end = time.time();\
print('.mean(): {} ms'.format((t_end-t_start)*1000))  # time [ms]
# .mean(): 2.289295196533203 ms

# Computation here - 3 minutes
# This is much better, given that this data doesn't all fit into memory, and
# reading in and calculating the mean on 1/12th of the data took ~ 45 sec
# (above, the pandas version).
t_start = time.time(); \
result = m.compute(); \
t_end = time.time(); \
print('.compute(): {} min'.format((t_end-t_start)/60))  # time [min]
# .compute(): 3.4004417498906454 min

# a quicker way to time computations in ipython notebooks - %time (shell)
m = df['trip_distance'].mean()
%time result = m.compute()
# CPU times: user 9min 50s, sys: 1min 16s, total: 11min 7s
# Wall time: 3min 1s



# This function will work with both Pandas dataframes and Dask dataframes
def by_region(df):
    toxins = df['Indicator Code'] == 'EN.ATM.PM25.MC.ZS'
    y2015 = df['Indicator Code'] == 2015
    regions = df.loc[toxins & y2015].groupby('Region')
    return regions['value'].mean()


# Time the Pandas version - read the file and call by_region
t0 = time.time()
df = pd.read_csv('WDI.csv')
result = by_region(df)
t1 = time.time()
print((t1-t0)*1000)

# Time only by_region for the Pandas version
df = pd.read_csv('WDI.csv')
t0 = time.time()
result = by_region(df)
t1 = time.time()
print((t1-t0)*1000)

# Time the Dask version - read the file and call by_region
t0 = time.time()
ddf = dd.read_csv('WDI.csv')
result = by_region(ddf).compute()
t1 = time.time()
print((t1-t0)*1000)


