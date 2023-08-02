import \
    pandas as pd  # Pandas is a data analysis library. It is used to import data from csv file. It is used to create dataframes. It is used to create series. It is used to create dataframes from dictionaries.
import numpy as np
from numpy.random import \
    randn  # Numpy is a library for scientific computing. It is used to create arrays. It is used to create random numbers.

pandas_series = pd.Series([300, 200,
                           100])  # Create a series from a list. The list contains 3 elements. Indexes are automatically created. Indexes are 0, 1, 2. Values are 300, 200, 100.
print(type(pandas_series))  # Print the type of the series. It is pandas.core.series.Series.
print(pandas_series)  # Print the series.

pandas_series = pd.Series([300, 200, 100], index=['a', 'b',
                                                  'c'])  # Create a series from a list. The list contains 3 elements. Indexes are manually created. Indexes are a, b, c. Values are 300, 200, 100.
print(pandas_series)  # Print the series. Type of the series is int64.

pandas_series = pd.Series({'a': 300, 'b': 200,
                           'c': 100})  # Create a series from a dictionary. The dictionary contains 3 elements. Indexes are automatically created. Indexes are a, b, c. Values are 300, 200, 100.
print(pandas_series)  # Print the series. Type of the series is int64.

pandas_series = pd.Series([1, 'a', 3.14])
print(type(
    pandas_series))  # Type of the series is object. Pandas convert all values to object type. Here, 1 is converted to '1', 3.14 is converted to '3.14'.
print(
    pandas_series)  # Create a series from a list. The list contains 3 elements. Indexes are automatically created. Indexes are 0, 1, 2. Values are 1, 'a', 3.14. The type of the series is object.

random_numbers = np.random.randint(0, 100,
                                   20)  # Create a numpy array. The array contains 20 elements. Elements are random numbers between 0 and 100.
pandas_series = pd.Series(
    random_numbers)  # Create a series from a numpy array. The array contains 20 elements. Indexes are automatically created. Indexes are 0, 1, 2, ..., 19. Values are random numbers between 0 and 100.
print(pandas_series)  # Print the series. Type of the series is int64.

pandas_series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd',
                                                  'e'])  # Create a series from a list. The list contains 5 elements. Indexes are manually created. Indexes are a, b, c, d, e. Values are 1, 2, 3, 4, 5.
print(pandas_series[0])  # Print the first element of the series. The first element is 1.
print(pandas_series['a'])  # Print the element of the series with index 'a'. The element is 1.
print(pandas_series[-1])  # Print the last element of the series. The last element is 5.
print(pandas_series[:2])  # Print the first 2 elements of the series. The first 2 elements are 1, 2.
print(pandas_series['a':'c'])  # Print the elements of the series with indexes 'a', 'b', 'c'. The elements are 1, 2, 3.
print(pandas_series[[0, 2, 4]])  # Print the elements of the series with indexes 0, 2, 4. The elements are 1, 3, 5.
print(pandas_series[
          ['a', 'c', 'e']])  # Print the elements of the series with indexes 'a', 'c', 'e'. The elements are 1, 3, 5.
print(pandas_series[
          pandas_series > 3])  # Print the elements of the series that are greater than 3. The elements are 4, 5.

print(
    pandas_series.ndim)  # Print the number of dimensions of the series. The number of dimensions is 1. The series is 1-dimensional. Indexes is not included in the dimensions.
print(
    pandas_series.shape)  # Print the shape of the series. The shape is (5,). The series has 5 elements. The series is 1-dimensional. Indexes is not included in the dimensions.
print(pandas_series.sum())  # Print the sum of the elements of the series. The sum is 15.
print(pandas_series.mean())  # Print the mean of the elements of the series. The mean is 3.
print(
    pandas_series.std())  # Print the standard deviation of the elements of the series. The standard deviation is 1.5811388300841898.
print(pandas_series.min())  # Print the minimum of the elements of the series. The minimum is 1.
print(pandas_series.max())  # Print the maximum of the elements of the series. The maximum is 5.

print(
    pandas_series > 3)  # Print the elements of the series that are greater than 3. The elements are False, False, False, True, True. The type of the elements is bool.
print(pandas_series[
          pandas_series > 3])  # Print the elements of the series that are greater than 3. The elements are 4, 5. The type of the elements is int64.

print(
    "----------------------------------------------------------------------------------------------------------------------")

# data frame is a 2-dimensional data structure. It is used to store data in rows and columns. It is used to import data from csv file. It is used to create dataframes from dictionaries. It is used to create dataframes from lists. It is used to create dataframes from numpy arrays.
# Series is a 1-dimensional data structure.

series1 = pd.Series([3, 2, 0,
                     1])  # Create a series from a list. The list contains 4 elements. Indexes are automatically created. Indexes are 0, 1, 2, 3. Values are 3, 2, 0, 1.
series2 = pd.Series([0, 3, 7,
                     2])  # Create a series from a list. The list contains 4 elements. Indexes are automatically created. Indexes are 0, 1, 2, 3. Values are 0, 3, 7, 2.

