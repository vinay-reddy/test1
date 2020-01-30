
import pandas as pd
import os

path = '/Users/vinayreddy/Documents/Log_Analyzer_Root/media/Logs/'
def full_path(filename):
    for f, sf, files in os.walk(path):
        if filename in files:
            return f + '/' + filename


postgresInfoFile = full_path('postgres-info.txt')

file_handle = open(path + '/cluster_list.txt', 'w+')

# cluster info extraction
print('Cluster List :',file=file_handle)
print('--------------',file=file_handle)
patternFound = False
dblines = []
with open(postgresInfoFile, 'r') as fh:
    for line in fh:
        line = line.strip()
        if 'Cluster servers table' in line:
            dblines.append(line)
            patternFound = True
        elif patternFound == True and 'rows)' not in line:
            dblines.append(line)
        elif patternFound == True and 'rows)' in line:
            dblines.append(line.strip())
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
    server_values.append([item.strip() for item in line.split('|')])

server_keys = []
for each_list in server_values:
    if each_list[8] == 'f':
        server_keys.append('Sub_' + each_list[2] + '_' + each_list[5])
    elif each_list[8] == 't':
        server_keys.insert(0, 'Pub_' + each_list[2] + '_' + each_list[5])

server_values_ordered = []
for each_list in server_values:
    if each_list[8] == 'f':
        server_values_ordered.append(each_list)
    elif each_list[8] == 't':
        server_values_ordered.insert(0, each_list)

for key, value in zip(server_keys, server_values_ordered):
    servers[key] = value

df = pd.DataFrame(servers, index=columns)
print(df.loc['is_master'], file=file_handle)

ids = list(df.loc['id'])
ips = list(df.loc['management_ip'])
id_to_ip = {}
for id, ip in zip(ids, ips):
    id_to_ip[id] = ip

# for i in list(df.columns):
#     print(df[i], end= ' ', file=file_handle)
#print(df.to_markdown(), file=file_handle)
df.to_html(path + '/serverlist.html', bold_rows=True, border=0)
print(file=file_handle)
