import pandas as pd
import subprocess
import os, re, json
import tarfile
import concurrent.futures

ro = re.compile(r'\d{4}\t')
#path = '/Users/vinayreddy/Desktop/logs/chandra-long/6_8/'
#path = '/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/'
path = '/Users/vinayreddy/Desktop/logs/chandra-long/tmpA_8bYH/'

# function to pull the full path once you pass the filename:


def full_path(filename):
    for f, sf, files in os.walk(path):
        if filename in files:
            return f + '/' + filename


config_backup_file = full_path('config-backup.tgz')

if config_backup_file is None:
    pass
else:
    to = tarfile.open(config_backup_file)
    to.extractall(path=os.path.dirname(config_backup_file))

tipsdb_content_file = full_path('tipsdb.pgdump')

with open(os.path.dirname(tipsdb_content_file) + '/tipsdb_content.txt', 'w') as fh:
    subprocess.run(['pg_restore', tipsdb_content_file ], universal_newlines=True, stdout=fh, stderr=subprocess.PIPE)

AppPlatform_content_file = full_path('AppPlatform.pgdump')

with open(os.path.dirname(AppPlatform_content_file) + '/appPlatform_content.txt', 'w') as fh:
    subprocess.run(['pg_restore', AppPlatform_content_file ], universal_newlines=True, stdout=fh, stderr=subprocess.PIPE)



sysinfo_path = full_path('sysinfo.txt')

with open(sysinfo_path) as fh:
    all_lines = fh.readlines()
    model = []
    for item in all_lines:
        if 'HARDWARE_VERSION' in item:
            print(item)
        elif item.startswith('Hostname:'):
            print(item)
        elif item.startswith('model name	'):
            model.append(item)
        elif item.startswith('Uname:'):
            index = all_lines.index(item)
            for lines in all_lines[index:index + 3]:
                print(lines.strip())
        elif item.startswith('Linux '):
            print(item)
        elif item.startswith('System login activity:'):
            for line in all_lines[all_lines.index(item):-1]:
                print(line.strip())
    print('CPU ' + model[0])

postgres_info_path = full_path('postgres-info.txt')

with open(postgres_info_path) as fh:
    for line in fh:
        print(line.strip())

tips_version_file = full_path('tips-version.properties')

with open(tips_version_file) as fh:
    print('CPPM VERSION DETAILS:')
    print('--------------------')
    for line in fh:
        if 'APP_MINOR_VERSION' not in line:
            print(line.strip())
        else:
            print(line.strip())
            app_minor_version = line.split('=')[1]

fips_file = full_path('fips-config.properties')

with open(fips_file) as fh:
    value = fh.read().split('=')[1]
    if int(value) == 0:
        print('FIPS mode is DISABLED')
    else:
        print(f'FIPS mode is ENABLED - {value}')

local_node_status = full_path('localnode.status')

with open(local_node_status) as fh:
    value = fh.read().split('=')[1]
    if 'True' in value:
        print('Local node is ENABLED')
    else:
        print(f'Local node is Disabled')

cluster_failover_status = full_path('cluster-failover.json')

with open(cluster_failover_status) as fh:
    json_string = fh.read()
    json_dict_value = json.loads(json_string)
    print()
    print(f'Server failed over: {json_dict_value["failover_status"]}')


core_files_file = full_path('core-files.list')

with open(core_files_file) as fh:
    lines = fh.readlines()
    print()
    print('Core files: ')
    print('-----------')
    for line in lines:
        print(line.strip())

system_network_config_file = full_path('system-network-config.properties')

with open(system_network_config_file) as fh:
    lines = fh.readlines()
    print()
    print('System Network Config file: ')
    print('---------------------------')
    for line in lines:
        print(line.strip())


#extraction of licenses.
# platform license.
#if int(app_minor_version) >= 8:
try:
    AppPlatform_content_file = full_path('appPlatform_content.txt')
    string = ''
    with open(AppPlatform_content_file) as infile, open(os.path.dirname(AppPlatform_content_file) + '/output', 'w') as outfile:
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
    print('\n'.join(string[1:].split('\t')[1].split('\\n')))


    tipsdb_content_file = full_path('tipsdb_content.txt')

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
        print('\n'.join(item.split('\\n')).strip())
except:
    try:
        AppPlatform_content_file = full_path('appPlatform_content.txt')
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
            print('Platform License: ')
            print('-----------------')
            for line in fh:
                line = line.strip()
                print(line)

        tipsdb_content_file = full_path('tipsdb_content.txt')

        with open(tipsdb_content_file) as infile, open(os.path.dirname(tipsdb_content_file) + '/output', 'w') as outfile:
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
                print(line)
    except:
        print('Leave licenses. Its a headache and not worth the hard work.')
        #========================
postgresInfoFile = full_path('postgres-info.txt')

# cluster info extraction
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

print(df)

core_backtraces_file = full_path('core-backtraces.list')

utils_file = full_path('utils.log')
print()
try:
    with open(utils_file) as fh:
        copy = False
        for line in fh:
            if 'Current system configuration' in line.strip():
                copy = True
                print(line.strip())
            elif line in ['\n', '\r\n'] and copy == True:
                copy = False
                break
            elif copy:
                print(line.strip())
except:
    print('Maybe this is a HW, will see how to fetch details when this is the case.')

event_viewer_file = full_path('tips-system-events.txt')
columns = ['Time', 'Task', 'Level', 'By', 'Description', 'status']
df_ev = pd.read_csv(event_viewer_file, header = None, skiprows=1, sep='|', names=columns)

print(df_ev)