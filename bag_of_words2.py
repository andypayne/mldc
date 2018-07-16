from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

s = "The cat is in the box. The cat likes the box. The box is over the cat."

tokens = [w for w in word_tokenize(s.lower()) if w.isalpha()]
no_stops = [t for t in tokens if t not in stopwords.words('english')]

Counter(no_stops).most_common(2)
# => [('cat', 3), ('box', 3)]


################################################################################

from nltk.stem import WordNetLemmatizer

alpha_only = [t for t in lower_tokens if t.isalpha()]
no_stops = [t for t in alpha_only if t not in english_stops]

wordnet_lemmatizer = WordNetLemmatizer()
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

bow = Counter(lemmatized)
print(bow.most_common(10))


