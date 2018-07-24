from rasa_nlu.converters import load_data
import json

training_data = load_data("./training_data.json")
print(json.dumps(data.training_examples[22], indent=2))
# => { "text": "i'm looking for a place in the north of town",
#      "intent": "restaurant_search",
#      "entities": { ... }
#    }


message = "I want to book a flight to London"
interpreter.parse(message)
# ...


# Creating a model
from rasa_nlu.config import RasaNULConfig
from rasa_nlu.model import Trainer

#config = RasaNULConfig(cmdline_args={"pipeline", "spacy_sklearn"})
config = RasaNULConfig(cmdline_args={"pipeline": "spacy_sklearn"})

trainer = Trainer(config)
interpreter = trainer.train(training_data)


# CRF = Conditional Random Field
# - Popular for named entity recognition
# - Can perform well even with a small amount of training data
spacy_sklearn_pipeline = [
  "nlp_spacy",
  "ner_crf",
  "ner_synonyms",
  "intent_featurizer_spacy",
  "intent_classifier_sklearn"
]

# These two are identical:
RasaNULConfig(cmdline_args={"pipeline": "spacy_sklearn"})
RasaNULConfig(cmdline_args={"pipeline": spacy_sklearn_pipeline})


# Include the intent_featurizer_ngrams component to help deal with typos, etc.
spacy_sklearn_pipeline = [
  "nlp_spacy",
  "intent_featurizer_spacy",
  "intent_featurizer_ngrams",
  "intent_classifier_sklearn"
]



from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

args = {"pipeline": "spacy_sklearn"}
config = RasaNLUConfig(cmdline_args=args)
trainer = Trainer(config)
training_data = load_data("./training_data.json")
interpreter = trainer.train(training_data)
print(interpreter.parse("I'm looking for a Mexican restaurant in the North of town"))



from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

pipeline = [
    "nlp_spacy",
    "tokenizer_spacy",
    "ner_crf"
]

config = RasaNLUConfig(cmdline_args={"pipeline": pipeline})
trainer = Trainer(config)
interpreter = trainer.train(training_data)

print(interpreter.parse("show me Chinese food in the centre of town"))
print(interpreter.parse("I want an Indian restaurant in the west"))
print(interpreter.parse("are there any good pizza places in the center?"))


