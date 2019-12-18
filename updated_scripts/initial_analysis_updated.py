import pandas as pd
import subprocess
import os, re, json
import tarfile
import numpy as np
import concurrent.futures

ro = re.compile(r'\d{4}\t')
path = '/Users/vinayreddy/Desktop/logs/chandra-long/6_7/tmpgfR9Qo'
#path = '/Users/vinayreddy/Desktop/logs/kushal/tmp505h5X/'
#path = '/Users/vinayreddy/Desktop/logs/rohit-1/tmpDAUyYu'

def full_path(filename):
    for f, sf, files in os.walk(path):
        if filename in files:
            return f + '/' + filename


postgres_info_path = full_path('postgres-info.txt')
tips_version_file = full_path('tips-version.properties')
fips_file = full_path('fips-config.properties')
local_node_status = full_path('localnode.status')
cluster_failover_status = full_path('cluster-failover.json')
core_files_file = full_path('core-files.list')
system_network_config_file = full_path('system-network-config.properties')
postgresInfoFile = full_path('postgres-info.txt')
tipsdb_content_file = full_path('tipsdb_content.txt')
AppPlatform_content_file = full_path('appPlatform_content.txt')
config_backup_file = full_path('config-backup.tgz')
sysinfo_path = full_path('sysinfo.txt')
core_backtraces_file = full_path('core-backtraces.list')
utils_file = full_path('utils.log')

list_of_start_lines = ['Size of all databases:', 'Current Blocked and Blocking Queries', 'Top relations in [tipsdb] over 1 MB:',]


# function to pull the full path once you pass the filename:

file_handle = open(path + '/initial_analysis.txt', 'w+')
print(path + '/initial_analysis.txt')

# with open(postgres_info_path) as fh:
#     print(f'Printing postgres-info.txt file: ')
#     for line in fh:
#         print(line.strip())

def extracting_lines(start_line, end_line, filepath):
    with open(filepath) as inf:
        grab = False
        for l in inf:
            if start_line in l.strip():
                grab = True
                print(l.strip(), file=file_handle)
            elif l.startswith(end_line) and grab is True:
                print(l.strip(), file=file_handle)
                break
            elif grab:
                print(l.strip(), file=file_handle)



#1. extracting the backup and converting the pgdump to text using pg_restore. (Doing nothing for now.)


if config_backup_file is None:
    pass
else:
    to = tarfile.open(config_backup_file)
    to.extractall(path=os.path.dirname(config_backup_file))

    tipsdb_content_file = full_path('tipsdb.pgdump')

    with open(os.path.dirname(tipsdb_content_file) + '/tipsdb_content.txt', 'w') as fh:
        subprocess.run(['pg_restore', tipsdb_content_file], universal_newlines=True, stdout=fh, stderr=subprocess.PIPE)

    with open(os.path.dirname(AppPlatform_content_file) + '/appPlatform_content.txt', 'w') as fh:
        subprocess.run(['pg_restore', AppPlatform_content_file], universal_newlines=True, stdout=fh, stderr=subprocess.PIPE)

#2.

with open(sysinfo_path) as fh:
    all_lines = fh.readlines()
    model = []
    for item in all_lines:
        if 'HARDWARE_VERSION' in item:
            print(item, file=file_handle)
        elif item.startswith('Hostname:'):
            print(item, file=file_handle)
        elif item.startswith('model name	'):
            model.append(item)
        elif item.startswith('Uname:'):
            index = all_lines.index(item)
            for lines in all_lines[index:index + 3]:
                print(lines.strip(), file=file_handle)
        elif item.startswith('Linux '):
            print(item, file=file_handle)
    print('CPU ' + model[0], file=file_handle)

extracting_lines('Current system time=', '(1 row)', postgres_info_path)
print(file=file_handle)

# Version of the server

with open(tips_version_file) as fh:
    print('CPPM VERSION DETAILS:', file=file_handle)
    print('--------------------', file=file_handle)
    for line in fh:
        if 'APP_MINOR_VERSION' not in line:
            print(line.strip(), file=file_handle)
        else:
            print(line.strip(), file=file_handle)
            app_minor_version = line.split('=')[1]

print(file=file_handle)

# Current system configuration
try:
    with open(utils_file) as fh:
        copy = False
        for line in fh:
            if 'Current system configuration' in line.strip():
                copy = True
                print(line.strip(), file=file_handle)
            elif line in ['\n', '\r\n'] and copy == True:
                copy = False
                break
            elif copy:
                print(line.strip(), file=file_handle)
except:
    print('Maybe this is a HW, will see how to fetch details when this is the case.', file=file_handle)

print(file=file_handle)
print(file=file_handle)

for line in list_of_start_lines:
    endline = '====='
    extracting_lines(line, endline, postgres_info_path )

# system network details of the server :

with open(system_network_config_file) as fh:
    lines = fh.readlines()
    print(file=file_handle)
    print('System Network Config file: ', file=file_handle)
    print('---------------------------', file=file_handle)
    for line in lines:
        print(line.strip(), file=file_handle)


# fips node present or not

with open(fips_file) as fh:
    value = fh.read().split('=')[1]
    string = 'FIPS mode is'
    if int(value) == 0:
        a = 'DISABLED'
        print(f'{string.ljust(20)}:{a.rjust(10)}', file=file_handle)
    else:
        a = 'ENABLED'
        print(f'{string.ljust(20)}:{a.rjust(10)}', file=file_handle)


# local node status

