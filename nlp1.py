from sklearn.feature_extraction.text import CountVectorizer

TOKENS_BASIC = '\\S+(?=\\s+)'  # Whitespace, followed by non whitespace

df.Program_Description.fillna('', inplace=True)

vec_basic = CountVectorizer(token_pattern=TOKENS_BASIC)
vec_basic.fit(df.Program_Description)

msg = 'There are {} tokens in Program_Description if tokens are any non-whitespace.'
print(msg.format(len(vec_basic.get_feature_names())))


