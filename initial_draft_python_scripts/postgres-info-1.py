
import pandas as pd
import os
import datetime as dt
import re

start = dt.datetime.now()

reg_obj_tipsdb = re.compile(r'([\d -:,]+).*relative lag=([\d]+) .* nodeId ([\d]+)')

def postgres_info_file(path):
    for f, sf, files in os.walk(path):
        if '/PolicyManagerLogs' in f:
            for file in files:
                if file == 'postgres-info.txt':
                    return (f + '/' +file)

def tips_db_files(path):
    tips_db_log_file_list = []
    tips_db_relative_lag_file = []
    for f, sf, files in os.walk(path):
        if '/PolicyManagerLogs/tips-db' in f:
            tips_db_folder = f
            for file in files:
                if 'relative_lag_csv' in file:
                    tips_db_relative_lag_file.append(f +'/' + file)
                elif 'log' in file:
                    tips_db_log_file_list.append(f + '/' + file)
            return tips_db_log_file_list, tips_db_relative_lag_file, tips_db_folder

postgresInfoFile = postgres_info_file('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/')
tips_db_log_file_list, tips_db_relative_lag_file, tips_db_folder = tips_db_files('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/')

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
server_values = []

for line in dblines[3:-1]:
    server_values.append([ item.strip() for item in line.split('|')])

server_keys = []
for each_list in server_values:
    if each_list[8] == 'f':
        server_keys.append('Sub_' + each_list[2] +'_'+ each_list[5])
    elif each_list[8] == 't':
        server_keys.insert(0, 'Pub_' + each_list[2] +'_'+ each_list[5])

server_values_ordered = []
for each_list in server_values:
    if each_list[8] == 'f':
        server_values_ordered.append(each_list)
    elif each_list[8] == 't':
        server_values_ordered.insert(0,each_list)

for key, value in zip(server_keys, server_values_ordered):
    servers[key] = value


df = pd.DataFrame(servers, index=columns)
print(df.loc['is_master'])

ids = list(df.loc['id'])
ips = list(df.loc['management_ip'])
id_to_ip = {}
for id, ip in zip(ids, ips):
    id_to_ip[id] = ip

tips_db_log_file_list, tips_db_relative_lag_file, tips_db_folder = tips_db_files('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/')
if len(tips_db_relative_lag_file) == 0:
    for file in tips_db_log_file_list[::-1]:
        with open(file, 'r') as fh:
            fh_w = open(tips_db_folder + '/' + 'relative_lag_csv', 'a+')
            for line in fh:
                line = line.strip()
                if 'DbClusterDiagnostics Updated last replication lag timestamp' in line:
                    mo = reg_obj_tipsdb.search(line)
                    # print(mo)
                    if mo is not None:
                        fh_w.write('"' + mo.group(1).strip()+ '",' + mo.group(2) + ',' + mo.group(3) + ',' + id_to_ip[mo.group(3)] + '\n')
                        # print(mo.groups())
            fh_w.close()

print(df)
columns_relative_lag = ['Time', 'Relative Lag in Seconds', 'Node Id', 'Node IP']
df2 = pd.read_csv(tips_db_folder + '/' + 'relative_lag_csv', names= columns_relative_lag, header= None)

df3 = df2[df2['Node Id'] == 5]
end = dt.datetime.now()
print(end - start)

'''

todo:
1. put the publisher as first column
2. rename columns names such that, publisher will have publisher as the column name and other servers will have subscribers_i as the column names.
'''