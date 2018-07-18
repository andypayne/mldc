name = "Greg"
weather = "cloudy"

responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "default message"
}

def respond(message):
  if message in responses:
    bot_message = responses[message]
  else:
    bot_message = responses["default"]
  return bot_message


################################################################################

import random

name = "Greg"
weather = "cloudy"

responses = {
  "what's your name?": [
    "my name is {0}".format(name),
    "they call me {0}".format(name),
    "I go by {0}".format(name)
   ],
  "what's today's weather?": [
    "the weather is {0}".format(weather),
    "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}

def respond(message):
  if message in responses:
    bot_message = random.choice(responses[message])
  else:
    bot_message = random.choice(responses["default"])
  return bot_message


################################################################################

import random

def respond(message):
  # Check for a question mark
  if message.endswith('?'):
    # Return a random question
    return random.choice(responses["question"])
  # Return a random statement
  return random.choice(responses["statement"])


# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")

