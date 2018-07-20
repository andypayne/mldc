import re

re.search(r"(hello|hey|hi)", "hey there!") is not None
# => True

re.search(r"(hello|hey|hi)", "which one?") is not None
# => True

re.search(r"\b(hello|hey|hi)\b", "which one?") is not None
# => False


pattern = re.compile('[A-Z]{1}[a-z]*')

message = "Mary is a friend of mine, she studied at Oxford and now works at Google"
pattern.findall(message)
# => ['Mary', 'Oxford', 'Google']



patterns = {}
for intent, keys in keywords.items():
  patterns[intent] = re.compile('|'.join(keys))
print(patterns)



def match_intent(message):
  matched_intent = None
  for intent, pattern in patterns.items():
    if pattern.search(message):
      matched_intent = intent
  return matched_intent

def respond(message):
  intent = match_intent(message)
  key = "default"
  if intent in responses:
    key = intent
  return responses[key]

send_message("hello!")
send_message("bye byeee")
send_message("thanks very much!")




# Define find_name()
def find_name(message):
	name = None
	# Create a pattern for checking if the keywords occur
	name_keyword = re.compile(r"name|call")
	# Create a pattern for finding capitalized words
	name_pattern = re.compile(r"[A-Z]{1}[a-z]*")
	if name_keyword.search(message):
		# Get the matching words in the string
		name_words = name_pattern.findall(message)
		if len(name_words) > 0:
			# Return the name if the keywords are present
			name = ' '.join(name_words)
	return name

# Define respond()
def respond(message):
	# Find the name
	name = find_name(message)
	if name is None:
			return "Hi there!"
	else:
			return "Hello, {0}!".format(name)

# Send messages
send_message("my name is David Copperfield")
send_message("call me Ishmael")
send_message("People call me Cassandra")




