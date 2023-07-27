import pandas as pd  # Pandas is a data analysis library. It is used to import data from csv file. It is used to create dataframes. It is used to create series. It is used to create dataframes from dictionaries.
import numpy as np
from numpy.random import randn  # Numpy is a library for scientific computing. It is used to create arrays. It is used to create random numbers.

pandas_series = pd.Series([300, 200, 100])  # Create a series from a list. The list contains 3 elements. Indexes are automatically created. Indexes are 0, 1, 2. Values are 300, 200, 100.
print(type(pandas_series))  # Print the type of the series. It is pandas.core.series.Series.
print(pandas_series)  # Print the series.

pandas_series = pd.Series([300, 200, 100], index=['a', 'b', 'c'])  # Create a series from a list. The list contains 3 elements. Indexes are manually created. Indexes are a, b, c. Values are 300, 200, 100.
print(pandas_series)  # Print the series. Type of the series is int64.

pandas_series = pd.Series({'a': 300, 'b': 200, 'c': 100})  # Create a series from a dictionary. The dictionary contains 3 elements. Indexes are automatically created. Indexes are a, b, c. Values are 300, 200, 100.
print(pandas_series)  # Print the series. Type of the series is int64.

pandas_series = pd.Series([1, 'a', 3.14])
print(type(pandas_series))  # Type of the series is object. Pandas convert all values to object type. Here, 1 is converted to '1', 3.14 is converted to '3.14'.
print(pandas_series)  # Create a series from a list. The list contains 3 elements. Indexes are automatically created. Indexes are 0, 1, 2. Values are 1, 'a', 3.14. The type of the series is object.

random_numbers = np.random.randint(0, 100, 20)  # Create a numpy array. The array contains 20 elements. Elements are random numbers between 0 and 100.
pandas_series = pd.Series(random_numbers)  # Create a series from a numpy array. The array contains 20 elements. Indexes are automatically created. Indexes are 0, 1, 2, ..., 19. Values are random numbers between 0 and 100.
print(pandas_series)  # Print the series. Type of the series is int64.

pandas_series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])  # Create a series from a list. The list contains 5 elements. Indexes are manually created. Indexes are a, b, c, d, e. Values are 1, 2, 3, 4, 5.
print(pandas_series[0])  # Print the first element of the series. The first element is 1.
print(pandas_series['a'])  # Print the element of the series with index 'a'. The element is 1.
print(pandas_series[-1])  # Print the last element of the series. The last element is 5.
print(pandas_series[:2])  # Print the first 2 elements of the series. The first 2 elements are 1, 2.
print(pandas_series['a':'c'])  # Print the elements of the series with indexes 'a', 'b', 'c'. The elements are 1, 2, 3.
print(pandas_series[[0, 2, 4]])  # Print the elements of the series with indexes 0, 2, 4. The elements are 1, 3, 5.
print(pandas_series[['a', 'c', 'e']])  # Print the elements of the series with indexes 'a', 'c', 'e'. The elements are 1, 3, 5.
print(pandas_series[pandas_series > 3])  # Print the elements of the series that are greater than 3. The elements are 4, 5.

print(pandas_series.ndim)  # Print the number of dimensions of the series. The number of dimensions is 1. The series is 1-dimensional. Indexes is not included in the dimensions.
print(pandas_series.shape)  # Print the shape of the series. The shape is (5,). The series has 5 elements. The series is 1-dimensional. Indexes is not included in the dimensions.
print(pandas_series.sum())  # Print the sum of the elements of the series. The sum is 15.
print(pandas_series.mean())  # Print the mean of the elements of the series. The mean is 3.
print(pandas_series.std())  # Print the standard deviation of the elements of the series. The standard deviation is 1.5811388300841898.
print(pandas_series.min())  # Print the minimum of the elements of the series. The minimum is 1.
print(pandas_series.max())  # Print the maximum of the elements of the series. The maximum is 5.

print(pandas_series > 3)  # Print the elements of the series that are greater than 3. The elements are False, False, False, True, True. The type of the elements is bool.
print(pandas_series[pandas_series > 3])  # Print the elements of the series that are greater than 3. The elements are 4, 5. The type of the elements is int64.

