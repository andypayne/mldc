import h5py

data_store = h5py.File('tmax.2008.hdf5')
# One key named tmax - max temp
for key in data_store.keys():
    print(key)
# tmax

data = data_store['tmax']
type(data)
# h5py._hl.dataset.Dataset
data.ndim
# 3

# A 3D array: (2D for each month)
data.shape
# (12, 444, 922)

import dask.array as da

data_dask = da.from_array(data, chunks=(1, 444, 922))


# Yields an unevaluated dask array
data_dask.min()
# dask.array<amin-aggregate, shape=(), dtype=float64, chunksize=()>
# Force computation
data_dask.min().compute()
# nan
# No min(), because there are NaN values

# Dask has NaN-aware computations
da.nanmin(data_dask).compute()
# -22.329354809176536

lo = da.nanmin(data_dask).compute()
hi = da.nanmax(data_dask).compute()
print(lo, hi)
# -22.3293548092 47.7625806255


# Visualizing the temperature maps -

# Number of images
N_months = data_dask.shape[0]

import matplotlib.pyplot as plt

fig, panels = plt.subplots(nrows=4, ncols=3)
for month, panel in zip(range(N_months), panels.flatten()):
    im = panel.imshow(data_dask[month, :, :],
                       origin='lower',
                       vmin=lo, vmax=hi)
    panel.set_title('2008-{:02d}'.format(month+1))
    panel.axis('off')
plt.suptitle('Monthly averages (max. daily temperature [C])');
plt.colorbar(im, ax=panels.ravel().tolist()); # Common colorbar
plt.show()



# Stacking numpy arrays
import numpy as np
a = np.ones(3); b = 2 * a; c = 3 * a

print(a, '\n'); print(b, '\n'); print(c)
# [ 1.  1.  1.]
# 
# [ 2.  2.  2.]
# 
# [ 3.  3.  3.]

# Makes a 2D array of shape (2,3)
np.stack([a, b])
# array([[ 1.,  1.,  1.],
#        [ 2.,  2.,  2.]])
# Same as above
np.stack([a, b], axis=0)
# array([[ 1.,  1.,  1.],
#        [ 2.,  2.,  2.]])
# Makes a 2D array of shape (3,2)
np.stack([a, b], axis=1)
# array([[ 1.,  2.],
#        [ 1.,  2.],
#        [ 1.,  2.]])


X = np.stack([a, b]); \
Y = np.stack([b, c]); \
Z = np.stack([c, a])
print(X, '\n'); print(Y, '\n'); print(Z, '\n')
# [[ 1.  1.  1.]
#  [ 2.  2.  2.]]
# 
# [[ 2.  2.  2.]
#  [ 3.  3.  3.]]
# 
# [[ 3.  3.  3.]
#  [ 1.  1.  1.]]


# Makes a 3D array of shape (3, 2, 3)
np.stack([X, Y, Z])
# array([[[ 1.,  1.,  1.],
#         [ 2.,  2.,  2.]],
# 
#        [[ 2.,  2.,  2.],
#         [ 3.,  3.,  3.]],
# 
#        [[ 3.,  3.,  3.],
#         [ 1.,  1.,  1.]]])
# Makes a 3D array of shape (2, 3, 3)
np.stack([X, Y, Z], axis=1)
# array([[[ 1.,  1.,  1.],
#         [ 2.,  2.,  2.],
#         [ 3.,  3.,  3.]],
# 
#        [[ 2.,  2.,  2.],
#         [ 3.,  3.,  3.],
#         [ 1.,  1.,  1.]]])0




import h5py
import dask.array as da

dsets = [h5py.File(f)['tmax'] for f in filenames]
monthly = [da.from_array(d, chunks=(1,444,922)) for d in dsets]
# Stack with the list of dask arrays
by_year = da.stack(monthly, axis=0)
print(by_year.shape)
# (4, 12, 444, 922)
dset = h5py.File('tmax.climate.hdf5')
climatology = da.from_array(dset['/tmax'], chunks=(1,444,922))

# Reshape the climatology data to be compatible with months
climatology.reshape(1, 12, 444, 922)


# Compute the difference
diff = (9/5) * (by_year - climatology)
# Compute the average over last two axes
avg = da.nanmean(diff, axis=(-1, -2)).compute()
# Plot the slices [:,0], [:,7], and [:11] against the x values
x = range(2008,2012)
f, ax = plt.subplots()
ax.plot(x,avg[:,0], label='Jan')
ax.plot(x,avg[:,7], label='Aug')
ax.plot(x,avg[:,11], label='Dec')
ax.axhline(0, color='red')
ax.set_xlabel('Year')
ax.set_ylabel('Difference (degrees Fahrenheit)')
ax.legend(loc=0)
plt.show()


