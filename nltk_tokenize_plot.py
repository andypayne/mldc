lines = holy_grail.split('\n')

# Replace all script lines for the speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]

tokenized_lines = [regexp_tokenize(s, "\w+") for s in lines]
line_num_words = [len(t_line) for t_line in tokenized_lines]

plt.hist(line_num_words)
plt.show()

