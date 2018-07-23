import spacy

nlp = spacy.load('en')

nlp.vocab.vectors_length
# => 300

doc = nlp('hello can you help me?')

for token in doc:
  print("{} : {}".format(token, token.vector[:3]))
# => ...


