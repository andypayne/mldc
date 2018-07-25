
INIT = 0
CHOOSE_COFFEE = 1
ORDERED = 2

# Policy rules - dictionary
# Keys = tuples of current state and expressed intent
# Values = tuples of next state and message relayed to user
policy_rules = {
  (INIT, "order"): (CHOOSE_COFFEE, "ok, Colombian or Kenyan?"),
  (CHOOSE_COFFEE, "specify_coffee"): (ORDERED, "perfect, the beans are on their way")
}

state = INIT

# interpret() returns the intent for a given message
def repond(state, message):
  (new_state, response) = policy_rules[(state, interpret(message))]
  return new_state, response

def send_message(state, message):
  new_state, response = respond(state, message)
  return new_state

state = send_message(state, message)



INIT = 0
CHOOSE_COFFEE = 1
ORDERED = 2

policy = {
  (INIT, "order"): (CHOOSE_COFFEE, "ok, Colombian or Kenyan?"),
  (INIT, "none"): (INIT, "I'm sorry - I'm not sure how to help you"),
  (CHOOSE_COFFEE, "specify_coffee"): (ORDERED, "perfect, the beans are on their way!"),
  (CHOOSE_COFFEE, "none"): (CHOOSE_COFFEE, "I'm sorry - would you like Colombian or Kenyan?"),
}

messages = [
  "I'd like to become a professional dancer",
  "well then I'd like to order some coffee",
  "my favourite animal is a zebra",
  "kenyan"
]

state = INIT
for message in messages:    
  state = send_message(policy, state, message)

"""
USER : I'd like to become a professional dancer
BOT : I'm sorry - I'm not sure how to help you
USER : well then I'd like to order some coffee
BOT : ok, Colombian or Kenyan?
USER : my favourite animal is a zebra
BOT : I'm sorry - would you like Colombian or Kenyan?
USER : kenyan
BOT : perfect, the beans are on their way!
"""



INIT=0 
CHOOSE_COFFEE=1
ORDERED=2

# Now with a help option
policy_rules = {
    (INIT, "ask_explanation"): (INIT, "I'm a bot to help you order coffee beans"),
    (INIT, "order"): (CHOOSE_COFFEE, "ok, Columbian or Kenyan?"),
    (CHOOSE_COFFEE, "specify_coffee"): (ORDERED, "perfect, the beans are on their way!"),
    (CHOOSE_COFFEE, "ask_explanation"): (CHOOSE_COFFEE, "We have two kinds of coffee beans - the Kenyan ones make a slightly sweeter coffee, and cost $6. The Brazilian beans make a nutty coffee and cost $5.")    
}

def send_messages(messages):
  state = INIT
  for msg in messages:
    state = send_message(state, msg)

send_messages([
  "what can you do for me?",
  "well then I'd like to order some coffee",
  "what do you mean by that?",
  "kenyan"
])

"""
USER : what can you do for me?
BOT : I'm a bot to help you order coffee beans
USER : well then I'd like to order some coffee
BOT : ok, Columbian or Kenyan?
USER : what do you mean by that?
BOT : We have two kinds of coffee beans - the Kenyan ones make a slightly sweeter coffee, and cost $6. The Brazilian beans make a nutty coffee and cost $5.
USER : kenyan
BOT : perfect, the beans are on their way!
"""




# Define respond()
def respond(message, params, prev_suggestions, excluded):
  # Interpret the message
  parse_data = interpret(message)
  # Extract the intent
  intent = parse_data["intent"]["name"]
  # Extract the entities
  entities = parse_data["entities"]
  # Add the suggestion to the excluded list if intent is "deny"
  if intent == "deny":
      excluded.extend(prev_suggestions)
  # Fill the dictionary with entities
  for ent in entities:
      params[ent["entity"]] = str(ent["value"])
  # Find matching hotels
  results = [
    r
    for r in find_hotels(params, excluded)
    if r[0] not in excluded
  ]
  # Extract the suggestions
  names = [r[0] for r in results]
  n = min(len(results), 3)
  suggestions = names[:2]
  return responses[n].format(*names), params, suggestions, excluded

# Initialize the empty dictionary and lists
params, suggestions, excluded = {}, [], []

# Send the messages
for message in ["I want a mid range hotel", "no that doesn't work for me"]:
  print("USER: {}".format(message))
  response, params, suggestions, excluded = respond(message, params, suggestions, excluded)
  print("BOT: {}".format(response))


"""
USER: I want a mid range hotel
BOT: Hotel for Dogs is one option, but I know others too :)
USER: no that doesn't work for me
BOT: Grand Hotel is one option, but I know others too :)
"""


