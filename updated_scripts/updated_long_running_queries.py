

import re
import os
import csv

import pandas as pd
import datetime as dt
import pprint

start = dt.datetime.now()
def postgresql_logs_folder(path):
    postgresql_files = []
    postgresql_files_csv = []
    for f, sf, files in os.walk(path):
        if '/SystemLogs/var/lib/pgsql/data/pg_log' in f:
            for file in files:
                if 'csv' in file:
                    postgresql_files_csv.append(f+'/'+file)
                elif 'csv' not in file:
                    postgresql_files.append(f+'/'+file)
            return postgresql_files, postgresql_files_csv

postgresql_files, postgresql_files_csv = postgresql_logs_folder('/Users/vinayreddy/Desktop/logs/balaji-postgres/')

print(postgresql_files)
print(postgresql_files_csv)


regexobj=re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3}) ')

string = ''
regexobj2 = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3,}) (\w+) (\w+) (\d+) .* duration: ([\d.]+) .*?: (.*)', re.DOTALL) #good perfectly working one.
listoflines = []

if len(postgresql_files_csv) == 0 :
    for file in postgresql_files:
        with open( file, 'r') as fh:
            firstPatternFound = None
            secondPatternFound = None
            for line in fh.readlines():
                b = regexobj.search(line)
                if b is not None and firstPatternFound is None:
                    firstPatternFound =1
                    string = string + line +'\n'
                elif b is None and firstPatternFound == 1:
                    string = string + line +'\n'
                elif b is not None and firstPatternFound == 1:
                    listoflines.append(string)
                    string = ''
                    string = string + line + '\n'


    with open('/Users/vinayreddy/Desktop/logs/balaji-postgres/tmpWSB2sL/SystemLogs/var/lib/pgsql/data/pg_log/queries.csv', 'w') as fh2:
        outputwriter = csv.writer(fh2)
        for item in listoflines:
            if 'duration:' in item:
                #             print(item)
                c = regexobj2.search(item)
                #             print(c.groups())
                outputwriter.writerow(c.groups())
            #             print(list(c.groups()))
            else:
                continue


columns = ['date', 'timezone', 'dbuser', 'Dbname', 'pid', 'duration', 'statement/query']

a=pd.read_csv('/Users/vinayreddy/Desktop/logs/balaji-postgres/tmpWSB2sL/SystemLogs/var/lib/pgsql/data/pg_log/queries.csv', names=columns, header = None)

a.duration = pd.to_numeric(a.duration, errors='coerce')

b = a.sort_values(by=['duration'], ascending=False)

#print(b.info())
print(b.describe())

#print(b[:])

series = b['statement/query']

c = series.value_counts(sort=True).to_frame()
c.reset_index(inplace=True)
query_count = c.rename(columns={'index': 'statement/query', 'statement/query': 'Count'})

# d = a.set_index(['Dbname', 'statement/query']).count(level='Dbname')
# print(d)

# no. of queries on each db
db_series = a['Dbname'].value_counts(sort=True).to_frame()

db_series.reset_index(inplace=True)
db_series_count = db_series.rename(columns={'index': 'Dbname', 'Dbname': 'Count'})

print(db_series_count)
end = dt.datetime.now()

print(end - start)

'''
output of db_series_count:
        Dbname  Count
0    insightdb  38375
1    tipsLogDb   5660
2       tipsdb    891
3  AppPlatform    411
4     postgres      5
5    template1      2

output of query_count:

query to count:
      statement/query                                          Count 
COMMIT\n\n                                                     3558
SELECT * FROM aaa_session_info WHERE mac=$1 \n\n                223
SELECT public.radius_acct.acct_id AS radius_acc...              195
SELECT public.radius_acct.acct_id AS radius_acc...              170
SELECT public.radius_acct.acct_id AS radius_acc...              165
                                                             ...
UPDATE public.endpoints SET updated_at='2019-05...                1
UPDATE public.endpoints SET updated_at='2019-07...                1
select tips_dhcp_snooping_info_insert_or_update...                1
select tips_dhcp_snooping_info_insert_or_update...                1
UPDATE public.endpoints SET updated_at='2019-09...                1

'''