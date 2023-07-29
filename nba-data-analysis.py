import pandas as pd

df = pd.read_csv('nba.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)  # (458, 9)
print(df.columns)  # Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight', 'College', 'Salary'], dtype='object')
print(df.index)  # RangeIndex(start=0, stop=458, step=1)

print(df['Salary'].mean())  # 4842684.105381166
print(df['Salary'].max())  # 25000000.0
print(df[df['Salary'] == df['Salary'].max()]["Name"])  # Name: Kobe Bryant, Length: 1, dtype: object. Max salary is Kobe Bryant's salary.
print(df[df['Salary'] == df['Salary'].max()]["Name"].iloc[0])  # Kobe Bryant

print(df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name", "Team"]])  # 20-25 years old players and their teams.
#                 Name            Team
# 3        R.J. Hunter  Boston Celtics
# 6      Jordan Mickey  Boston Celtics
# 8       Terry Rozier  Boston Celtics
# 9       Marcus Smart  Boston Celtics
# 10   Jared Sullinger  Boston Celtics
# ..               ...             ...
# 446   Derrick Favors       Utah Jazz
# 447      Rudy Gobert       Utah Jazz
# 449      Rodney Hood       Utah Jazz
# 452       Trey Lyles       Utah Jazz
# 454        Raul Neto       Utah Jazz
#
# [152 rows x 2 columns]

print(df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name", "Team"]].groupby("Team").count())
#                         Name
# Team
# Atlanta Hawks              5
# Boston Celtics             6
# Brooklyn Nets              5
# Charlotte Hornets          6
# Chicago Bulls              4
# Cleveland Cavaliers        1

print(df[df["Name"] == "Kobe Bryant"]["Team"])  # 109    Los Angeles Lakers  # Kobe Bryant's team is Los Angeles Lakers.
# 109    Los Angeles Lakers
# Name: Team, dtype: object

print(len(df.groupby("Team")))  # 30. There are 30 teams in NBA.

print(df["Team"].value_counts())  # Number of players in each team.
# New Orleans Pelicans      19
# Memphis Grizzlies         18
# New York Knicks           16
#  ....

df.dropna(how="any", inplace=True)  # Drop rows with NaN values.
print(df[df["Name"].str.contains("Wr")])  # Players whose names contain "Wr".


def str_find(name):
    if "wr" in name.lower():
        return True
    return False


print(df[df["Name"].apply(str_find)])  # Players whose names contain "Wr".


