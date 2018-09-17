# Comparison with numpy
import numpy as np

time_series = np.loadtxt('max_temps.csv', dtype=np.int64)
print(time_series.dtype)
# int64
print(time_series.shape)
# (21,)
print(time_series.ndim)
# 1
print(time_series)
# [49 51 60 54 47 50 64 58 47 43 50 63 67 68 64 48 55 46 66 51 52]

# Reshaped row-wise
table = time_series.reshape((3,7))
print(table)
# [[49 51 60 54 47 50 64]
#  [58 47 43 50 63 67 68]
#  [64 48 55 46 66 51 52]]

# Reshaping column-wise - this is incorrect
time_series.reshape((7,3))
# array([[49, 51, 60],
#        [54, 47, 50],
#        [64, 58, 47],
#        [43, 50, 63],
#        [67, 68, 64],
#        [48, 55, 46],
#        [66, 51, 52]])

# Reshaping column-wise - you have to pass order='F'
# order='C' ==> C ordering (default)
# order='F' ==> Fortran ordering
time_series.reshape((7,3), order='F')
# array([[49, 58, 64],
#        [51, 47, 48],
#        [60, 43, 55],
#        [54, 50, 46],
#        [47, 63, 66],
#        [50, 67, 51],
#        [64, 68, 52]])


print(table) # Display the result
# [[49 51 60 54 47 50 64]
#  [58 47 43 50 63 67 68]
#  [64 48 55 46 66 51 52]]
table[0, 4] # value from Week 0, Day 4 [Day 5? zero ordering]
# Out[13]: 47

table[1, 2:5] # values from Week 1, Days 2, 3, & 4
# array([43, 50, 63])
table[0::2, ::3] # values from Weeks 0 & 2, Days 0, 3, & 6
# array([[49, 54, 64],
#        [64, 46, 52]])
table[0] # Equivalent to table[0, :]
# array([49, 51, 60, 54, 47, 50, 64])



print(table)
# [[49 51 60 54 47 50 64]
# [58 47 43 50 63 67 68]
# [64 48 55 46 66 51 52]]

# Mean of every entry in the table
table.mean()
# 54.904761904761905

# Mean computed of rows (for each day)
daily_means = table.mean(axis=0)
daily_means
# array([ 57.        ,  48.66666667,  52.66666667,  50.        ,
#         58.66666667,  56.        ,  61.33333333])

# Mean computed of columns (for each week)
weekly_means = table.mean(axis=1)
weekly_means
# array([ 53.57142857,  56.57142857,  54.57142857])

# Mean of rows, then columns
table.mean(axis=(0,1))
# 54.904761904761905

# Subtract the means - this works
table - daily_means
# array([[ -8.        ,   2.33333333,   7.33333333,   4.        ,
#         -11.66666667,  -6.        ,   2.66666667],
#        [  1.        ,  -1.66666667,  -9.66666667,   0.        ,
#           4.33333333,  11.        ,   6.66666667],
#        [  7.        ,  -0.66666667,   2.33333333,  -4.        ,
#           7.33333333,  -5.        ,  -9.33333333]])

# This doesn't work
table - weekly_means
#  ---------------------------------------------------------------------------
#  ValueError                                Traceback (most recent call last)
#  ----> 1 table - weekly_means
#   ValueError: operands could not be broadcast together with shapes (3,7) (3,)

# Numpy broadcasting rules -
# Compatible Arrays:
# 1. same ndim: all dimensions same or 1
# 2. different ndim: smaller shape prepended with ones & #1. applies
# Broadcasting: copy array values to missing dimensions, then do arithmetic

print(table.shape)
# (3, 7)
# print(daily_means.shape)
# (7,)
# print(weekly_means.shape)
# (3,)
# Reshaping - this works now
result = table - weekly_means.reshape((3,1))

# Reshape - 
# table - daily_means: (3,7) - (7,) \rightarrow→ (3,7) - (1,7): compatible
# table - weekly_means: (3,7) - (3,) \rightarrow→ (3,7) - (1,3): incompatible
# table - weekly_means.reshape((3,1)): (3,7) - (3,1): compatible




data = np.loadtxt('', usecols=(1,2,3,4), dtype=np.int64)
data.shape
# (366, 4)

type(data)
# numpy.ndarray
data_dask = da.from_array(data, chunks=(366,2))
# Standard deviation down columns
result = data_dask.std(axis=0)
result.compute()
# array([ 15.08196053,  14.9456851 ,  15.52548285,  14.47228351])



# Reshape load_recent to three dimensions
# 3 years, each with 365 days, each with 96 chunks of 15 minutes
load_recent_3d = load_recent.reshape(3, 365, 96)

# Reshape load_2001 to three dimensions
# Only 1 year
load_2001_3d = load_2001.reshape(1, 365, 96)

# Subtract the load in 2001 from the load in 2013 - 2015
diff_3d = load_recent_3d - load_2001_3d

# Print the difference from each year to 2001 on March 2 at noon
print(diff_3d[:, 61, 48])


# Print mean value of load_recent_3d
print(load_recent_3d.mean())

# Print maximum of load_recent_3d across 2nd & 3rd dimensions
print(load_recent_3d.max(axis=(1,2)))

# Compute sum along last dimension of load_recent_3d: daily_consumption
daily_consumption = load_recent_3d.sum(axis=-1)

# Print mean of 62nd row of daily_consumption
print(daily_consumption.mean(axis=0)[61])