with open(local_node_status) as fh:
    value = fh.read().split('=')[1]
    string = 'Local node is'
    if 'True' in value:
        a = 'ENABLED'
        print(f'{string.ljust(20)}:{a.rjust(10)}', file=file_handle)
    else:
        a = 'DISABLED'
        print(f'{string.ljust(20)}:{a.rjust(10)}', file=file_handle)

# cluster failover status

with open(cluster_failover_status) as fh:
    json_string = fh.read()
    json_dict_value = json.loads(json_string)
    string = 'Server failed over'
    value = str(json_dict_value["failover_status"])
    print(f'{string.ljust(20)}:{value.upper().rjust(10)}', file=file_handle)

# core files present ?
with open(core_files_file) as fh:
    lines = fh.readlines()
    print(file=file_handle)
    print('Core files: ', file=file_handle)
    print('-----------', file=file_handle)
    for line in lines:
        print(line.strip(), file=file_handle)

print(file=file_handle)

# core backtrace files


# extraction of licenses.
# platform license.
# if int(app_minor_version) >= 8:
try:
    string = ''
    with open(AppPlatform_content_file) as infile, open(os.path.dirname(AppPlatform_content_file) + '/output',
                                                        'w') as outfile:
        copy = False
        for line in infile:
            if 'COPY public.license_info' in line.strip():
                copy = True
                continue
            elif line in ['\n', '\r\n']:
                copy = False
                continue
            elif copy:
                outfile.write(line)

    with open(os.path.dirname(AppPlatform_content_file) + '/output') as fh:
        for line in fh:
            line = line.strip()
            string = string + line
    print('\n'.join(string[1:].split('\t')[1].split('\\n')), file=file_handle)


    string = ''

    with open(tipsdb_content_file) as infile, open(os.path.dirname(tipsdb_content_file) + '/output', 'w') as outfile:
        copy = False
        for line in infile:
            if 'COPY public.license_info' in line.strip():
                copy = True
                continue
            elif line in ['\n', '\r\n']:
                copy = False
                continue
            elif copy:
                outfile.write(line)

    with open(os.path.dirname(tipsdb_content_file) + '/output') as fh:
        for line in fh:
            line = line.strip()
            string = string + line

    for item in ro.split(string):
        print('\n'.join(item.split('\\n')).strip(), file=file_handle)
except:
    try:
        with open(AppPlatform_content_file) as infile, open(os.path.dirname(AppPlatform_content_file) + '/output', 'w') as outfile:
            copy = False
            for line in infile:
                if 'COPY license_info' in line.strip():
                    copy = True
                    continue
                elif line in ['\n', '\r\n']:
                    copy = False
                    continue
                elif copy:
                    outfile.write(line)
        with open(os.path.dirname(AppPlatform_content_file) + '/output') as fh:
            print('Platform License: ', file=file_handle)
            print('-----------------', file=file_handle)
            for line in fh:
                line = line.strip()
                print(line, file=file_handle)


        with open(tipsdb_content_file) as infile, open(os.path.dirname(tipsdb_content_file) + '/output',
                                                       'w') as outfile:
            copy = False
            for line in infile:
                if 'COPY license_info' in line.strip():
                    copy = True
                    continue
                elif line in ['\n', '\r\n']:
                    copy = False
                    continue
                elif copy:
                    outfile.write(line)

        with open(os.path.dirname(tipsdb_content_file) + '/output') as fh:
            for line in fh:
                line = line.strip()
                print(line, file=file_handle)
    except:
        print('Leave licenses. Its a headache and not worth the hard work.', file=file_handle)

print(file=file_handle)
print(file=file_handle)

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
        elif patternFound == True and 'row' not in line:
            dblines.append(line)
        elif patternFound == True and 'row' in line:
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

print(df, file=file_handle)
print(file=file_handle)

print('Event Viewer: ',file=file_handle)
print('-------------',file=file_handle)
# event viewer
event_viewer_file = full_path('tips-system-events.txt')
columns = ['Time', 'Source', 'Level', 'Category', 'Description', 'Action']
df_ev = pd.read_csv(event_viewer_file, header=None, skiprows=1, sep='|', names=columns)
filtered_df = df_ev[(df_ev['Level'].str.strip() == 'ERROR')|(df_ev['Level'].str.strip() == 'WARN')]
lens = []
for col in filtered_df.columns:
    lens.append(max(filtered_df[col].str.strip().map(len).values))
print(filtered_df.columns[0].ljust(lens[0]), filtered_df.columns[1].ljust(lens[1]),filtered_df.columns[2].ljust(lens[2]),filtered_df.columns[3].ljust(lens[3]),filtered_df.columns[4].ljust(lens[4]), filtered_df.columns[5].ljust(lens[5]), file=file_handle)
print(file=file_handle)
for index, row in filtered_df.iterrows():
    row = row.str.strip()
    print(row['Time'].ljust(lens[0]), row['Source'].ljust(lens[1]), row['Level'].ljust(lens[2]), row['Category'].ljust(lens[3]), row['Description'].ljust(lens[4]), row['Action'].ljust(lens[5]), sep='\t', file=file_handle)


with open(sysinfo_path) as fh:
    all_lines = fh.readlines()
    model = []
    for item in all_lines:
        if item.startswith('System login activity:'):
            print(file=file_handle)
            print('System login activity:', file=file_handle)
            print('----------------------', file=file_handle)
            print(file=file_handle)
            for line in all_lines[all_lines.index(item)+1:-1]:
                print(line.strip(), file=file_handle)

file_handle.close()