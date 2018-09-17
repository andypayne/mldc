
import dask.dataframe as dd

# Reading CSV
# dd.read_csv() - accepts a single filename or glob pattern
# Does not read files immediately (lazy evaluation)
# File(s) need not fit in memory

# %ls is an ipython feature
%ls 
# quarter1.csv  quarter2.csv  quarter3.csv  quarter4.csv
# The data from all files are concatenated into a single dask dataframe
transactions = dd.read_csv('*.csv')

transactions.head()
#     id    names  amount        date
# 0  131  Norbert   -1159  2016-01-01
# 1  342    Jerry    1149  2016-01-01
# 2  485      Dan    1380  2016-01-01
# 3  513   Xavier    1555  2016-01-02
# 4  849  Michael     363  2016-01-02
transactions.tail()
#       id     names  amount        date
# 195  838     Wendy      87  2016-12-28
# 196  915       Bob     852  2016-12-30
# 197  749  Patricia    1741  2016-12-31
# 198  743   Michael    1191  2016-12-31
# 199  889     Wendy     336  2016-12-31


is_wendy = (transactions['names'] == 'Wendy')
wendy_amounts = transactions.loc[is_wendy, 'amount']

wendy_amounts
# Dask Series Structure:
# npartitions=4
# None    int64
# None      ...
# None      ...
# None      ...
# None      ...
# Name: amount, dtype: int64
# Dask Name: loc-series, 24 tasks

wendy_diff = wendy_amounts.sum()
wendy_diff
# dd.Scalar<series-..., dtype=int64>

wendy_diff.visualize(rankdir='LR')


# Some pandas features are unavailable in dask.dataframe:
# - unsupported file formats (e.g., .xls, .zip, .gz)
# - sorting
# Available in dask.dataframe:
# - indexing, selection, & reindexing
# - aggregations: .sum(), .mean(), .std(), .min(), .max() etc.
# - grouping with .groupby()
# - datetime conversion with dd.to_datetime()


# Read from 'WDI.csv': df
df = dd.read_csv('WDI.csv')
# Boolean series where 'Indicator Code' is 'EN.ATM.PM25.MC.ZS'
toxins = df['Indicator Code'] == 'EN.ATM.PM25.MC.ZS'
# Boolean series where 'Region' is 'East Asia & Pacific'
region = df['Region'] == 'East Asia & Pacific'
# Filter the DataFrame using toxins & region
filtered = df.loc[toxins & region]

# Group filtered by the 'Year' column
yearly = filtered.groupby('Year')
# Aggregate the mean of the groupby object
yearly_mean = yearly.mean()
result = yearly_mean.compute()
# Plot
result['value'].plot.line()
plt.ylabel('% pop exposed')
plt.show()

