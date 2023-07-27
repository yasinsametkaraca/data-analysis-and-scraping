import pandas as pd

df = pd.read_csv('imdb_top.csv')
df.drop(['Unnamed: 0'], axis=1, inplace=True)
print(df.columns)
print(df.head())  # First 5 rows
print(df.info())  # 250 entries, 15 columns, no null values
print(df.tail())  # Last 5 rows

print(df['Duration'].head())  # First 5 rows of Duration column

print(df[['Title', 'Rating count']].head())  # First 5 rows of Title and Rating count columns
print(df[5:][['Title', 'Rating count']])  # Title and Rating count columns from 5th row to end
print(df[df['Rating count'] > 1000000][['Title', 'Rating count']])  # Title and Rating count columns where Rating count > 1000000

df['Rating count'] = df['Rating count'].apply(lambda x: x / 1000)  # Divide Rating count column by 1000
print(df['Rating count'].head())  # First 5 rows of Rating count column

df['Rating count'] = df['Rating count'].apply(lambda x: x * 1000)  # Multiply Rating count column by 1000
print(df['Rating count'].head())  # First 5 rows of Rating count column

print(df[df['Genre'] == 'Drama'][['Genre', 'Rating count']])  # Title and Rating count columns where Genre is Drama

print(df[df['Genre'].isin(['Drama', 'Action'])][['Genre', 'Rating count']])  # Title and Rating count columns where Genre is Drama or Action

print(df[df['Genre'].str.contains('Drama')][['Genre', 'Rating count']])  # Title and Rating count columns where Genre contains Drama

print(df[df['Genre'].str.startswith('Drama')][['Genre', 'Rating count']])  # Title and Rating count columns where Genre starts with Drama

print(df[df['Genre'].str.endswith('Drama')][['Genre', 'Rating count']])  # Title and Rating count columns where Genre ends with Drama

print("--------------------")

print(df[(df['Genre'].str.len() > 10) & (df['Title'].str.startswith('The W'))][['Title', 'Genre', 'Rating count']])  # Title and Rating count columns where Genre length > 10 and Title starts with The W


