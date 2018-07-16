import re

re.match('abc', 'abcde')
# match object with 'abc'

re.search('abc', 'abcde')
# match object with 'abc'

re.match('cd', 'abcde')
# no match

re.search('cd', 'abcde')
# match object with 'cd' at index 2