data = dict(bananas=series1,
            apples=series2)  # Create a dictionary. The dictionary contains 2 elements. Keys are bananas, apples. Values are series1, series2.
df = pd.DataFrame(
    data)  # Create a dataframe from a dictionary. The dictionary contains 2 elements. Keys are bananas, apples. Values are series1, series2.
print(
    df)  # Print the dataframe. The dataframe contains 4 rows and 2 columns. The dataframe is 2-dimensional. The dataframe has 4 indexes. Indexes are 0, 1, 2, 3. The dataframe has 2 columns. Columns are bananas, apples. The type of the dataframe is int64.
#    bananas  apples
# 0        3       0
# 1        2       3
# 2        0       7
# 3        1       2

df = pd.DataFrame()
print(
    df)  # Print the dataframe. The dataframe is empty. The dataframe is 2-dimensional. The dataframe has 0 rows and 0 columns. The dataframe has 0 indexes. The dataframe has 0 columns. The type of the dataframe is object.

data = [['Sarah', 90], ['John', 80], ['Mike', 70], ['Kate',
                                                    60]]  # Create a list. The list contains 4 elements. Values are ['Sarah', 90], ['John', 80], ['Mike', 70], ['Kate', 60].
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'], columns=['Name', 'Score'],
                  dtype=float)  # Create a dataframe from a list. The list contains 4 elements. Values are ['Sarah', 90], ['John', 80], ['Mike', 70], ['Kate', 60]. Columns are manually created. Columns are Name, Score. Indexes are manually created. Indexes are a, b, c, d.
print(
    df)  # Print the dataframe. The dataframe contains 4 rows and 2 columns. The dataframe is 2-dimensional. The dataframe has 4 indexes. The dataframe has 2 columns. Columns are Name, Score. The type of the dataframe is object.
#     Name  Score
# a  Sarah   90.0
# b   John   80.0
# c   Mike   70.0
# d   Kate   60.0

dict1 = {'Name': ['Sarah', 'John', 'Mike', 'Kate'], 'Score': [90, 80, 70,
                                                              60]}  # Create a dictionary. The dictionary contains 2 elements. Keys are Name, Score. Values are ['Sarah', 'John', 'Mike', 'Kate'], [90, 80, 70, 60].
df = pd.DataFrame(dict1, index=['a', 'b', 'c',
                                'd'])  # Create a dataframe from a dictionary. The dictionary contains 2 elements. Keys are Name, Score. Values are ['Sarah', 'John', 'Mike', 'Kate'], [90, 80, 70, 60]. Indexes are manually created. Indexes are a, b, c, d.
print(
    df)  # Print the dataframe. The dataframe contains 4 rows and 2 columns. The dataframe is 2-dimensional. The dataframe has 4 indexes. The dataframe has 2 columns. Columns are Name, Score. The type of the dataframe is object.
#   Name  Score
# a  Sarah     90
# b   John     80
# c   Mike     70
# d   Kate     60
print(df[
          'Name'])  # Print the column Name of the dataframe. The column Name contains 4 elements. The elements are Sarah, John, Mike, Kate. The type of the elements is object.
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
df = pd.DataFrame(dict_list, index=['a', 'b', 'c',
                                    'd'])  # Create a dataframe from a list of dictionaries. The list contains 4 elements. Values are {'Name': 'Sarah', 'Score': 90}, {'Name': 'John', 'Score': 80}, {'Name': 'Mike', 'Score': 70}, {'Name': 'Kate', 'Score': 60}. Indexes are manually created. Indexes are a, b, c, d.
print(
    df)  # Print the dataframe. The dataframe contains 4 rows and 2 columns. The dataframe is 2-dimensional. The dataframe has 4 indexes. The dataframe has 2 columns. Columns are Name, Score. The type of the dataframe is object.
#     Name  Score
# a  Sarah     90
# b   John     80
# c   Mike     70
# d   Kate     60

print(
    "----------------------------------------------------------------------------------------------------------------------")

df = pd.read_csv(
    'survey.csv')  # Read a csv file. To read json file, use pd.read_json(). To read excel file, use pd.read_excel(). To read sql file, use pd.read_sql(). To read html file, use pd.read_html(). To read clipboard, use pd.read_clipboard(). To read python pickle object, use pd.read_pickle().
print(df)

print(
    "----------------------------------------------------------------------------------------------------------------------")

df = pd.DataFrame(randn(3, 3), index=['a', 'b', 'c'], columns=['x', 'y',
                                                               'z'])  # Create a dataframe from a numpy array. The numpy array contains 3 rows and 3 columns. The numpy array is 2-dimensional. The numpy array has 3 indexes. Indexes are a, b, c. The numpy array has 3 columns. Columns are x, y, z.
print(df)
#           x         y         z
# a  0.250034  0.370692 -0.947904
# b  1.736494 -0.571718 -0.594398
# c  1.189452  1.430620 -0.131545
print(df[
          'x'])  # Print the column x of the dataframe. The column x contains 3 elements. The elements are 0.250034, 1.736494, 1.189452. The type of the elements is float64.
