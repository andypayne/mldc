import re

pattern = "do you remember .*"
message = "do you remember when you ate strawberries in the garden"
match = re.search(pattern, message)
if match:
  print("string matches")

pattern = "if (.*)"
message = "what would you do if bots took over the world"
match = re.serach(pattern, message)

match.group(0) # whole string
match.group(1) # first match
...


# grammatical transformation

def swap_pronouns(phrase):
  if 'I' in phrase:
    return re.sub('I', 'you', phrase)
  if 'my' in phrase:
    return re.sub('my', 'your', phrase)
  else:
    return phrase

swap_pronouns("I walk my dog") # "you walk your dog"



pattern = "do you remember (.*)"
message = "do you remember when you ate strawberries in the garden"
#phrase = pattern.search(pattern, message).group(1) # => "when you ate strawberries in the garden"
phrase = re.search(pattern, message).group(1) # => "when you ate strawberries in the garden"
response = choose_response(pattern)
phrase = swap_pronouns(phrase)


def match_rule(rules, message):
  response, phrase = "default", None
  for pattern, responses in rules.items():
    match = re.search(pattern, message)
    if match is not None:
      response = random.choice(responses)
      if '{0}' in response:
         phrase = match.group(1)
  return response, phrase

print(match_rule(rules, "do you remember your last birthday"))


def replace_pronouns(message):
  message = message.lower()
  if 'me' in message:
    return re.sub('me', 'you', message)
  if 'my' in message:
    return re.sub('my', 'your', message)
  if 'your' in message:
    return re.sub('your', 'my', message)
  if 'you' in message:
    return re.sub('you', 'me', message)
  return message

print(replace_pronouns("my last birthday"))
print(replace_pronouns("when you went to Florida"))
print(replace_pronouns("I had my own castle"))




def respond(message):
  response, phrase = match_rule(rules, message)
  if '{0}' in response:
    phrase = replace_pronouns(phrase)
    response = response.format(phrase)
  return response

send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")



