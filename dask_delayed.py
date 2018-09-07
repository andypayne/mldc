from math import sqrt
from dask import delayed

def f(z):
   return sqrt(z + 4)

def g(y):
   return y - 3

def h(x):
   return x ** 2

x = 4
y = h(x)
z = g(y)
w = f(z)

print(w)  # final result
# 4.123105625617661
print(f(g(h(x))))  # equivalent to before
# 4.123105625617661



y = delayed(h)(x)
z = delayed(g)(y)
w = delayed(f)(z)
print(w)
# Delayed('f-5f9307e5-eb43-4304-877f-1df5c583c11c')

type(w)  # a Dask Delayed object
# dask.delayed.Delayed

w.compute()  # computation occurs now
# 4.123105625617661

w.visualize()
# Visualization - task graph



# Permanently decorate f, g, & h:
f = delayed(f)
g = delayed(g)
h = delayed(h)

w = f(g(h(4))
w.compute()
# 4.123105625617661


