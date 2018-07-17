import spacy

nlp = spacy.load('en')
nlp.entity
# => spacy.pipeline.EntityRecognizer

doc = nlp("""Berlin is the capital of Germany; and the residence of Chancellor Angela Merkel.""")

doc.ents
# => (Berlin, Germany, Angela Merkel)

print(doc.ents[0], doc.ents[0].label_)
# => Berlin GPE


################################################################################

import spacy

nlp = spacy.load('en', tagger=False, parser=False, matcher=False)
doc = nlp(article)
for ent in doc.ents:
  print(ent.label_, ent.text)


