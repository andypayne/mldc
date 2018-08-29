import pandas as pd


dfs = []

for chunk in pd.read_csv('WDI.csv', chunksize=1000):
    is_urban = chunk['Indicator Name'] == 'Urban population (% of total)'
    is_AUS = chunk['Country Code'] == 'AUS'
    filtered = chunk.loc[is_urban & is_AUS]
    dfs.append(filtered)

print(len(dfs))
df = pd.concat(dfs)
print(len(df))

df.plot.line(x='Year', y='value')
plt.ylabel('% Urban population')
plt.show()


