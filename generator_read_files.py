
template = 'yellow_tripdata_2015-{:02d}.csv'
filenames = (template.format(k) for k in range(1,13))

for fname in filenames:
     print(fname)
# yellow_tripdata_2015-01.csv
# yellow_tripdata_2015-02.csv
# yellow_tripdata_2015-03.csv
# yellow_tripdata_2015-04.csv
# yellow_tripdata_2015-05.csv
# yellow_tripdata_2015-06.csv
# yellow_tripdata_2015-07.csv
# yellow_tripdata_2015-08.csv
# yellow_tripdata_2015-09.csv
# yellow_tripdata_2015-10.csv
# yellow_tripdata_2015-11.csv
# yellow_tripdata_2015-12.csv



# Columns 1 and 2 are datetime objects
df = pd.read_csv('yellow_tripdata_2015-12.csv', parse_dates=[1, 2])

df.info()  # columns deleted from output
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 71634 entries, 0 to 71633
# Data columns (total 19 columns):
# VendorID                 71634 non-null int64
# tpep_pickup_datetime     71634 non-null datetime64[ns]
# tpep_dropoff_datetime    71634 non-null datetime64[ns]
# passenger_count          71634 non-null int64
# ...
# ...
# dtypes: datetime64[ns](2), float64(12), int64(4), object(1)
# memory usage: 10.4+ MB




def count_long_trips(df):
    df['duration'] = (df.tpep_dropoff_datetime -
                       df.tpep_pickup_datetime).dt.seconds
    is_long_trip = df.duration > 1200
    result_dict = {'n_long':[sum(is_long_trip)],
                   'n_total':[len(df)]}
    return pd.DataFrame(result_dict)


filenames = [template.format(k) for k in range(1,13)] # listcomp
dataframes = (pd.read_csv(fname, parse_dates=[1,2])
                  for fname in filenames)  # generator

totals = (count_long_trips(df) for df in dataframes) # generator

# The calculations happen here 
annual_totals = sum(totals) # Consumes generators

print(annual_totals)
#    n_long  n_total
# 0  172617   851390

fraction = annual_totals['n_long'] / annual_totals['n_total']

print(fraction)
# 0    0.202747
# dtype: float64





def pct_delayed(df):
    n_delayed = (df['DEP_DELAY'] > 0).sum()
    return n_delayed  * 100 / len(df)


dataframes = (pd.read_csv(file) for file in filenames)

monthly_delayed = [pct_delayed(df) for df in dataframes]

x = range(1,13)
plt.plot(x, monthly_delayed, marker='o', linewidth=0)
plt.ylabel('% Delayed')
plt.xlabel('Month - 2016')
plt.xlim((1,12))
plt.ylim((0,100))
plt.show()


