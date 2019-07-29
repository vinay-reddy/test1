import csv
import pandas as pd
import pprint


columns = ['date', 'timezone', 'dbuser', 'Dbname', 'pid', 'duration', 'statement/query']

a=pd.read_csv('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/SystemLogs/var/lib/pgsql/data/pg_log/queries.csv', names=columns, header = None)

a.duration = pd.to_numeric(a.duration, errors='coerce')


b = a.sort_values(by=['duration'], ascending=False)


print(b.describe())

b.to_csv(r'/Users/vinayreddy/Desktop/logs/balaji/csv_file.csv')

series = b['statement/query']

c = series.value_counts(sort=True)


#print(c)