print("----------------------------------------------------------------------------------------------------------------------")

# data frame is a 2-dimensional data structure. It is used to store data in rows and columns. It is used to import data from csv file. It is used to create dataframes from dictionaries. It is used to create dataframes from lists. It is used to create dataframes from numpy arrays.
# Series is a 1-dimensional data structure.

series1 = pd.Series([3, 2, 0, 1])  # Create a series from a list. The list contains 4 elements. Indexes are automatically created. Indexes are 0, 1, 2, 3. Values are 3, 2, 0, 1.
series2 = pd.Series([0, 3, 7, 2])  # Create a series from a list. The list contains 4 elements. Indexes are automatically created. Indexes are 0, 1, 2, 3. Values are 0, 3, 7, 2.

data = dict(bananas=series1, apples=series2)  # Create a dictionary. The dictionary contains 2 elements. Keys are bananas, apples. Values are series1, series2.
df = pd.DataFrame(data)  # Create a dataframe from a dictionary. The dictionary contains 2 elements. Keys are bananas, apples. Values are series1, series2.
print(df)  # Print the dataframe. The dataframe contains 4 rows and 2 columns. The dataframe is 2-dimensional. The dataframe has 4 indexes. Indexes are 0, 1, 2, 3. The dataframe has 2 columns. Columns are bananas, apples. The type of the dataframe is int64.
#    bananas  apples
# 0        3       0
# 1        2       3
# 2        0       7
# 3        1       2

df = pd.DataFrame()
print(df)  # Print the dataframe. The dataframe is empty. The dataframe is 2-dimensional. The dataframe has 0 rows and 0 columns. The dataframe has 0 indexes. The dataframe has 0 columns. The type of the dataframe is object.

data = [['Sarah', 90], ['John', 80], ['Mike', 70], ['Kate', 60]]  # Create a list. The list contains 4 elements. Values are ['Sarah', 90], ['John', 80], ['Mike', 70], ['Kate', 60].
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'], columns=['Name', 'Score'], dtype=float)  # Create a dataframe from a list. The list contains 4 elements. Values are ['Sarah', 90], ['John', 80], ['Mike', 70], ['Kate', 60]. Columns are manually created. Columns are Name, Score. Indexes are manually created. Indexes are a, b, c, d.
print(df)  # Print the dataframe. The dataframe contains 4 rows and 2 columns. The dataframe is 2-dimensional. The dataframe has 4 indexes. The dataframe has 2 columns. Columns are Name, Score. The type of the dataframe is object.
#     Name  Score
# a  Sarah   90.0
# b   John   80.0
# c   Mike   70.0
# d   Kate   60.0

dict1 = {'Name': ['Sarah', 'John', 'Mike', 'Kate'], 'Score': [90, 80, 70, 60]}  # Create a dictionary. The dictionary contains 2 elements. Keys are Name, Score. Values are ['Sarah', 'John', 'Mike', 'Kate'], [90, 80, 70, 60].
df = pd.DataFrame(dict1, index=['a', 'b', 'c', 'd'])  # Create a dataframe from a dictionary. The dictionary contains 2 elements. Keys are Name, Score. Values are ['Sarah', 'John', 'Mike', 'Kate'], [90, 80, 70, 60]. Indexes are manually created. Indexes are a, b, c, d.
print(df)  # Print the dataframe. The dataframe contains 4 rows and 2 columns. The dataframe is 2-dimensional. The dataframe has 4 indexes. The dataframe has 2 columns. Columns are Name, Score. The type of the dataframe is object.
#   Name  Score
# a  Sarah     90
# b   John     80
# c   Mike     70
# d   Kate     60
print(df['Name'])  # Print the column Name of the dataframe. The column Name contains 4 elements. The elements are Sarah, John, Mike, Kate. The type of the elements is object.
# a    Sarah
# b     John
# c     Mike
# d     Kate
# Name: Name, dtype: object

