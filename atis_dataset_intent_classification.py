
sentences_train[:2]
# => ...

labels_train[:2]
# => [ "atis_flight", "atis_flight" ]

import numpy as np

X_train_shape = (len(sentences_train), nlp.vocab.vectors_length)

X_train = np.zeroes(X_train_shape)

for sentence in sentences_train:
  X_train[i,:] = nlp(sentence).vector

# Nearest neighbor classification in scikit-learn
# Could also use spacy similarity function
from sklearn.metrics.pairwise import cosine_similarity

test_message = "i would like to find a flight from charlotte to las vegas that makes a stop in st. louis"

test_x = nlp(test_message).vector

scores = [
  cosine_similarity(X[i,:], test_x)
  for i in range(len(sentences_train))
]

# The training label with the highest score is the best guess at the answer
labels_train[np.argmax(scores)]
# => 'atis_flight'


# More robust - SVM / SVC (Support Vector Classifier)
from sklearn.svm import SVC

clf = SVC()

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)


################################################################################

from sklearn.svm import SVC

clf = SVC(C=1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

n_correct = 0
for i in range(len(y_test)):
    if y_pred[i] == y_test[i]:
        n_correct += 1

print("Predicted {0} correctly out of {1} test examples".format(n_correct, len(y_test)))



