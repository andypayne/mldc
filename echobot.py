import time

def respond(msg):
  return "I can hear you. You said: {}".format(msg)

def send_message(msg):
  rsp = respond(msg)
  time.sleep(0.5)
  print(rsp)


bot_template = "BOT : {0}"
user_template = "USER : {0}"

def respond(message):
  bot_message = "I can hear you! You said: " + message
  return bot_message


def send_message(message):
	print(user_template.format(message))
	response = respond(message)
	print(bot_template.format(response))

send_message("hello")


################################################################################

responses = {
	"what's your name?": "my name is EchoBot",
	"what's the weather today?": "it's sunny!"
}

def respond(msg):
	if msg in responses:
		return responses[msg]


################################################################################

responses = {
	"what's the weather today?": "it's {} today"
}

...
weather_today = "cloudy"
responses[message].format(weather_today)
...


################################################################################

import random

responses = {
	"what's your name?": [
		"my name is EchoBot",
		"they call me EchoBot",
		"the name's Bot, Echo Bot"
	]
}

return random.choice(responses[message])



