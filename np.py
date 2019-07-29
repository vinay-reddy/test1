"""

video 1:

 Data Types
 Creating arrays
 Slicing Arrays
 Mathematics
 Methods and Functions


 Video 1: Numpy data types

 Numpy data types which is how numpy handles data
 Discussing Numpy arrays

 Numpy "ndarray" is the reasons of Numpy's existance
 ndarrays have a specified dtype and store data in a multidimensional, tabular like format.
 Most ndarrays have one or two dimensions (so vector like or matrix like), but, arbitrary number of dimensions are possible.
 Numpy arrays exist to allow or storing data and for giving python the linear algebra functionality.


Numpy data types:

Numpy introduces new data types, or dtypes to manage data
dtypes emulate data types seen in other programming languages like C, C++ / FORTRAN (i.e fixed lenght)
dtypes have a hierarchy, some are special instances of others.
dtypes have lengths, int8 is a 8 bit integer.



type                                     Description

int8, int16, int32, int64                integer(signed)
uint8, uint16, uint32, uint64            integer(unsigned)
float16, float32, float64, float128      Floating point number
bool_                                    Boolean (True or False)
string_                                  Fixed length string type
unicode_                                 fixed length unicode type


>>>import np as np

>>>
>>> int_ones = np.ones((2,2), dtype=np.int8)
>>> int_ones
array([[1, 1],
       [1, 1]], dtype=int8)
>>> int_ones.dtypes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'numpy.ndarray' object has no attribute 'dtypes'
>>> int_ones.dtype
dtype('int8')
>>>


>>>
>>>
>>> float_ones = np.ones((3,3), dtype=np.float16)
>>> float_ones
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]], dtype=float16)
>>>

>>> float_ones.dtype
dtype('float16')
>>>

>>>
>>> uint_ones = np.ones((2,2), dtype=uint16)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'uint16' is not defined
>>> uint_ones = np.ones((2,2), dtype=np.uint16)
>>> uint_ones
array([[1, 1],
       [1, 1]], dtype=uint16)
>>>


>>> int_ones([1,1]) = -1
  File "<stdin>", line 1
SyntaxError: can't assign to function call
>>> int_ones[(1,1)] = -1
>>>
>>> int_ones
array([[ 1,  1],
       [ 1, -1]], dtype=int8)
>>>
>>> int_ones[(1,1)] = -1
>>> int_ones
array([[ 1,  1],
       [ 1, -1]], dtype=int8)
>>> int_ones[1,1] = -1
>>> int_ones
array([[ 1,  1],
       [ 1, -1]], dtype=int8)
>>>
>>>




"""

import numpy as np


a = [2,34,5,6]

b = np.array(a)

print(b)

c = np.ones((2,3,4))
print(c)


d = np.array([[1, 2, 3, 4], [5, 6, 7, 8, 9]])
print(type(d))

d = np.array([[1,2,3,4], [5,6,7,8,9]])

print(d)

e = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [2,34,5,6]])

print(e)
print(e.shape)
print(e.ndim)

arr1 = np.array([1,2,34,5], dtype=np.float64)
print(arr1)

import pandas as pd

series = pd.Series(np.arange(3), index=['a', 'b', 'c'])

frame = pd.DataFrame(np.arange(12).reshape(4,3), index = ['a','c', 'd', 'e'])

print(frame.add(frame.T, fill_value = 0))





def multiply2(x):
    return x * 2

a= map(multiply2, [1, 2, 3, 4])  # Output [2, 4, 6, 8]


print(a)