# a    0.250034
# b    1.736494
# c    1.189452
# Name: x, dtype: float64
print(df[['x',
          'y']])  # Print the columns x, y of the dataframe. The columns x, y contain 3 elements. The elements are 0.250034, 1.736494, 1.189452, 0.370692, -0.571718, 1.430620. The type of the elements is float64.
#           x         y
# a  0.250034  0.370692
# b  1.736494 -0.571718
# c  1.189452  1.430620

#  While using the loc command, we specify the row or column name, while in the iloc command we specify the index number of the row or column.
print(df.loc[
          'a'])  # Print the row a of the dataframe. The row a contains 3 elements. The elements are 0.250034, 0.370692, -0.947904. The type of the elements is float64. Loc is used to access a group of rows and columns by label(s) or a boolean array.
# x    0.250034
# y    0.370692
# z   -0.947904
print(df.loc[['a',
              'b'], 'x'])  # Print the rows a, b of the column x of the dataframe. The rows a, b of the column x contain 2 elements. The elements are 0.250034, 1.736494. The type of the elements is float64.
# a    0.250034
# b    1.736494
print(df.loc[:, 'x'])  # loc["row", "column"]  # loc["row"]  # loc[:, "column"]
#           x
# a  0.250034
# b  1.736494
# c  1.189452
print(df.loc[:,
      'x': 'z'])  # Print the columns x, y, z of the dataframe. The columns x, y, z contain 3 elements. The elements are 0.250034, 1.736494, 1.189452, 0.370692, -0.571718, 1.430620, -0.947904, -0.594398, -0.131545. The type of the elements is float64.
#           x         y         z
# a  0.250034  0.370692 -0.947904
# b  1.736494 -0.571718 -0.594398
# c  1.189452  1.430620 -0.131545
print(df.loc[['a', 'b'], ['x',
                          'y']])  # Print the rows a, b of the columns x, y of the dataframe. The rows a, b of the columns x, y contain 4 elements. The elements are 0.250034, 1.736494, 0.370692, -0.571718. The type of the elements is float64.
#           x         y
# a  0.250034  0.370692
# b  1.736494 -0.571718
print(df.loc['a':'c',
      :'y'])  # Print the rows a, b, c of the columns x, y of the dataframe. The rows a, b, c of the columns x, y contain 6 elements. The elements are 0.250034, 1.736494, 1.189452, 0.370692, -0.571718, 1.430620. The type of the elements is float64.
#           x         y
# a  0.250034  0.370692
# b  1.736494 -0.571718
# c  1.189452  1.430620

print(df.iloc[
          0])  # Print the row 0 of the dataframe. The row 0 contains 3 elements. The elements are 0.250034, 0.370692, -0.947904. The type of the elements is float64. Iloc is used to access a group of rows and columns by integer position(s) or a boolean array.
# x    0.250034
# y    0.370692
# z   -0.947904
print(df.iloc[[0,
               1], 0])  # Print the rows 0, 1 of the column 0 of the dataframe. The rows 0, 1 of the column 0 contain 2 elements. The elements are 0.250034, 1.736494. The type of the elements is float64.
# a    0.250034
# b    1.736494
print(df.iloc[:, 0])  # iloc["row", "column"]  # iloc["row"]  # iloc[:, "column"]
# a    0.250034
# b    1.736494
# c    1.189452
print(df.iloc[:,
      0: 3])  # Print the columns 0, 1, 2 of the dataframe. The columns 0, 1, 2 contain 3 elements. The elements are 0.250034, 1.736494, 1.189452, 0.370692, -0.571718, 1.430620, -0.947904, -0.594398, -0.131545. The type of the elements is float64.
#           x         y         z
# a  0.250034  0.370692 -0.947904
# b  1.736494 -0.571718 -0.594398
# c  1.189452  1.430620 -0.131545

print(df.loc[
          'a', 'x'])  # Print the element of the row a and the column x of the dataframe. The element is 0.250034. The type of the element is float64.
# 0.250034

print("--------------------------------------------------------------------------------------------------------")

df["column4"] = pd.Series(randn(3), ["a", "b",
                                     "c"])  # Add a new column to the dataframe. The new column is column4. The new column contains 3 elements. The elements are 0.132003, 0.243905, 0.266883. The type of the elements is float64.
print(df)
#           x         y         z   column4
# a  0.250034  0.370692 -0.947904  0.132003
# b  1.736494 -0.571718 -0.594398  0.243905
# c  1.189452  1.430620 -0.131545  0.266883
df["column5"] = df["x"] + df[
    "y"]  # Add a new column to the dataframe. The new column is column5. The new column contains 3 elements. The elements are 0.620726, 1.164776, 2.620072. The type of the elements is float64.
print(df)

