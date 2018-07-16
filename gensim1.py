from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize

my_documents = [
  'The movie was about a spaceship and aliens.',
  'I really liked the movie!',
  'Awesome action scenes, but boring characters.',
  'The movie was awful! I hate alien films.',
  'Space is cool! I liked the movie.',
  'More space films, please!'
]

# Remove punctuation & stop words

tokenized_docs = [word_tokenize(doc.lower()) for doc in my_documents]

dictionary = Dictionary(tokenized_docs)

dictionary.token2id
# => {'!': 11, ..., 'a': 2, 'about': 4, ... }

corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]

# gensim models can be easily saved, updated, and reused.

################################################################################

from gensim.corpora.dictionary import Dictionary

dictionary = Dictionary(articles)
computer_id = dictionary.token2id.get("computer")
print(dictionary.get(computer_id))

corpus = [dictionary.doc2bow(article) for article in articles]
print(corpus[4][:10])


################################################################################


doc = corpus[4]
bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)

# Print the top 5 words of the document alongside the count
for word_id, word_count in bow_doc[:5]:
    print(dictionary.get(word_id), word_count)

# Create the defaultdict: total_word_count
total_word_count = defaultdict(int)
for word_id, word_count in itertools.chain.from_iterable(corpus):
    total_word_count[word_id] += word_count

# Create a sorted list from the defaultdict: sorted_word_count
sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True)

# Print the top 5 words across all documents alongside the count
for word_id, word_count in sorted_word_count[:5]:
    print(dictionary.get(word_id), word_count)


