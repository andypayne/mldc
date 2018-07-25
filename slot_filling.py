
# params is now passed in, so that it can be updated with each new message as
# more info comes in.
def respond(message, params):
  # update params with entities in the message
  # run query
  # pick response
  return response, params

params = {}
response, params = respond(message, params)



def respond(message, params):
  entities = interpreter.parse(message)["entities"]
  for ent in entities:
    params[ent["entity"]] = str(ent["value"])
  results = find_hotels(params)
  names = [r[0] for r in results]
  n = min(len(results), 3)
  return responses[n].format(*names), params

params = {}

for message in ["I want an expensive hotel", "in the north of town"]:
  print("USER: {}".format(message))
  response, params = respond(message, params)
  print("BOT: {}".format(response))


