from sklearn.preprocessing import PolynomialFeatures

interaction = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)

interaction.fit_transform(x)


# SparseInteractions is a replacement for PolynomialFeatures that supports
# sparse matrices, to minimize memory usage as the number of interaction
# terms grows exponentially
# Available at: https://github.com/drivendataorg/box-plots-sklearn/blob/master/src/features/SparseInteractions.py
SparseInteractions(degree=2).fit_transform(x).toarray()