dict_list = [
    {'Name': 'Sarah', 'Score': 90},
    {'Name': 'John', 'Score': 80},
    {'Name': 'Mike', 'Score': 70},
    {'Name': 'Kate', 'Score': 60}
]
df = pd.DataFrame(dict_list, index=['a', 'b', 'c', 'd'])  # Create a dataframe from a list of dictionaries. The list contains 4 elements. Values are {'Name': 'Sarah', 'Score': 90}, {'Name': 'John', 'Score': 80}, {'Name': 'Mike', 'Score': 70}, {'Name': 'Kate', 'Score': 60}. Indexes are manually created. Indexes are a, b, c, d.
print(df)  # Print the dataframe. The dataframe contains 4 rows and 2 columns. The dataframe is 2-dimensional. The dataframe has 4 indexes. The dataframe has 2 columns. Columns are Name, Score. The type of the dataframe is object.
#     Name  Score
# a  Sarah     90
# b   John     80
# c   Mike     70
# d   Kate     60

print("----------------------------------------------------------------------------------------------------------------------")

df = pd.read_csv('survey.csv')  # Read a csv file. To read json file, use pd.read_json(). To read excel file, use pd.read_excel(). To read sql file, use pd.read_sql(). To read html file, use pd.read_html(). To read clipboard, use pd.read_clipboard(). To read python pickle object, use pd.read_pickle().
print(df)

print("----------------------------------------------------------------------------------------------------------------------")


df = pd.DataFrame(randn(3, 3), index=['a', 'b', 'c'], columns=['x', 'y', 'z'])  # Create a dataframe from a numpy array. The numpy array contains 3 rows and 3 columns. The numpy array is 2-dimensional. The numpy array has 3 indexes. Indexes are a, b, c. The numpy array has 3 columns. Columns are x, y, z.
print(df)
#           x         y         z
# a  0.250034  0.370692 -0.947904
# b  1.736494 -0.571718 -0.594398
# c  1.189452  1.430620 -0.131545
print(df['x'])  # Print the column x of the dataframe. The column x contains 3 elements. The elements are 0.250034, 1.736494, 1.189452. The type of the elements is float64.
# a    0.250034
# b    1.736494
# c    1.189452
# Name: x, dtype: float64
print(df[['x', 'y']])  # Print the columns x, y of the dataframe. The columns x, y contain 3 elements. The elements are 0.250034, 1.736494, 1.189452, 0.370692, -0.571718, 1.430620. The type of the elements is float64.
#           x         y
# a  0.250034  0.370692
# b  1.736494 -0.571718
# c  1.189452  1.430620

#  While using the loc command, we specify the row or column name, while in the iloc command we specify the index number of the row or column.
print(df.loc['a'])  # Print the row a of the dataframe. The row a contains 3 elements. The elements are 0.250034, 0.370692, -0.947904. The type of the elements is float64. Loc is used to access a group of rows and columns by label(s) or a boolean array.
# x    0.250034
# y    0.370692
# z   -0.947904
print(df.loc[['a', 'b'], 'x'])  # Print the rows a, b of the column x of the dataframe. The rows a, b of the column x contain 2 elements. The elements are 0.250034, 1.736494. The type of the elements is float64.
# a    0.250034
# b    1.736494
print(df.loc[:, 'x'])  # loc["row", "column"]  # loc["row"]  # loc[:, "column"]
#           x
# a  0.250034
# b  1.736494
# c  1.189452
print(df.loc[:, 'x': 'z'])  # Print the columns x, y, z of the dataframe. The columns x, y, z contain 3 elements. The elements are 0.250034, 1.736494, 1.189452, 0.370692, -0.571718, 1.430620, -0.947904, -0.594398, -0.131545. The type of the elements is float64.
#           x         y         z
# a  0.250034  0.370692 -0.947904
# b  1.736494 -0.571718 -0.594398
# c  1.189452  1.430620 -0.131545
print(df.loc[['a', 'b'], ['x', 'y']])  # Print the rows a, b of the columns x, y of the dataframe. The rows a, b of the columns x, y contain 4 elements. The elements are 0.250034, 1.736494, 0.370692, -0.571718. The type of the elements is float64.
#           x         y
# a  0.250034  0.370692
# b  1.736494 -0.571718
print(df.loc['a':'c', :'y'])  # Print the rows a, b, c of the columns x, y of the dataframe. The rows a, b, c of the columns x, y contain 6 elements. The elements are 0.250034, 1.736494, 1.189452, 0.370692, -0.571718, 1.430620. The type of the elements is float64.
#           x         y
# a  0.250034  0.370692
# b  1.736494 -0.571718
# c  1.189452  1.430620

