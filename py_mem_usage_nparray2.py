print(celsius.nbytes // (1024 ** 2))
before = memory_footprint()
fahrenheit = (9/5) * celsius + 32
after = memory_footprint()
print(after - before)

