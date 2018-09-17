from math import sqrt
from dask import delayed


template = 'yellow_tripdata_2015-{:02d}.csv'
filenames = [template.format(k) for k in range(1,13)]

@delayed
def count_long_trips(df):
    df['duration'] = (df.tpep_dropoff_datetime -
                      df.tpep_pickup_datetime).dt.seconds
    is_long_trip = df.duration > 1200
    result_dict = {'n_long':[sum(is_long_trip)],
                   'n_total':[len(df)]}
    return pd.DataFrame(result_dict)

@delayed
def read_file(fname):
    return pd.read_csv(fname, parse_dates=[1,2])

totals = [count_long_trips(read_file(fname)) for fname in filenames]
annual_totals = sum(totals)
annual_totals = annual_totals.compute()
# Dataframe -
#   n_long  n_total
#0  172617   851390

fraction = annual_totals['n_long'] / annual_totals['n_total']

print(fraction)
# 0    0.202747
# dtype: float64





@delayed
def count_flights(df):
    return len(df)

@delayed
def count_delayed(df):
    return (df['DEP_DELAY'] > 0).sum()

@delayed
def pct_delayed(n_delayed, n_flights):
    return 100 * sum(n_delayed) / sum(n_flights)


for file in filenames:
    df = read_one(file)
    n_delayed.append(count_delayed(df))
    n_flights.append(count_flights(df))

result = pct_delayed(n_delayed, n_flights)
print(result.compute())
# 34.199953360948875


