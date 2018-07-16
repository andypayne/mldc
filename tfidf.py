#w_i_j: TF-IDF weight for token i in document j
#w_i_j = tf_i * log(N/df_i)
#where:
#  tf_i:   Number of occurrences of token i in document j
#  N:      Total number of documents
#  df_i:   Number of documents that contain token i

from gensim.models.tfidfmodel import TfidfModel

tfidf = TfidfModel(corpus)

# TF-IDF scores of the second document in the corpus
tfidf[corpus[1]]


################################################################################
from gensim.models.tfidfmodel import TfidfModel

tfidf = TfidfModel(corpus)
# Calculate the tfidf weights of doc
tfidf_weights = tfidf[doc]
# Print the first five weights
print(tfidf_weights[:5])
# Sort the weights from highest to lowest
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)
# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary[term_id], weight)


