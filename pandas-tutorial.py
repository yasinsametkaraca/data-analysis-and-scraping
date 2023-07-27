import pandas as pd  # Pandas is a data analysis library. It is used to import data from csv file. It is used to create dataframes. It is used to create series. It is used to create dataframes from dictionaries.
import numpy as np

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

