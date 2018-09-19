
filenames = glob.glob('sotu/*.txt')
filenames = sorted(filenames)
# Dask bag
speeches = db.read_text(filenames)
print(speeches.count().compute())

one_element = speeches.take(1)
# Extract first element of one_element
first_speech = one_element[0]
# Print the type of first_speech and the first 60 characters
print(type(first_speech))
print(first_speech[0:60])


