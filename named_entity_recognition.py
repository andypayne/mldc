import nltk

sentence = 'In New York, I like to ride the Metro to visit MOMA and some restaurants rated well by Ruth Reichl.'

tokenized_sent = nltk.word_tokenize(sentence)
tagged_sent = nltk.pos_tag(tokenized_sent)
tagged_sent[:3]
# => [('In', 'IN'), ('New', 'NNP'), ('York', 'NNP')]

print(nltk.ne_chunk(tagged_sent))
# => Tree with named entities

################################################################################

# Tokenize the article into sentences
sentences = nltk.sent_tokenize(article)

# Tokenize each sentence into words
token_sentences = [nltk.word_tokenize(sent) for sent in sentences]

# Tag each tokenized sentence into parts of speech
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences] 

# Create the named entity chunks
chunked_sentences = nltk.ne_chunk_sents(pos_sentences, binary=True)

# Test for stems of the tree with 'NE' tags
for sent in chunked_sentences:
	for chunk in sent:
		if hasattr(chunk, "label") and chunk.label() == "NE":
			print(chunk)

################################################################################

ner_categories = defaultdict(int)

for sent in chunked_sentences:
	for chunk in sent:
		if hasattr(chunk, 'label'):
			ner_categories[chunk.label()] += 1
            
labels = list(ner_categories.keys())
values = [ner_categories.get(l) for l in labels]

plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.show()

