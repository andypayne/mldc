import h5py, time

with h5py.File('dist.hdf5', 'r') as dset:
    dist = dset['dist'][:]

dist_dask8 = da.from_array(dist, chunks=dist.shape[0]//8)
t_start = time.time(); \
mean8 = dist_dask8.mean().compute(); \
t_end = time.time()
t_elapsed = (t_end - t_start) * 1000

print('Elapsed time: {} ms'.format(t_elapsed))
# Elapsed time: 180.96423149108887 ms

