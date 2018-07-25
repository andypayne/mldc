
doc = nlp('not sushi, maybe pizza?')

indices = [1, 4]

ents, negated_ents = [], []

start = 0
for i in indices:
  phrase = "{}".format(doc[start:i])
  if "not" in phrase or "n't" in phrase:
    negated_ents.append(doc[i])
  else:
    ents.append(doc[i])
  start = i



def negated_ents(phrase):
  # Extract the entities using keyword matching
  ents = [e for e in ["south", "north"] if e in phrase]
  # Find the index of the final character of each entity
  ends = sorted([phrase.index(e) + len(e) for e in ents])
  chunks = []
  # Take slices of the sentence up to and including each entitiy
  start = 0
  for end in ends:
    chunks.append(phrase[start:end])
    start = end
  result = {}
  # Iterate over the chunks and look for entities
  for chunk in chunks:
    for ent in ents:
      if ent in chunk:
        # If the entity is preceeded by a negation, give it the key False
        if "not" in chunk or "n't" in chunk:
          result[ent] = False
        else:
          result[ent] = True
  return result  

# Check that the entities are correctly assigned as True or False
for test in tests:
  print(negated_ents(test[0]) == test[1])



def respond(message, params, neg_params):
  entities = interpreter.parse(message)["entities"]
  ent_vals = [e["value"] for e in entities]
  negated = negated_ents(message, ent_vals)
  for ent in entities:
    if ent["value"] in negated and negated[ent["value"]]:
      neg_params[ent["entity"]] = str(ent["value"])
    else:
      params[ent["entity"]] = str(ent["value"])
  results = find_hotels(params, neg_params)
  names = [r[0] for r in results]
  n = min(len(results),3)
  return responses[n].format(*names), params, neg_params

params = {}
neg_params = {}

for message in ["I want a cheap hotel", "but not in the north of town"]:
  print("USER: {}".format(message))
  response, params, neg_params = respond(message, params, neg_params)
  print("BOT: {}".format(response))


