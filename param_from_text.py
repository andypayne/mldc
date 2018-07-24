
message = "a cheap hotel in the north"
data = interpreter.parse(message)
data
# => ...

params = {}
for ent in data["entities"]:
  params[ent["entity"]] = ent["value"]

params
# => {'location': 'north', 'price': 'low'}

query = "SELECT name FROM hotels"

filters = ["{}=?".format(k) for k in params.keys()]
filters
# => ['price=?', 'location=?']

conditions = " AND ".join(filters)
conditions
# => 'price=? AND location=?'

final_q = " WHERE ".join([query, conditions])


# Responses ordered by number of results
responses = [
  "I'm sorry, I couldn't find anything like that.",
  "What about {}?",
  "{} is one option, but there are others."
]

c.execute(final_q, ...)
results = c.fetchall()

len(results)
# => 4

index = min(len(results), len(responses) - 1)

responses[index]
# => "{} is one option, but there are others."



def find_hotels(params):
  query = 'SELECT * FROM hotels'
  if len(params) > 0:
    filters = ["{}=?".format(k) for k in params.keys()]
    query += " WHERE " + " and ".join(filters)
  # TODO: t should be under the if clause above
  #t = tuple([params[k] for k in params.keys()])
  t = tuple(params.values())
  conn = sqlite3.connect("hotels.db")
  c = conn.cursor()
  c.execute(query, t)
  return c.fetchall()

params = {"area": "south", "price": "lo"}
print(find_hotels(params))
# => [('Cozy Cottage', 'lo', 'south', 2)]


def respond(message):
  entities = interpreter.parse(message)["entities"]
  params = {}
  for ent in entities:
    params[ent["entity"]] = str(ent["value"])
  results = find_hotels(params)
  names = [r[0] for r in results]
  n = min(len(results),3)
  return responses[n].format(*names)


print(respond("I want an expensive hotel in the south of town"))
# => Grand Hotel is a great hotel!


