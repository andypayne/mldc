import spacy

nlp = spacy.load('en')

n_sentences = len(sentences)

# dimensionality of nlp
embedding_dim = nlp.vocab.vectors_length

# Initialize the array with zeros
X = np.zeros((n_sentences, embedding_dim))

for idx, sentence in enumerate(sentences):
    doc = nlp(sentence)
    X[idx, :] = doc.vector