result = df.drop("column5",
                 axis=1)  # Delete the column5 from the dataframe. The column5 contains 3 elements. The elements are 0.620726, 1.164776, 2.620072. The type of the elements is float64. Axis 1 means column. Axis 0 means row.
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
df.drop("column5", axis=1,
        inplace=True)  # Delete the column5 from the dataframe. Inplace=True means the original dataframe is changed. Inplace=False means the original dataframe is not changed. Result =
print(df)  # The column5 is deleted from the dataframe. Original dataframe is changed.
#           x         y         z   column4
# a  0.250034  0.370692 -0.947904  0.132003
# b  1.736494 -0.571718 -0.594398  0.243905
# c  1.189452  1.430620 -0.131545  0.266883

print("--------------------------------------------------------------------------------------------------------")

data = np.random.randint(10, 100, 75).reshape(15,
                                              5)  # Create a 15x5 array. The array contains 75 elements. The elements are 10, 11, 12, ..., 98, 99. The type of the elements is int64.
print(data)
df = pd.DataFrame(data, columns=["column1", "column2", "column3", "column4",
                                 "column5"])  # Create a dataframe. The dataframe contains 15 rows and 5 columns. The dataframe contains 75 elements. The elements are 10, 11, 12, ..., 98, 99. The type of the elements is int64.
print(df)
print(
    df.columns)  # Get the column names of the dataframe. The column names are column1, column2, column3, column4, column5. The type of the column names is Index. # Index(['column1', 'column2', 'column3', 'column4', 'column5'], dtype='object')
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
print(
    df["column1"].head())  # Get the first 5 elements of the column1 of the dataframe. The column1 contains 15 elements.
# 0    94
# 1    36
# 2    72
# 3    57
# 4    19
print(df[["column1",
          "column2"]].head())  # Get the first 5 elements of the column1 and column2 of the dataframe. The column1 and column2 contain 15 elements.
print(df[0:2])  # Get the first 2 rows of the dataframe. The first 2 rows contain 5 elements.
print(df[5:15][["column1",
                "column2"]].head())  # Get the first 5 elements of the column1 and column2 of the dataframe. The column1 and column2 contain 10 elements.
# column1  column2
# 5       59       92
# 6       89       13
# 7       99       64
# 8       95       44
# 9       36       92
print(
    df > 50)  # Get the boolean values of the dataframe. The dataframe contains 15 rows and 5 columns. The dataframe contains 75 elements. The elements are True or False. The type of the elements is bool.
#    column1  column2  column3  column4  column5
# 0     True    False    False     True     True
# 1    False    False    False     True    False
# 2     True    False     True     True    False
# 3     ....................
print(df[
          df > 50])  # Get the elements of the dataframe. The dataframe contains 15 rows and 5 columns. The dataframe contains 75 elements. The elements are 10, 11, 12, ..., 98, 99. The type of the elements is int64.
#    column1  column2  column3  column4  column5
# 0     64.0      NaN      NaN     85.0     53.0
# 1      NaN      NaN      NaN     73.0      NaN
# 2     90.0      NaN     87.0     53.0      NaN
# 3     97.0      NaN     99.0      NaN      NaN
# 4     .........
print(df[df["column1"] > 50])  # Returns rows with records greater than 50 in column1.
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
print(df[(df["column1"] > 50) & (
            df["column1"] < 70)])  # Returns rows with records greater than 50 and less than 70 in column1.
#    column1  column2  column3  column4  column5
# 0       64       16       11       85       53
# 5       59       92       10       11       98
print(df[(df["column1"] > 50) & (df["column1"] < 70)][["column1",
                                                       "column2"]])  # Returns column1 and column2 with records greater than 50 and less than 70 in column1.
#    column1  column2
# 0       64       16
# 5       59       92
print(df.query("column1 > 50 & column1 < 70"))  # Returns rows with records greater than 50 and less than 70 in column1.
#    column1  column2  column3  column4  column5
# 0       64       16       11       85       53
# 5       59       92       10       11       98
print(df.query("column1 > 50 & column2 < 70")[["column1",
                                               "column2"]])  # Returns column1 and column2 with records greater than 50 and less than 70 in column1.
#    column1  column2
# 0       64       16
# 5       59       92
print(df.query("column1 > 50 & column1 < 70").query(
    "column2 > 50 & column2 < 70"))  # Returns rows with records greater than 50 and less than 70 in column1 and column2.
#    column1  column2  column3  column4  column5
# 5       59       92       10       11       98

print(
    "--------------------------------------------------")  # groupby method: It is used to group the data according to the specified column. It is used with aggregate functions. It is used with aggregate functions such as sum, mean, max, min, count, etc.

person_dict = {
    "name": ["ali", "veli", "kenan", "hilal", "ayse", "evren"],
    "age": [15, 16, 17, 33, 45, 66],
    "salary": [100, 150, 240, 350, 110, 220],
    "city": ["ankara", "istanbul", "konya", "antalya", "kayseri", "adana"],
    "department": ["IT", "IT", "R&D", "Accounting", "HR", "IT"]
}