print(df.iloc[0])  # Print the row 0 of the dataframe. The row 0 contains 3 elements. The elements are 0.250034, 0.370692, -0.947904. The type of the elements is float64. Iloc is used to access a group of rows and columns by integer position(s) or a boolean array.
# x    0.250034
# y    0.370692
# z   -0.947904
print(df.iloc[[0, 1], 0])  # Print the rows 0, 1 of the column 0 of the dataframe. The rows 0, 1 of the column 0 contain 2 elements. The elements are 0.250034, 1.736494. The type of the elements is float64.
# a    0.250034
# b    1.736494
print(df.iloc[:, 0])  # iloc["row", "column"]  # iloc["row"]  # iloc[:, "column"]
# a    0.250034
# b    1.736494
# c    1.189452
print(df.iloc[:, 0: 3])  # Print the columns 0, 1, 2 of the dataframe. The columns 0, 1, 2 contain 3 elements. The elements are 0.250034, 1.736494, 1.189452, 0.370692, -0.571718, 1.430620, -0.947904, -0.594398, -0.131545. The type of the elements is float64.
#           x         y         z
# a  0.250034  0.370692 -0.947904
# b  1.736494 -0.571718 -0.594398
# c  1.189452  1.430620 -0.131545

print(df.loc['a', 'x'])  # Print the element of the row a and the column x of the dataframe. The element is 0.250034. The type of the element is float64.
# 0.250034

print("--------------------------------------------------------------------------------------------------------")

df["column4"] = pd.Series(randn(3), ["a", "b", "c"])  # Add a new column to the dataframe. The new column is column4. The new column contains 3 elements. The elements are 0.132003, 0.243905, 0.266883. The type of the elements is float64.
print(df)
#           x         y         z   column4
# a  0.250034  0.370692 -0.947904  0.132003
# b  1.736494 -0.571718 -0.594398  0.243905
# c  1.189452  1.430620 -0.131545  0.266883
df["column5"] = df["x"] + df["y"]  #  Add a new column to the dataframe. The new column is column5. The new column contains 3 elements. The elements are 0.620726, 1.164776, 2.620072. The type of the elements is float64.
print(df)

result = df.drop("column5", axis=1)  # Delete the column5 from the dataframe. The column5 contains 3 elements. The elements are 0.620726, 1.164776, 2.620072. The type of the elements is float64. Axis 1 means column. Axis 0 means row.
print(result)  # The column5 is deleted from the dataframe. Original dataframe is not changed.
#           x         y         z   column4
# a  0.250034  0.370692 -0.947904  0.132003
# b  1.736494 -0.571718 -0.594398  0.243905
# c  1.189452  1.430620 -0.131545  0.266883
print(df)  # The column5 is not deleted from the dataframe. Original dataframe is not changed.
#           x         y         z   column4   column5
# a  0.250034  0.370692 -0.947904  0.132003  0.620726
# b  1.736494 -0.571718 -0.594398  0.243905  1.164776
# c  1.189452  1.430620 -0.131545  0.266883  2.620072
df.drop("column5", axis=1, inplace=True)  # Delete the column5 from the dataframe. Inplace=True means the original dataframe is changed. Inplace=False means the original dataframe is not changed. Result =
print(df)  # The column5 is deleted from the dataframe. Original dataframe is changed.
#           x         y         z   column4
# a  0.250034  0.370692 -0.947904  0.132003
# b  1.736494 -0.571718 -0.594398  0.243905
# c  1.189452  1.430620 -0.131545  0.266883

print("--------------------------------------------------------------------------------------------------------")

