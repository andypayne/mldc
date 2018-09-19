import pandas as pd
from dask import delayed

@delayed
def pipeline(filename, account_name):
    df = pd.read_csv(filename)
    df['account_name'] = account_name
    return df

delayed_dfs = []

for account in ['Bob', 'Alice', 'Dave']:
   fname = 'accounts/{}.csv'.format(account)
   delayed_dfs.append(pipeline(fname, account))

import dask.dataframe as dd

dask_df = dd.from_delayed(delayed_dfs)
dask_df['amount'].mean().compute()
# 10.56476


"""
Cleaning flight delays

Use .replace(): 0 \rightarrow→ NaN
Cleaning weather data

'PrecipitationIn': text \rightarrow→ numeric
Add column for airport code
"""

df = pd.read_csv('flightdelays-2016-1.csv')
df.columns
# Index(['FL_DATE', 'UNIQUE_CARRIER', 'FL_NUM', 'ORIGIN', 'ORIGIN_CITY_NAME',
#        'ORIGIN_STATE_ABR', 'ORIGIN_STATE_NM', 'DEST', 'DEST_CITY_NAME',
#        'DEST_STATE_ABR', 'DEST_STATE_NM', 'CRS_DEP_TIME', 'DEP_DELAY',
#        'CRS_ARR_TIME', 'ARR_DELAY', 'CANCELLED', 'DIVERTED', 'CARRIER_DELAY',
#        'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY',
#        'Unnamed: 22'],
#       dtype='object')

df['WEATHER_DELAY'].tail()
# 89160    NaN
# 89161    0.0
# 89162    NaN
# 89163    NaN
# 89164    NaN
# Name: WEATHER_DELAY, dtype: float64

# .replace -
"""
In [12]: series
Out[12]: 
0    6
1    0
2    6
3    5
4    7
dtype: int64
In [13]: new_series = series.replace(6, np.nan)

In [14]: new_series
Out[14]: 
0    NaN
1    0.0
2    NaN
3    5.0
4    7.0
dtype: float64
"""


@delayed
def read_flights(filename):
    df = pd.read_csv(filename, parse_dates=['FL_DATE'])
    df['WEATHER_DELAY'] = df['WEATHER_DELAY'].replace(0, np.nan)
    return df

for filename in filenames:
    dataframes.append(read_flights(filename))

flight_delays = dd.from_delayed(dataframes)
print(flight_delays['WEATHER_DELAY'].mean().compute())



