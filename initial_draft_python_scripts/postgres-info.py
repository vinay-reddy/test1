
import pandas as pd
import os
import datetime as dt

start = dt.datetime.now()
def postgres_info_file(path):
    for f, sf, files in os.walk(path):
        if '/PolicyManagerLogs' in f:
            for file in files:
                if file == 'postgres-info.txt':
                    return (f + '/' +file)

postgresInfoFile = postgres_info_file('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/')

# cluster info extraction
patternFound = False
dblines = []
with open(postgresInfoFile, 'r') as fh:
    for line in fh:
        line = line.strip()
        if 'Cluster servers table' in line:
            dblines.append(line)
            patternFound = True
        elif patternFound == True and 'rows' not in line:
            dblines.append(line)
        elif patternFound == True and 'rows' in line:
            dblines.append(line)
            break
        else:
            continue

No_of_servers = int(dblines[-1].split('(')[1].split(' ')[0])
columns = []
for item in dblines[1].split('|'):
    columns.append(item.strip())

servers = {}
server_keys = [ 'server_'+str(i) for i in range(1, No_of_servers + 1)]
server_values = []

for line in dblines[3:-1]:
    server_values.append([ item.strip() for item in line.split('|')])

for key, value in zip(server_keys, server_values):
    servers[key] = value


df = pd.DataFrame(servers, index=columns)
print(df.loc['is_master'])
end = dt.datetime.now()

print(end - start)

'''

todo:
1. put the publisher as first column
2. rename columns names such that, publisher will have publisher as the column name and other servers will have subscribers_i as the column names.
'''