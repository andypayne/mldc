
# Call da.from_array():  energy_dask
energy_dask = da.from_array(energy, chunks = len(energy) // 4)

# Print energy_dask.chunks
print(energy_dask.chunks)

# Print Dask array average and then NumPy array average
print(energy_dask.mean().compute())
print(energy.sum()/len(energy))



# Compare computations with different chunk sizes -

import time

energy_dask4 = da.from_array(energy, chunks=len(energy)//4)
# Print the time to compute the standard deviation
t_start = time.time()
std_4 = energy_dask4.std().compute()
t_end = time.time()
print((t_end - t_start) * 1.0e3)


energy_dask8 = da.from_array(energy, chunks=len(energy) // 8)
# Print the time to compute the standard deviation
t_start = time.time()
std_8 = energy_dask8.std().compute()
t_end = time.time()
print((t_end - t_start) * 1.0e3)


