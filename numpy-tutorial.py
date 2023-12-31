import numpy as np  # numpy used for working with arrays. Mathematically, it is used for linear algebra, fourier transform, and matrices.

py_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Python list
np_array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Numpy array

print(type(py_list))  # <class 'list'>
print(type(np_array1))  # <class 'numpy.ndarray'>


py_multi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Python multi-dimensional list
np_multi = np_array1.reshape(3, 3)  # Numpy multi-dimensional array

print(py_multi)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np_multi)  # [[1 2 3]
                 # [4 5 6]
                 # [7 8 9]]

print(np_array1.ndim)  # 1 (1-dimensional)
print(np_multi.ndim)  # 2 (2-dimensional)

print(np_array1.shape)  # (9,) (1-dimensional with 9 elements)
print(np_multi.shape)  # (3, 3) (2-dimensional with 3 rows and 3 columns)

print(np_array1.size)  # 9 (1-dimensional with 9 elements)
print(np_multi.size)  # 9 (2-dimensional with 9 elements)

print(np.arange(1, 10))  # [1 2 3 4 5 6 7 8 9]
print(np.arange(1, 11, 2))  # [1 3 5 7 9]

print(np.zeros(5))  # [0. 0. 0. 0. 0.]
print(np.ones(5))  # [1. 1. 1. 1. 1.]  # float
print(np.ones(5, dtype=int))  # [1 1 1 1 1]  # int
print(np.linspace(0, 100, 5))  # [  0.  25.  50.  75. 100.]   5 evenly spaced numbers between 0 and 100

print(np.random.randint(0, 10, 5))  # [0 9 3 7 3]  5 random integers between 0 and 10
print(np.random.rand(5))  # 5 random floats between 0 and 1
print(np.random.randn(5))  # 5 random floats from the standard normal distribution. Negative values are possible.
print(np.random.choice([1, 2, 3, 4, 5], 3))  # [1 4 4 ]  3 random choices from the given list

np_multi1 = np.arange(50).reshape(5, 10)  # 2-dimensional array with 5 rows and 10 columns. 0 to 49. Matrix-like.
print(np_multi1)
print(np_multi.sum(axis=1))  # [ 45 145 245 345 445]  Sum of each row
print(np_multi.sum(axis=0))  # [ 60  70  80  90 100]  Sum of each column

random_numbers = np.random.randint(1, 100, 10)  # 10 random integers between 1 and 100
print(random_numbers)
print(random_numbers.max())  # 99 # (Random) Maximum value
print(random_numbers.min())  # 1 # (Random) Minimum value
print(random_numbers.mean())  # 51.5 # Average
print(random_numbers.argmax())  # 8 # Index of the maximum value
print(random_numbers.argmin())  # 0 # Index of the minimum value

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 1-dimensional array
print(numbers[4])  # 5
print(numbers[1:4])  # [2 3 4] # Elements from index 1 to 4 (not including 4)
print(numbers[:4])  # [1 2 3 4]  # First 4 elements
print(numbers[4:])  # [5 6 7 8 9]  # Elements from index 4 to the end
print(numbers[::2])  # [1 3 5 7 9]  # Every other element. Third parameter is the step size. First parameter is the start index. Second parameter is the end index (not including the end index)
print(numbers[::-1])  # [9 8 7 6 5 4 3 2 1]  # Reverse the array
print(numbers[-1])  # 9  # Last element
print(numbers[-4:])  # [6 7 8 9]  # Last 4 elements
print(numbers[-4:-1])  # [6 7 8]  # Elements from index -4 to -1 (not including -1)
print(numbers[1:3:1])  # [2 3]  # Elements from index 1 to 3 (not including 3) with step size 1

numbers1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 2-dimensional array
print(numbers1)  # [[1 2 3]
                 # [4 5 6]
                 # [7 8 9]]
