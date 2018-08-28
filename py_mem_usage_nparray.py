import psutil, os
import numpy as np

def memory_footprint():
  '''Returns memory (in MB) being used by the Python process'''
  mem = psutil.Process(os.getpid()).memory_info().rss
  return (mem / 1024 ** 2)



before = memory_footprint()
N = (1024 ** 2) // 8 # Number of floats that fill 1 MB

x = np.random.randn(50*N) # Random array filling 50 MB
print('Memory usage for x: {} MB'.format(x.nbytes / 1024 ** 2))

after = memory_footprint()
print('Memory before: {} MB'.format(before))
# Memory before: 45.68359375 MB

print('Memory after: {} MB'.format(after))
# Memory after: 95.765625 MB

print('Usage: {} MB'.format(after - before))


before2 = memory_footprint()

x ** 2 # Computes, but doesn't bind result to a variable
# array([ 0.16344891,  0.05993282,  0.53595334, ...,  0.50537523,
#         0.48967157,  0.06905984])

after2 = memory_footprint()

print('Extra memory obtained: {} MB'.format(after2 - before2))
# Extra memory obtained: 50.34375 MB

