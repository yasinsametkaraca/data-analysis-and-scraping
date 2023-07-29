import pandas as pd

df = pd.read_csv('scatter.csv')

# print(df.head())
# print(df.columns)
# print(df.info())
# print(df.describe())

print(df['category_id'].value_counts())  # Get the number of each category
# Entertainment            1145
# Music                     545
# Howto & Style             418
# Comedy                    363
# People & Blogs            354
# Sports                    336
# News & Politics           334
# Science & Technology      283
# Film & Animation          235
# Education                 192
# Pets & Animals            108
# Gaming                     87
# Autos & Vehicles           51
# Travel & Events            48
# Nonprofits & Activism      11
# Shows                       4
# Name: category_id, dtype: int64

print(df.columns)
# Index(['Unnamed: 0', 'title', 'channel_title', 'category_id', 'views', 'likes', 'dislikes'], dtype='object')

print(df['likes'].mean())  # Get the average number of likes. 410.5
print(df['dislikes'].mean())  # Get the average number of dislikes. 31.0
print(df['views'].mean())  # Get the average number of views

print(df.head(10)['views'])  # Get the first 10 rows of views
print(df['views'].max())  # Get the maximum number of views. 225211923
print(df[df['views'].max() == df['views']])  # Get the row of the maximum number of views.
print(df[df['views'] == df['views'].max()]['title'])  # Get the title of the maximum number of views.
# 4163    Childish Gambino - This Is America (Official V...
# Name: title, dtype: object
print(df[df['views'] == df['views'].max()]['title'].iloc[
          0])  # Get the title of the maximum number of views. Directly name of the video.
# Childish Gambino - This Is America (Official Video)

print(df.sort_values('views', ascending=False).head(10)[
          ['title', 'views']])  # Get the first 10 rows of the sorted views. Get the top 10 videos with the most views.

print(df.groupby('category_id').mean())  # Get the average number of likes, dislikes and views of each category.
#                         Unnamed: 0         views          likes      dislikes
# category_id
# Autos & Vehicles       1490.803922  1.719166e+06    8266.509804    632.745098
# Comedy                 2351.126722  1.603124e+06   58862.597796   2273.696970
# Education              2197.984375  6.646118e+05   22549.458333    763.322917
# Entertainment          2379.117031  1.832750e+06   41166.672489   3779.758952
# Film & Animation       2220.068085  2.937875e+06   61956.072340   2480.770213
# Gaming                 2835.643678  2.642444e+06   76980.149425   7081.839080
# Howto & Style          2304.626794  9.495817e+05   37686.607656   1167.818182
# Music                  2415.091743  7.576131e+06  223962.084404   8181.946789
# News & Politics        1835.464072  5.412179e+05    6585.715569   1433.937126
# Nonprofits & Activism  1533.727273  2.819110e+06  216887.818182  51198.636364
# People & Blogs         2223.022599  1.632233e+06   54022.632768   2732.525424
# Pets & Animals         1802.388889  7.743719e+05   18499.120370    510.111111
# Science & Technology   2091.378092  1.195014e+06   27516.438163   1397.681979
# Shows                  2265.750000  7.624000e+05   15435.250000    362.750000
# Sports                 2268.366071  1.703135e+06   34543.642857   2211.226190
# Travel & Events        1826.145833  1.078142e+06   10799.104167    529.583333

print(df.groupby('category_id').mean()['views'])  # Get the average number of views of each category.

print(df['category_id'].value_counts())  # Get the number of each category

df['title_len'] = df['title'].apply(len)  # Get the length of each title. We add a new column to the dataframe.
print(df.head())

print("---------Get the rate of likes and dislikes. likes / (likes + dislikes) = rate of likes and dislikes.-----------")


def likes_dislikes_rate(dataset):
    likes_list = list(df['likes'])  # Get the list of likes. Convert the dataframe to a list.
    dislikes_list = list(df['dislikes'])  # Get the list of dislikes. Convert the dataframe to a list.

    tuple_list = list(zip(likes_list,
                          dislikes_list))  # Combine the two lists into a tuple list. [(like, dislike), (like, dislike), ...]
    print(tuple_list)

    rate_list = []
    for like, dislike in tuple_list:  # (like, dislike) is a tuple
        if(like + dislike) == 0:
            rate_list.append(0)
        else:
            rate_list.append(like / (like + dislike))
    print(rate_list)  # Get the rate of likes and dislikes. [0.985, 0.988, 0.986, ...]
    return rate_list


df['like_dislike_rate'] = likes_dislikes_rate(df)  # Add a new column to the dataframe. The new column is the rate of likes and dislikes.
print(df.sort_values('like_dislike_rate', ascending=False)[['title', 'like_dislike_rate']].head(100))