df = pd.DataFrame(person_dict)
print(df)
#     name  age  salary      city  department
# 0    ali   15     100    ankara          IT
# 1   veli   16     150  istanbul          IT
# 2  kenan   17     240     konya         R&D
# 3  hilal   33     350   antalya  Accounting
# 4   ayse   45     110   kayseri          HR
# 5  evren   66     220     adana          IT

print(df["department"].unique())  # Get the unique values of the department column.
print(df.groupby(
    "department"))  # Get the groupby object of the department column.  #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000018BA342EBC0>
print(df.groupby(
    "department").groups)  # Get the groups of the department column.  # {'Accounting': [3], 'HR': [4], 'IT': [0, 1, 5], 'R&D': [2]}. Give the index numbers of the rows.
print(df.groupby("department").get_group(
    "IT"))  # Get the rows of the department column.  # Get the rows of the IT department.
#     name  age  salary      city department
# 0    ali   15     100    ankara         IT
# 1   veli   16     150  istanbul         IT
# 5  evren   66     220     adana         IT

print(df.groupby("department").get_group("IT")["salary"])  # Get the salary column of the rows of the IT department.
# 0    100
# 1    150
# 5    220
# Name: salary, dtype: int64
print(df.groupby(["department",
                  "city"]).groups)  # Get the groups of the department and city columns.  # {('Accounting', 'antalya'): [3], ('HR', 'kayseri'): [4], ('IT', 'adana'): [5], ('IT', 'ankara'): [0], ('IT', 'istanbul'): [1], ('R&D', 'konya'): [2]}. Give the index numbers of the rows.

for name, group in df.groupby("department"):  # Get the name and group of the department column.
    print(name)
    print(group)
    print("*******************")
# Accounting
#     name  age  salary     city  department
# 3  hilal   33     350  antalya  Accounting
# *******************
# HR
#    name  age  salary     city department
# 4  ayse   45     110  kayseri         HR
# *******************
# IT
#     name  age  salary      city department
# 0    ali   15     100    ankara         IT
# 1   veli   16     150  istanbul         IT
# 5  evren   66     220     adana         IT
# *******************
# R&D
#     name  age  salary   city department
# 2  kenan   17     240  konya        R&D
# *******************

print(df.groupby(
    "department").sum())  # Get the sum of the department column. # Get the sum of the age and salary columns of the department column.
#             age  salary
# department
# Accounting   33     350  # 33 + 350 = 383
# HR           45     110  # 45 + 110 = 155
# IT           97     470  # 15 + 100 + 16 + 150 + 66 + 220 = 567
# R&D          17     240  # 17 + 240 = 257

print(df.groupby("city")[
          "age"].mean())  # Get the mean of the age column of the city column. For example mean of the age column of the ankara city.
# city
# adana       66
# ankara      15
# antalya     33
# istanbul    16
# kayseri     45
# konya       17
# Name: age, dtype: int64

print(df.groupby("department").agg({"salary": "mean",
                                    "age": "max"}))  # Get the mean of the salary column and max of the age column of the department column.
#                 salary  age
# department
# Accounting  350.000000   33
# HR          110.000000   45
# IT          156.666667   66
# R&D         240.000000   17

print(df.groupby("department")["salary"].max()["IT"])  # Get the max of the IT column of the department column. # 220
print(df.groupby("department")["salary"].agg(
    [np.sum, np.mean, np.max, np.min]))  # Get the sum, mean, max, min of the salary column of the department column.
#             sum    mean      amax   amin
# department
# Accounting  350  350.000000   350   350
# HR          110  110.000000   110   110
# IT          470  156.666667   220   100
# R&D         240  240.000000   240   240

print(df.groupby("department")["salary"].agg([np.sum, np.mean, np.max, np.min]).loc[
          "IT"])  # Get the sum, mean, max, min of the salary column of the IT department.
# sum     470.000000
# mean    156.666667
# amax    220.000000
# amin    100.000000
# Name: IT, dtype: float64

print("-----------------------------------------")

# Nan Values (Missing Values). When we have a missing value in a column, we can fill it with a value or delete it.
# We can fill the missing values with the mean, median, mode, etc. of the column.
# We can delete the missing values with the dropna() method.
# We can fill the missing values with the fillna() method.

data = np.random.randint(10, 100, 15).reshape(5, 3)
df = pd.DataFrame(data, index=["a", "c", "e", "f", "h"], columns=["column1", "column2", "column3"])
df = df.reindex(
    ["a", "b", "c", "d", "e", "f", "g", "h"])  # Add the missing rows.  # Add the missing rows with the NaN values.
print(df)
#    column1  column2  column3
# a     78.0     70.0     63.0
# b      NaN      NaN      NaN
# c     37.0     37.0     37.0
# d      NaN      NaN      NaN
# e     10.0     10.0     10.0
# f     78.0     78.0     78.0
# g      NaN      NaN      NaN
# h     63.0     63.0     63.0

print(df.drop("column1", axis=1))  # Delete the column1 column.

print(df.drop(["column1", "column2"], axis=1))  # Delete the column1 and column2 columns.
print(df.drop("a", axis=0))  # Delete the a row.