data = np.random.randint(10, 100, 75).reshape(15, 5)  # Create a 15x5 array. The array contains 75 elements. The elements are 10, 11, 12, ..., 98, 99. The type of the elements is int64.
print(data)
df = pd.DataFrame(data, columns=["column1", "column2", "column3", "column4", "column5"])  # Create a dataframe. The dataframe contains 15 rows and 5 columns. The dataframe contains 75 elements. The elements are 10, 11, 12, ..., 98, 99. The type of the elements is int64.
print(df)
print(df.columns)  # Get the column names of the dataframe. The column names are column1, column2, column3, column4, column5. The type of the column names is Index. # Index(['column1', 'column2', 'column3', 'column4', 'column5'], dtype='object')
print(df.head())  # Get the first 5 rows of the dataframe. The first 5 rows contain 5 elements.
#    column1  column2  column3  column4  column5
# 0       64       16       11       85       53
# 1       49       28       17       73       32
# 2       90       39       87       53       34
# 3       97       46       99       27       48
# 4       99       13       84       49       30
print(df.head(3))  # Get the first 3 rows of the dataframe. The first 3 rows contain 3 elements.
print(df.tail())  # Get the last 5 rows of the dataframe. The last 5 rows contain 5 elements.
print(df.tail(3))  # Get the last 3 rows of the dataframe. The last 3 rows contain 3 elements.
print(df["column1"].head())  # Get the first 5 elements of the column1 of the dataframe. The column1 contains 15 elements.
# 0    94
# 1    36
# 2    72
# 3    57
# 4    19
print(df[["column1", "column2"]].head())  # Get the first 5 elements of the column1 and column2 of the dataframe. The column1 and column2 contain 15 elements.
print(df[0:2])  # Get the first 2 rows of the dataframe. The first 2 rows contain 5 elements.
print(df[5:15][["column1", "column2"]].head())  # Get the first 5 elements of the column1 and column2 of the dataframe. The column1 and column2 contain 10 elements.
# column1  column2
# 5       59       92
# 6       89       13
# 7       99       64
# 8       95       44
# 9       36       92
print(df > 50)  # Get the boolean values of the dataframe. The dataframe contains 15 rows and 5 columns. The dataframe contains 75 elements. The elements are True or False. The type of the elements is bool.
#    column1  column2  column3  column4  column5
# 0     True    False    False     True     True
# 1    False    False    False     True    False
# 2     True    False     True     True    False
# 3     ....................
print(df[df > 50])  # Get the elements of the dataframe. The dataframe contains 15 rows and 5 columns. The dataframe contains 75 elements. The elements are 10, 11, 12, ..., 98, 99. The type of the elements is int64.
#    column1  column2  column3  column4  column5
# 0     64.0      NaN      NaN     85.0     53.0
# 1      NaN      NaN      NaN     73.0      NaN
# 2     90.0      NaN     87.0     53.0      NaN
# 3     97.0      NaN     99.0      NaN      NaN
# 4     .........
print(df[df["column1"] > 50])   # Returns rows with records greater than 50 in column1.
#    column1  column2  column3  column4  column5
# 0       64       16       11       85       53
# 2       90       39       87       53       34
# 3       97       46       99       27       4
# 5       59       92       10       11       98
print(df[df["column1"] > 50]["column1"])  # Returns column1 with records greater than 50 in column1.
# 0    64
# 2    90
# 3    97
# 5    59
# Name: column1, dtype: int64
print(df[(df["column1"] > 50) & (df["column1"] < 70)])  # Returns rows with records greater than 50 and less than 70 in column1.
#    column1  column2  column3  column4  column5
# 0       64       16       11       85       53
# 5       59       92       10       11       98
print(df[(df["column1"] > 50) & (df["column1"] < 70)][["column1", "column2"]])  # Returns column1 and column2 with records greater than 50 and less than 70 in column1.
#    column1  column2
# 0       64       16
# 5       59       92
print(df.query("column1 > 50 & column1 < 70"))  # Returns rows with records greater than 50 and less than 70 in column1.
#    column1  column2  column3  column4  column5
# 0       64       16       11       85       53
# 5       59       92       10       11       98
print(df.query("column1 > 50 & column2 < 70")[["column1", "column2"]])  # Returns column1 and column2 with records greater than 50 and less than 70 in column1.
#    column1  column2
# 0       64       16
# 5       59       92
print(df.query("column1 > 50 & column1 < 70").query("column2 > 50 & column2 < 70"))  # Returns rows with records greater than 50 and less than 70 in column1 and column2.
#    column1  column2  column3  column4  column5
# 5       59       92       10       11       98




