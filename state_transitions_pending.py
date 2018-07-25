
message = "I'd like to order some coffee"

state = INIT
action = "request_auth"
pending_state = AUTHED

response = "Sounds good! I'd love to help you but you'll have to login first, what's your phone number?"

message = "555-1212"

state = AUTHED
action = "acknowledge_auth"
pending_state = NONE

response = "Perfect! Welcome back."



def policy(intent):
  if intent == "affirm":
    return "do_pending", None
  if intent == "deny":
    return "Ok", None
  if intent == "order":
    return "Unfortunately, the Kenyan coffee is currently out of stock, would you like to order the Brazilian beans?", "Alright, I've ordered that for you!"


def send_message(pending, message):
  print("USER : {}".format(message))
  action, pending_action = policy(interpret(message))
  if action == "do_pending" and pending is not None:
    print("BOT : {}".format(pending))
  else:
    print("BOT : {}".format(action))
  return pending_action
    
def send_messages(messages):
  pending = None
  for msg in messages:
    pending = send_message(pending, msg)


send_messages([
  "I'd like to order some coffee",
  "ok yes please"
])


"""
USER : I'd like to order some coffee
BOT : Unfortunately, the Kenyan coffee is currently out of stock, would you like to order the Brazilian beans?
USER : ok yes please
BOT : Alright, I've ordered that for you!
"""



# Define the states
INIT=0
AUTHED=1
CHOOSE_COFFEE=2
ORDERED=3

# Define the policy rules
policy_rules = {
  (INIT, "order"): (INIT, "you'll have to log in first, what's your phone number?", AUTHED),
  (INIT, "number"): (AUTHED, "perfect, welcome back!", None),
  (AUTHED, "order"): (CHOOSE_COFFEE, "would you like Columbian or Kenyan?", None),    
  (CHOOSE_COFFEE, "specify_coffee"): (ORDERED, "perfect, the beans are on their way!", None)
}

# Define send_messages()
def send_messages(messages):
  state = INIT
  pending = None
  for msg in messages:
    state, pending = send_message(state, pending, msg)

# Send the messages
send_messages([
  "I'd like to order some coffee",
  "555-12345",
  "kenyan"
])


"""
USER : I'd like to order some coffee
BOT : you'll have to log in first, what's your phone number?
USER : 555-12345
BOT : perfect, welcome back!
BOT : would you like Columbian or Kenyan?
USER : kenyan
BOT : perfect, the beans are on their way!
BOT : would you like Columbian or Kenyan?
"""



def chitchat_response(message):
  response, phrase = match_rule(eliza_rules, message)
  if response == "default":
    return None
  if '{0}' in response:
    # Replace the pronouns of phrase
    phrase = replace_pronouns(phrase)
    response = response.format(phrase)
  return response



def send_message(state, pending, message):
  print("USER : {}".format(message))
  response = chitchat_response(message)
  if response is not None:
    print("BOT : {}".format(response))
    return state, None
  new_state, response, pending_state = policy_rules[(state, interpret(message))]
  print("BOT : {}".format(response))
  if pending is not None:
    new_state, response, pending_state = policy_rules[pending]
    print("BOT : {}".format(response))
  if pending_state is not None:
    pending = (pending_state, interpret(message))
  return new_state, pending

def send_messages(messages):
  state = INIT
  pending = None
  for msg in messages:
    state, pending = send_message(state, pending, msg)

send_messages([
  "I'd like to order some coffee",
  "555-12345",
  "do you remember when I ordered 1000 kilos by accident?",
  "kenyan"
])


"""
USER : I'd like to order some coffee
BOT : you'll have to log in first, what's your phone number?
USER : 555-12345
BOT : perfect, welcome back!
BOT : would you like Columbian or Kenyan?
USER : do you remember when I ordered 1000 kilos by accident?
BOT : Yes .. and?
USER : kenyan
BOT : perfect, the beans are on their way!
"""