print(df.isnull())  # Get the NaN values.  # Get the NaN values of the dataframe.
#    column1  column2  column3
# a    False    False    False
# b     True     True     True
# c    False    False    False
# d     True     True     True
# e    False    False    False
# f    False    False    False
# g     True     True     True
# h    False    False    False
print(
    df.isnull().sum())  # Get the NaN values.  # Get the NaN values of the dataframe.  # Get the NaN values of the columns.
print(df["column2"].notnull().sum())  # Get the NaN values.  # Get the NaN values of the column2 column.  # 5

print("-----------------------------------------")

data = np.random.randint(10, 100, 15).reshape(5, 3)
df = pd.DataFrame(data, index=["a", "c", "e", "f", "h"], columns=["column1", "column2", "column3"])
df = df.reindex(
    ["a", "b", "c", "d", "e", "f", "g", "h"])  # Add the missing rows.  # Add the missing rows with the NaN values.

newColumn = [np.nan, 30, np.nan, 51, np.nan, np.nan, 17, np.nan]  # Create a new column with the NaN values.
df["column4"] = newColumn
print(df)
#    column1  column2  column3  column4
# a     78.0     70.0     63.0      NaN
# b      NaN      NaN      NaN     30.0
# c     37.0     37.0     37.0      NaN
# d      NaN      NaN      NaN     51.0
# e     10.0     10.0     10.0      NaN
# f     78.0     78.0     78.0      NaN
# g      NaN      NaN      NaN     17.0
# h     63.0     63.0     63.0      NaN

print(df[df["column1"].isnull()])  # Get the NaN values.  # Get the NaN values of the column1 column.
#     column1  column2  column3  column4
# b      NaN      NaN      NaN     30.0
# d      NaN      NaN      NaN     51.0
# g      NaN      NaN      NaN     17.0
print(df[df["column1"].isnull()]["column1"])  # Get the NaN values.  # Get the NaN values of the column1 column.
# b   NaN
# d   NaN
# g   NaN
# Name: column1, dtype: float64

print(
    df.dropna())  # Delete the NaN values.  # Delete the NaN values of the dataframe.  # Delete the NaN values of the rows. default axis=0, so we don't need to write it.
# Empty DataFrame
# Columns: [column1, column2, column3, column4]
# Index: []
print(df.dropna(
    axis=1))  # Delete the NaN values.  # Delete the NaN values of the dataframe.  # Delete the NaN values of the columns.
# Empty DataFrame
# Columns: []
# Index: [a, b, c, d, e, f, g, h]

print(df.dropna(
    how="all"))  # If you want to delete the rows that all of the values are NaN, you can use the how="all" parameter.
#    column1  column2  column3  column4
# a     74.0     44.0     28.0      NaN
# b      NaN      NaN      NaN     30.0
# c     16.0     90.0     73.0      NaN
# d      NaN      NaN      NaN     51.0
# e     90.0     47.0     14.0      NaN
# f     96.0     34.0     65.0      NaN
# g      NaN      NaN      NaN     17.0
# h     31.0     49.0     26.0      NaN
print(df.dropna(
    how="any"))  # If you want to delete the rows that any of the values are NaN, you can use the how="any" parameter.
# Empty DataFrame
# Columns: [column1, column2, column3, column4]
# Index: []

print(df.dropna(subset=[
    "column1"]))  # If you want to delete the rows that the column1 values are NaN, you can use the subset=["column1"] parameter.
#    column1  column2  column3  column4
# a     74.0     44.0     28.0      NaN
# c     16.0     90.0     73.0      NaN
# e     90.0     47.0     14.0      NaN
# f     96.0     34.0     65.0      NaN
# h     31.0     49.0     26.0      NaN
print(df.dropna(
    thresh=2))  # If you want to delete the rows that the number of NaN values are more than 2, you can use the thresh=2 parameter.
#    column1  column2  column3  column4
# a     66.0     47.0     15.0      NaN
# c     79.0     61.0     84.0      NaN
# e     29.0     43.0     88.0      NaN
# f     11.0     28.0     29.0      NaN
# h     10.0     10.0     10.0      NaN

print(df.fillna(value="no data"))  # Fill the NaN values with the "no data" value.
#    column1  column2  column3  column4
# a     96.0     23.0     77.0  no data
# b  no data  no data  no data     30.0
# c     39.0     95.0     59.0  no data
# d  no data  no data  no data     51.0
# e     23.0     39.0     89.0  no data
# f     48.0     49.0     47.0  no data
# g  no data  no data  no data     17.0
# h     44.0     42.0     21.0  no data
print(df.fillna(value=1))  # Fill the NaN values with the 1 value.
#    column1  column2  column3  column4
# a     64.0     53.0     44.0      1.0
# b      1.0      1.0      1.0     30.0
# c     56.0     97.0     91.0      1.0
# d      1.0      1.0      1.0     51.0
# e     62.0     61.0     25.0      1.0
# f     98.0     70.0     74.0      1.0
# g      1.0      1.0      1.0     17.0
# h     97.0     83.0     89.0      1.0

