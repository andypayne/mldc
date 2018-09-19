import pandas as pd

df = pd.read_csv('DEN.csv', parse_dates=True, index_col='Date')

df.columns
# Index(['Max TemperatureF', 'Mean TemperatureF', 'Min TemperatureF',
#        'Max Dew PointF', 'MeanDew PointF', 'Min DewpointF', 'Max Humidity',
#        'Mean Humidity', 'Min Humidity', 'Max Sea Level PressureIn',
#        'Mean Sea Level PressureIn', 'Min Sea Level PressureIn',
#        'Max VisibilityMiles', 'Mean VisibilityMiles', 
#        'Min VisibilityMiles',
#        'Max Wind SpeedMPH', 'Mean Wind SpeedMPH', 'Max Gust SpeedMPH',
#        'PrecipitationIn', 'CloudCover', 'Events', 'WindDirDegrees'],
#       dtype='object')

df.loc['March 2016', ['PrecipitationIn','Events']].tail()
#            PrecipitationIn             Events
# Date                                         
# 2016-03-27            0.00                NaN
# 2016-03-28            0.00                NaN
# 2016-03-29            0.04  Rain-Thunderstorm
# 2016-03-30            0.04          Rain-Snow
# 2016-03-31            0.01               Snow

# The PrecipitationIn column is misleading. The values are strings, not numbers.
df['PrecipitationIn'][0]
# '0.00'
type(df['PrecipitationIn'][0])
# str

df[['PrecipitationIn', 'Events']].info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 366 entries, 0 to 365
# Data columns (total 2 columns):
# PrecipitationIn    366 non-null object
# Events             115 non-null object
# dtypes: object(2)
# memory usage: 5.8+ KB

# PrecipitationIn contains a mix of strings and numeric values, so its type is str,
# and it needs to be cleaned to be usable.
# pd.to_numeric can do this.
series
# 0      0
# 1      M
# 2      2
# 3    1.5
# 4      E
# dtype: object
new_series = pd.to_numeric(series, errors='coerce')

new_series
# 0    0.0
# 1    NaN
# 2    2.0
# 3    1.5
# 4    NaN
# dtype: float64


@delayed
def read_weather(filename):
    df = pd.read_csv(filename, parse_dates=['Date'])
    df['PrecipitationIn'] = pd.to_numeric(df['PrecipitationIn'], errors='coerce')
    df['Airport'] = filename.split('.')[0]
    return df

for filename in filenames:
    weather_dfs.append(read_weather(filename))
weather = dd.from_delayed(weather_dfs)
print(weather.nlargest(1, 'Max TemperatureF').compute())


# Which cities are the snowiest?
# Make cleaned Boolean Series from weather['Events']
is_snowy = weather['Events'].str.contains('Snow').fillna(False)

# Create filtered DataFrame with weather.loc & is_snowy
got_snow = weather.loc[is_snowy]

result = got_snow.groupby('Airport')['PrecipitationIn'].sum()
print(result.compute())


