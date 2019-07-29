import csv
import pandas as pd
import pprint


columns = ['date', 'timezone', 'dbuser', 'Dbname', 'pid', 'duration', 'statement/query']
a=pd.read_csv('queries.csv', names=columns, header = None)

a.duration = pd.to_numeric(a.duration, errors='coerce')

b = a.sort_values(by=['duration'], ascending=False)

print(b.describe())

series = b['statement/query']

c = series.value_counts(sort=True)

print b

#c =b.groupby(by='statement/query', sort=True).head(5)