print("--------------------")

print(df.sum())  # Calculate the sum of the values.
# column1    448.0
# column2    364.0
# column3    341.0
# column4    146.0
print(df.sum().sum())  # Calculate the sum of the values.
# 1299.0
print(df.size)  # Calculate the size of the dataframe.
# 32
print(df.isnull().sum())  # Calculate the number of NaN values.
# column1    4
# column2    4
# column3    4
# column4    8
print(df.isnull().sum().sum())  # Calculate the number of NaN values.


# 20


def calculateMean(df):
    total = df.sum().sum()
    size = df.size - df.isnull().sum().sum()
    return total / size


print(df.fillna(value=calculateMean(
    df)))  # Fill the NaN values with the mean value. # Fill the NaN values with the mean value of the dataframe.
#    column1  column2  column3  column4
# a     17.0     47.0     70.0     53.0
# b     53.0     53.0     53.0     30.0
# c     40.0     97.0     32.0     53.0
# d     53.0     53.0     53.0     51.0
# e     57.0     94.0     94.0     53.0
# f     67.0     49.0     44.0     53.0
# g     53.0     53.0     53.0     17.0
# h     15.0     78.0     55.0     53.0

print("-----------------------------------------------------------")

data = pd.read_csv(
    'survey.csv')  # Read a csv file. To read json file, use pd.read_json(). To read excel file, use pd.read_excel(). To read sql file, use pd.read_sql(). To read html file, use pd.read_html(). To read clipboard, use pd.read_clipboard(). To read python pickle object, use pd.read_pickle().
data.dropna(inplace=True)  # Delete the rows that any of the values are NaN.
print(data)

data["Industry_aggregation_NZSIOC"] = data[
    "Industry_aggregation_NZSIOC"].str.upper()  # Convert the values to uppercase.
print(data["Industry_aggregation_NZSIOC"])

data["Industry_aggregation"] = data["Industry_aggregation_NZSIOC"].str.find(
    "1")  # Find the index of the "a" character. New column is created. If the character is not found, -1 is returned.
print(data["Industry_aggregation"])

print(data[data["Industry_aggregation_NZSIOC"].str.contains(
    "1")])  # Find the rows that the values contain the "a" character.

print(data["Industry_code_ANZSIC06"].str.replace("A",
                                                 "B"))  # Replace the "A" character with the "B" character. default n=1 means that only the first "A" character is replaced.
print(data["Industry_code_ANZSIC06"].str.replace("A", "B",
                                                 n=1))  # Replace the "A" character with the "B" character. n=1 means that only the first "A" character is replaced.

print("-----------------------------------------------------------")

customers = {
    "CustomerId": [1, 2, 3, 4],
    "FirstName": ["Peter", "John", "Amy", "Hannah"],
    "LastName": ["Anderson", "Doe", "Taylor", "Smith"]
}
orders = {
    "OrderId": [10, 12, 13, 14],
    "CustomerId": [1, 2, 5, 7],
    "OrderDate": ["2019-01-01", "2019-01-02", "2019-01-03", "2019-01-04"]
}

df_customers = pd.DataFrame(customers)  # Create a dataframe from a dictionary.
df_orders = pd.DataFrame(orders)  # Create a dataframe from a dictionary.
print(df_customers)
print(df_orders)

#   CustomerId FirstName  LastName
# 0           1     Peter  Anderson
# 1           2      John       Doe
# 2           3       Amy    Taylor
# 3           4    Hannah     Smith

#    OrderId  CustomerId   OrderDate
# 0       10           1  2019-01-01
# 1       12           2  2019-01-02
# 2       13           5  2019-01-03
# 3       14           7  2019-01-04

result = pd.merge(df_customers, df_orders,
                  how="inner")  # Merge two dataframes. how="inner" means that only the common rows are returned.
print(result)
#    CustomerId FirstName  LastName  OrderId   OrderDate
# 0           1     Peter  Anderson       10  2019-01-01
# 1           2      John       Doe       12  2019-01-02

result = pd.merge(df_customers, df_orders,
                  how="left")  # Merge two dataframes. how="left" means that all the rows of the left dataframe are returned. Left dataframe is the first dataframe. So all the rows of the first dataframe are returned.
print(result)
#    CustomerId FirstName  LastName  OrderId   OrderDate
# 0           1     Peter  Anderson     10.0  2019-01-01
# 1           2      John       Doe     12.0  2019-01-02
# 2           3       Amy    Taylor      NaN         NaN
# 3           4    Hannah     Smith      NaN         NaN

result = pd.merge(df_customers, df_orders,
                  how="right")  # Merge two dataframes. how="right" means that all the rows of the right dataframe are returned. Right dataframe is the second dataframe.
print(result)
#    CustomerId FirstName  LastName  OrderId   OrderDate
# 0           1     Peter  Anderson       10  2019-01-01
# 1           2      John       Doe       12  2019-01-02
# 2           5       NaN       NaN       13  2019-01-03
# 3           7       NaN       NaN       14  2019-01-04

