import csv
import pandas as pd
import pprint

# with open('file.txt', 'w') as fh:
#     outputwriter=csv.writer(fh)
#     outputwriter.writerow(['vinay', '2','er'])
#

columns = ['date', 'timezone', 'dbuser', 'Dbname', 'pid', 'duration', 'statement/query']

a=pd.read_csv('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/SystemLogs/var/lib/pgsql/data/pg_log/queries.csv', names=columns, header = None)

a.duration = pd.to_numeric(a.duration, errors='coerce')
#a.duration = pd.to_numeric(a.duration)
#print(a['statement/query'])

#print(a['duration'].dtype)

#print(a)

# if a['duration'] > 1000:
#     print[]

b = a.sort_values(by=['duration'], ascending=False)

#print(b.info())
print(b.describe())

#print(b[:])

series = b['statement/query']

c = series.value_counts(sort=True)


#c =b.groupby(by='statement/query', sort=True).head(5)

