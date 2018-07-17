from polyglot.text import Text

text = """El presidente de la Generalitat de Cataluna, ..."""
ptext = Text(text)
ptext.entities
# => [I-ORG(['Generalitat', 'de']),
# ...


################################################################################

# Create the list of tuples: entities
entities = [(ent.tag, ' '.join(ent)) for ent in txt.entities]

# Print the entities
for ent in entities:
    print(ent)


################################################################################

count = 0

for ent in txt.entities:
    if 'Márquez' in ent or 'Gabo' in ent:
        count += 1

print(count)
# Calculate the percentage of entities that refer to "Gabo"
percentage = count * 1.0 / len(txt.entities)
print(percentage)

