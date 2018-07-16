import re

sentence_endings = r"[.?!]"
print(re.split(sentence_endings, my_string))

capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, my_string))

spaces = r"\s+"
print(re.split(spaces, my_string))

digits = r"\d"
print(re.findall(digits, my_string))

