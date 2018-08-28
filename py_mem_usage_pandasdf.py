import psutil, os
import numpy as np
import pandas as pd

def memory_footprint():
  '''Returns memory (in MB) being used by the Python process'''
  mem = psutil.Process(os.getpid()).memory_info().rss
  return (mem / 1024 ** 2)



before = memory_footprint()
N = (1024 ** 2) // 8

x = np.random.randn(50*N)
print('Memory usage for x: {} MB'.format(x.nbytes / 1024 ** 2))

after = memory_footprint()
print('Memory before: {} MB'.format(before))
# Memory before: 45.68359375 MB

print('Memory after: {} MB'.format(after))
# Memory after: 95.765625 MB

print('Usage: {} MB'.format(after - before))


df = pd.DataFrame(x)
print(df.memory_usage(index=False))
# 0    52428800
# dtype: int64

print(df.memory_usage(index=False) // (1024 ** 2))
# 0    50
# dtype: int64

