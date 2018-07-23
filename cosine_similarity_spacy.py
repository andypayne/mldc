import spacy

nlp = spacy.load('en')

doc = nlp('cat')

doc.similarity(nlp('can'))
# => 0.30165...

doc.similarity(nlp('dog'))
# => 0.80168...

