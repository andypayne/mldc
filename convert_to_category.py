
categorize_label = lambda x: x.astype('category')

sample_df.label = sample_df[['label']].apply(categorize_label, axis=0)  # axis=0 instructs apply to apply the lambda to each column
sample_df.info()




