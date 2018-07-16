import re

match_digits_and_words = ('(\d+|\w+)')

re.findall(match_digits_and_words, 'He has 11 cats.')
# => ['He', 'has', '11', 'cats']


