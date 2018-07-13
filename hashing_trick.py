from sklearn.feature_extraction.text import HashingVectorizer

# First two params allow us to use this in place of the CountVectorizer
vec = HashingVectorizer(norm=None, non_negative=True, token_pattern=TOKENS_ALPHANUMERIC, ngram_range=(1, 2))



