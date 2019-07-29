

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# a=np.array([1,34,53,45])
#
# print(a)
#
# b = np.ones((2,2), dtype=np.float16)
# print(b)
#
# print(b.dtype)
#
# print(a.dtype)


#
# csv_file=pd.read_csv('/Users/vinayreddy/Documents/test.csv')
#
# print(type(csv_file))
#
# print(csv_file)
# print(csv_file.head())
# print(csv_file.count())

df=pd.read_csv('/Users/vinayreddy/Desktop/1.csv')
#print(df.head())

# print("============")
# print(df.iloc[0:2,:])
#
# print("============")
# print(df.iloc[0:,0])

# print(df['time'])
#
# print(df['value'])
#
#
# print(df[df['value'] > 2.35])
#
# df2=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
# print(df2)
#



# Get to Know a Pandas Array
# You will use the dataframe df for the following:
#
# df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
# import pandas as pd
# ​
# df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
# 1) find the unique values in column 'a' :
#
# df['a']
# 0    1
# 1    2
# 2    1
# Name: a, dtype: int64
# 2) return a dataframe with only the rows where column a is less than two
#
# df[
#     df[df['a'] <2]
# a	b
# 0	1	1
# 2	1	1


print(np.dot(np.array([1,-1]),np.array([1,1])))

xaxis=np.linspace(0,2*np.pi, num=100)

yaxis=np.sin(xaxis)

plt.plot(xaxis,yaxis)
plt.show()

