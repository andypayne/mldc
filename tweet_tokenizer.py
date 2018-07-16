from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

# hashtags
pattern1 = r"#\w+"
regexp_tokenize(tweets[0], pattern1)

# mentions and hashtags
pattern2 = r"([@#]\w+)"
regexp_tokenize(tweets[-1], pattern2)

tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)

