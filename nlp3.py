
# ...

# tokenize on whitespace & punctuation
# include unigrams & bigrams
vec = CountVectorizer(token_pattern=TOKENS_ALPHANUMERIC, ngram_range=(1, 2))

# ...

