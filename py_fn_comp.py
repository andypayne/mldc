from math import sqrt

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

print(w) # final result
# 4.123105625617661
print(f(g(h(x)))) # equivalent to before
# 4.123105625617661


