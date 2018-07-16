from nltk.tokenize import word_tokenize
from collections import Counter

s = "The cat is in the box. The cat likes the box. The box is over the cat."

counter = Counter(word_tokenize(s))
# =>
#Counter({
#  '.': 3,
#  'The': 3,
#  'box': 3,
#  'cat': 3,
#  'in': 1,
#  ...
#  'the': 3
#})

counter.most_common(2)
# => [('The', 3), ('box', 3)]

################################################################################

tokens = word_tokenize(article)
lower_tokens = [t.lower() for t in tokens]
bow_simple = Counter(lower_tokens)
print(bow_simple.most_common(10))