result = pd.merge(df_customers, df_orders,
                  how="outer")  # Merge two dataframes. how="outer" means that all the rows of both dataframes are returned.
print(result)
#    CustomerId FirstName  LastName  OrderId   OrderDate
# 0           1     Peter  Anderson     10.0  2019-01-01
# 1           2      John       Doe     12.0  2019-01-02
# 2           3       Amy    Taylor      NaN         NaN
# 3           4    Hannah     Smith      NaN         NaN
# 4           5       NaN       NaN     13.0  2019-01-03
# 5           7       NaN       NaN     14.0  2019-01-04


# concat() function is used to concatenate two dataframes. axis=0 means that the dataframes are concatenated vertically. axis=1 means that the dataframes are concatenated horizontally.
result = pd.concat([df_customers, df_orders],
                   axis=0)  # Concatenate two dataframes vertically. axis=0 means that the dataframes are concatenated vertically.
print(result)
#    CustomerId FirstName  LastName  OrderId   OrderDate
# 0           1     Peter  Anderson      NaN         NaN
# 1           2      John       Doe      NaN         NaN
# 2           3       Amy    Taylor      NaN         NaN
# 3           4    Hannah     Smith      NaN         NaN
# 0           1       NaN       NaN     10.0  2019-01-01
# 1           2       NaN       NaN     12.0  2019-01-02
# 2           5       NaN       NaN     13.0  2019-01-03
# 3           7       NaN       NaN     14.0  2019-01-04

print("-----------------------------------------------------------")

data = {
    "Column1": [1, 2, 3, 4],
    "Column2": [10, 20, 20, 40],
    "Column3": ["abc", "def", "ghi", "xyz"]
}
df = pd.DataFrame(data)
print(df)
#    Column1  Column2 Column3
# 0        1       10     abc
# 1        2       20     def
# 2        3       20     ghi
# 3        4       40     xyz

print(df["Column2"].unique())  # Get the unique values of column 2. [10 20 40]
print(df["Column2"].nunique())  # Get the number of unique values of column 2. result = 3
print(df["Column2"].value_counts())  # Get the number of each unique value of column 2.
# 20    2
# 10    1
# 40    1
# Apply functions similar to Map function in Java.
print(df["Column2"].apply(lambda x: x * 2))  # Apply a function to each value of column 2. x is the value of each row.
# 0    20
# 1    40
# 2    40
# 3    80
# Name: Column2, dtype: int64
print(df["Column3"].apply(len))  # Apply a function to each value of column 3. len() function returns the length of a string.
# 0    3
# 1    3
# 2    3
# 3    3
# Name: Column3, dtype: int64
print(df.index)  # Get the index of the dataframe. RangeIndex(start=0, stop=4, step=1. 4 is not included.)
print(df.columns)  # Get the columns of the dataframe. Index(['Column1', 'Column2', 'Column3'], dtype='object')

print(df.sort_values("Column2", ascending=False))  # Sort the dataframe by column 2. ascending=False means that the dataframe is sorted in descending order.
#    Column1  Column2 Column3
# 3        4       40     xyz
# 1        2       20     def
# 2        3       20     ghi
# 0        1       10     abc

data = {
    "Month": ["January", "February", "March", "April", "May", "June", "January", "February", "March", "April", "May", "June", ],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Books", "Books", "Books", "Books", "Books", "Books", ],
    "Amount": [100, 200, 300, 400, 500, 600, 10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)
print(df)
#        Month     Category  Amount
# 0    January  Electronics     100
# 1   February  Electronics     200
# 2      March  Electronics     300
# 3      April  Electronics     400
# 4        May  Electronics     500
# 5       June  Electronics     600
# 6    January        Books      10
# 7   February        Books      20
# 8      March        Books      30
# 9      April        Books      40
# 10       May        Books      50
# 11      June        Books      60

print(df.pivot_table(index="Month", columns="Category", values="Amount"))  # Create a pivot table. index="Month" means that the months are the index of the pivot table. columns="Category" means that the categories are the columns of the pivot table. values="Amount" means that the values of the pivot table are the amounts.
# Category  Books  Electronics
# Month
# April        40          400
# February     20          200
# January      10          100
# June         60          600
# March        30          300
# May          50          500


# Read a CSV file.
df = pd.read_csv("pokemon.csv")


def attack_power(attack, Sp_atk):
    if attack + Sp_atk > 180:
        return "Strong"
    else:
        return "Weak"


df["Attacker"] = df[["Attack", "Sp. Atk"]].apply(lambda x: attack_power(x["Attack"], x["Sp. Atk"]), axis=1)  # Create a new column named "Attacker" and apply the attack_power function to each row of the dataframe.
print(df.head(5))

#  vectorize() function is used to apply a function to each element of a dataframe. Vectorize method is faster than apply method.
df["Attacker"] = np.vectorize(attack_power)(df["Attack"], df["Sp. Atk"])  # Create a new column named "Attacker" and apply the attack_power function to each row of the dataframe.
print(df.head(5))



