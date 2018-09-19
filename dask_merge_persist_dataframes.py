
left_df
#   cat_left  value_left
# 0        d           4
# 1        d           9
# 2        b           1
# 3        d           7
# 4        c           3

right_df
#   cat_right  value_right
# 0         b            9
# 1         c            2
# 2         f            0
# 3         d            8
# 4         a            8

# Merge the dataframes with an inner join (the default)
left_df.merge(right_df,
              left_on=['cat_left'],
              right_on=['cat_right'],
              how='inner')
#   cat_left  value_left cat_right  value_right
# 0        d           4         d            8
# 1        d           9         d            8
# 2        d           7         d            8
# 3        b           1         b            9
# 4        c           3         c            2



# For the flight delay and weather data
import dask.dataframe as dd

df = dd.read_csv('flightdelays-2016-*.csv')
%time print(df.WEATHER_DELAY.mean().compute())
# 2.701183508773752
# CPU times: user 3.35 s, sys: 719 ms, total: 4.07 s
# Wall time: 1.64 s
%time print(df.WEATHER_DELAY.std().compute())
# 21.230502105
# CPU times: user 3.33 s, sys: 706 ms, total: 4.04 s
# Wall time: 1.61 s
%time print(df.WEATHER_DELAY.count().compute())
# 192563
# CPU times: user 3.36 s, sys: 695 ms, total: 4.06 s
# Wall time: 1.66 s


# Persisting can speed up subsequent operations on the same dataframe
%time persisted_df = df.persist()
# CPU times: user 3.32 s, sys: 688 ms, total: 4.01 s
# Wall time: 1.59 s
%time print(persisted_df.WEATHER_DELAY.mean().compute())
# 2.701183508773752
# CPU times: user 15.1 ms, sys: 9.24 ms, total: 24.3 ms
# Wall time: 18.5 ms
%time print(persisted_df.WEATHER_DELAY.std().compute())
# 21.230502105
# CPU times: user 29.6 ms, sys: 12.5 ms, total: 42.1 ms
# Wall time: 29.5 ms
%time print(persisted_df.WEATHER_DELAY.count().compute())
# 192563
# CPU times: user 9.88 ms, sys: 2.98 ms, total: 12.9 ms
# Wall time: 9.43 ms


# Print time in milliseconds to compute percentage_delayed on weather_delays
t_start = time.time()
print(percent_delayed(weather_delays).compute())
t_end = time.time()
print((t_end-t_start)*1000)

# Persisted version
persisted_weather_delays = weather_delays.persist()
# Print time in milliseconds to compute percentage_delayed on persisted_weather_delays
t_start = time.time()
print(percent_delayed(persisted_weather_delays).compute())
t_end = time.time()
print((t_end-t_start)*1000)



# Group persisted_weather_delays by 'Events'
by_event = persisted_weather_delays.groupby('Events')

# Count 'by_event['WEATHER_DELAY'] column & divide by total number of delayed flights
pct_delayed = 100*by_event['WEATHER_DELAY'].count()/persisted_weather_delays['WEATHER_DELAY'].count()

# Compute & print five largest values of pct_delayed
print(pct_delayed.compute().nlargest(5))

# Calculate mean of by_event['WEATHER_DELAY'] column & return the 5 largest entries
avg_delay_time = by_event['WEATHER_DELAY'].mean().nlargest(5)
print(avg_delay_time.compute())


