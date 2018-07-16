


all_words = word_tokenize(german_text)
print(all_words)


capital_words = r"[A-Z|Ü]\w+"
print(regexp_tokenize(german_text, capital_words))


emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(regexp_tokenize(german_text, emoji))