print(numbers1[1][2])  # 6
print(numbers1[1, 2])  # 6
print(numbers1[1])  # [4 5 6]
print(numbers1[1, :])  # [4 5 6] # First parameter is the row index. Second parameter is the column index. : means all columns
print(numbers1[:, 1])  # [2 5 8] # All rows. Second column
print(numbers1[1:, 1:])  # [[5 6] [8 9]] # From row index 1 to the end. From column index 1 to the end
print(numbers1[:, 2])  # [3 6 9] # All rows. Third column
print(numbers1[:, 2:])  # [[3] [6] [9]] # All rows. From column index 2 to the end
print(numbers1[:, 0:2])  # [[2] [5] [8]] # All rows. From column index 1 to 2 (not including 2)
print(numbers1[1:, 0:2])  # [[4 5] [7 8]] # Choose from row index 1 to the end. From column index 1 to 2 (not including 2)
print(numbers1[-1, :])  # [7 8 9] # Last row. All columns
print(numbers1[-1, 1:])  # [8 9] # Last row. From column index 1 to the end
print(numbers1[-1, 1])  # 8 # Last row. Second column
print(numbers1[0])  # [1 2 3] # First row. All columns

numbers2 = np.arange(1, 10)
numbers3 = numbers2.copy()  # Copy the array. Value type assignment. Both variables point to different arrays.
numbers3[0] = 10
print(numbers2)  # [1 2 3 4 5 6 7 8 9]
print(numbers3)  # [10  2  3  4  5  6  7  8  9]

numbers4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
numbers5 = numbers4  # Assign the array to another variable. Both variables point to the same array. Reference type assignment. If you change one variable, the other variable will also change.
numbers5[0] = 10
print(numbers4)  # [10  2  3  4  5  6  7  8  9]
print(numbers5)  # [10  2  3  4  5  6  7  8  9]

numbers6 = np.random.randint(10, 100, 5)  # 5 random integers between 10 and 100
numbers7 = np.random.randint(10, 100, 5)  # 5 random integers between 10 and 100
print(f"number6 {numbers6}")
print(numbers7)
print(numbers6 + numbers7)  # Add the elements of the arrays with the same index
print(numbers6 - numbers7)  # Subtract the elements of the arrays with the same index
print(numbers6 * numbers7)  # Multiply the elements of the arrays with the same index
print(numbers6 + 10)  # Add 10 to each element
print(np.sin(numbers6))  # Calculate the sine of each element
print(np.cos(numbers6))  # Calculate the cosine of each element
print(np.log(numbers6))  # Calculate the natural logarithm of each element
print(np.sqrt(numbers6))  # Calculate the square root of each element
print(np.square(numbers6))  # Calculate the square of each element
print(np.power(numbers6, 2))  # Calculate the power of each element

numbers8 = np.random.randint(10, 100, 6)
print(numbers8)
print(numbers8 > 50)  # for example: [False False False  True  True  True] # Compare each element with 50
print(numbers8[numbers8 > 50])  # [51 52 53] # Get the elements that are greater than 50
print(numbers8 % 2 == 0)  # [False  True False  True False  True] # Get the even numbers. Compare each element with 2
print(numbers8[numbers8 % 2 == 0])  # [52 54 56] # Get the even numbers.
print(numbers8[(numbers8 % 2 == 0) & (numbers8 > 50)])  # [52 54 56] # Get the even numbers that are greater than 50
print(numbers8[(numbers8 % 2 == 0) | (numbers8 > 50)])  # [51 52 53 54 55 56] # Get the even numbers or the numbers that are greater than 50
result = numbers8 > 50
print(numbers8[result])  # [] # Get the elements that are greater than 50

multinumber8 = numbers8.reshape(2, 3)  # Reshape the array to 2 rows and 3 columns
multinumber9 = np.random.randint(10, 100, 6).reshape(2, 3)  # Reshape the array to 2 rows and 3 columns
print(multinumber8)
print(multinumber9)
print(np.vstack((multinumber8, multinumber9)))  # Stack the arrays vertically
print(np.hstack((multinumber8, multinumber9)))  # Stack the arrays horizontally

numbers10 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 2-dimensional array
evens = numbers10[numbers10 % 2 == 0]  # Get the even numbers
print(evens)  # [2 4 6 8]
print(evens[evens > 4])  # [6 8] # Get the even numbers that are greater than 4
