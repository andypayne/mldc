from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

#print(df.head())

y = df.label
X_train, X_test, y_train, y_test = train_test_split(df["text"], y, test_size=0.33, random_state=53)

count_vectorizer = CountVectorizer(stop_words="english")
# Transform the training data using only the 'text' column values
count_train = count_vectorizer.fit_transform(X_train.values)
# Transform the test data using only the 'text' column values
count_test = count_vectorizer.transform(X_test.values)
# Print the first 10 features of the count_vectorizer
print(count_vectorizer.get_feature_names()[:10])


from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
tfidf_train = tfidf_vectorizer.fit_transform(X_train.values)
tfidf_test = tfidf_vectorizer.transform(X_test.values)

# Print the first 10 features
print(tfidf_vectorizer.get_feature_names()[:10])
# Print the first 5 vectors of the tfidf training data
print(tfidf_train.A[:5])


# Create the CountVectorizer DataFrame
count_df = pd.DataFrame(count_train.A, columns=count_vectorizer.get_feature_names())

# Create the TfidfVectorizer DataFrame
tfidf_df = pd.DataFrame(tfidf_train.A, columns=tfidf_vectorizer.get_feature_names())

print(count_df.head())
print(tfidf_df.head())

# Calculate the difference in columns: difference
difference = set(count_df) - set(tfidf_df)
print(difference)

# Check whether the DataFrames are equal
print(count_df.equals(tfidf_df))



