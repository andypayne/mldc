import spacy

# Named entity recognition can be used with intents to recognize entities that
# don't exist in the training data.
nlp = spacy.load('en')
doc = nlp("my friend Mary has worked at Google since 2009")

for ent in doc.ents:
  print(ent.text, ent.label_)
# => Mary PERSON
#    Google ORG
#    2009 DATE



# Roles - What about from/to with entities?
# Can use regexp:
pattern_1 = re.compile('.* from (.*) to (.*)')
pattern_2 = re.compile('.* to (.*) from (.*)')

# More robust - Dependency parsing - use a parse tree to assign roles

doc = nlp('a flight to Shanghai from Singapore')


