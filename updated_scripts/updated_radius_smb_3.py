import re, csv
import subprocess, os
import pprint
import operator
import pandas as pd
import datetime as dt
import concurrent.futures

start = dt.datetime.now()

reg_obj_smb = re.compile(r'^\[[\d/]+')
reg_obj2_smb = re.compile(r'([\d/ :.]+),\s+(\d),\s+pid=(\d+)\]\s+(.*)\n(.*)')
reg_obj3_smb = re.compile(r'\[([\d/ :.]+),\s+(\d),\s+pid=(\d+)\]\s+(.*?)\n(.*)',re.DOTALL)
reg_obj4_smb = re.compile(r'.*domain (.*) from .*')
reg_obj5_smb = re.compile(r'.*= (.*) ms')
reg_obj_policy = re.compile(r'(\d{4}(-\d{2}){2} [\d:,]+) \[(.*?)\] ([A-Z]+?)\s+(.*?) - (.*?)\n')
regexobj2_postgresql = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3,}) (\w+) (\w+) (\d+) .* duration: ([\d.]+) .*?: (.*)', re.DOTALL) #good perfectly working one.
regexobj_postgresql= re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3}) ')
regex_system_load_monitor = re.compile(r'(([\d -:]+(PM|AM))\n(.*?load average: ([\d .]+),([\d .]+),([\d .]+))\n.*\n([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+([\d. ]+)ni, ([\d. ]+)id, ([\d. ]+)wa, ([\d. ]+)hi, ([\d. ]+)si, ([\d. ]+)st)\n(KiB Mem : ([\d ]+)total,([\d ]+)free,([\d ]+)used,([\d ]+)buff/cache)\n(KiB Swap:([\d ]+)total,([\d ]+)free,([\d ]+)used.([\d ]+)avail Mem))')


path = '/Users/vinayreddy/Desktop/logs/chandra-long/tmpA_8bYH/'

columns_smb = ['Time', 'Some Number', 'pid', 'Some info', 'Last Column']
columns_policy = ['Time', 'drop', 'Hmmm...', 'Level', 'Module', 'Message']
columns_radius = ['Time', 'drop', 'Thread/RequestNo./SessionID', 'Level','Module', 'Message']
columns_postgresql = ['date', 'timezone', 'dbuser', 'Dbname', 'pid', 'duration', 'statement/query']
columns_system_load_monitor = ['Date-Time', '1 Min load avg', '5 Min load avg', '15 Min load avg', 'us', 'sy', 'ni', 'id','wa', 'hi', 'si', 'st', 'KiB Memory-Total', 'KiB Memory-free', 'KiB Memory-used', 'KiB Memory-Buff/Cache', 'KiB Swap-total', 'KiB Swap-free', 'KiB Swap-used', 'KiB Swap-available-Mem']


def start_and_end_time(file_list):
    end_time = subprocess.check_output(['tail', '-1', file_list[0]]).decode('utf8').split(',')[1]
    start_time = subprocess.check_output(['head', '-1', file_list[-1]]).decode('utf8').split(',')[1]
    return end_time, start_time


def radius_folder_files(path):
    radius_files = []
    radius_csv = []
    radius_config = []
    radius_config_csv = []
    radius_folder = ''

    for f, sf, files in os.walk(path):
        if '/PolicyManagerLogs/tips-radius-server' in f:
            radius_folder = f
            for file in files:
                if 'csv' in file:
                    radius_csv.append(f+'/'+file)
                elif 'radius_config_csv' in file:
                    radius_config_csv.append(f+'/'+file)
                elif 'radius.log' in file:
                    radius_files.append(f+'/'+file)
                elif 'radius_config' in file:
                    radius_config.append(f+'/'+file)

            return radius_files, radius_config,radius_config_csv, radius_csv, radius_folder


def policy_folder_files(path):
    policy_files = []
    policy_files_csv = []
    policy_folder = ''
    for f, sf, files in os.walk(path):
        if 'PolicyManagerLogs/policy-server' in f:
            policy_folder = f
            for file in files:
                if 'csv' in file:
                    policy_files_csv.append(f + '/' + file)
                elif 'policy-server.log' in file:
                    policy_files.append(f + '/' + file)
            return policy_files, policy_files_csv, policy_folder


def policy_file_reordering():
    policy_file_ordered = []
    path = os.path.dirname(policy_files[0])
    for i in range(len(policy_files)):
        policy_file_ordered.append(path+ '/policy-server.log.' + str(i))
    return policy_file_ordered


def radius_file_reordering():
    radius_file_ordered = []
    path = os.path.dirname(radius_files[0])
    for i in range(len(radius_files)):
        radius_file_ordered.append(path+ '/radius.log.' + str(i))
    return radius_file_ordered


def samba_folder_files(path):
    samba_files = []
    samba_files_csv = []
    samba_folders = []
    for f, fs, files in os.walk(path):
        if '/PolicyManagerLogs/samba/' in f:
            samba_folders.append(f)
            for file in files:
                if 'csv' in file:
                    samba_files_csv.append(f + '/' + file)
                elif 'log.wb' in file:
                    samba_files.append(f + '/' + file)
    return samba_files, samba_files_csv, samba_folders


def policy_csv_creation():
    print('inside policy csv creation')
    a = dt.datetime.now()
    if len(policy_files_csv) == 0:
        for file in policy_file_ordered[::-1]:
            fileh2 = open(policy_folder + '/lines_that_didnt_match_policy.txt','w+')

            fileh = open(policy_folder + '/policy.csv','a+')
            csvoutput = csv.writer(fileh)

            with open(file, 'a') as fh:
                fh.write('\n')  #last line of the file doesn't match if new line is not added.

            with open(file, 'r') as fh_read:
                for line in fh_read:
                    mo=reg_obj_policy.search(line)
                    if mo is not None:
                        csvoutput.writerow(mo.groups())
                    else:
                        fileh2.write(line)  #writing the lines that didnt match the regex.

            fileh.close()
            fileh2.close()
    b = dt.datetime.now()
    return 'Success policy- ', b - a


def smb_csv_creation():
    print('inside smb csv creation')
    z = dt.datetime.now()
    #    print(z)
    pattern_found = None
    string = ''
    line_list = []
    if len(samba_files_csv) == 0:
        #        print('Samba Folders: ',samba_folders)
        for folder in samba_folders:
            samba_o_files, samba_o_csv, samba_o_folders= samba_folder_files(folder)
            #            print('Samba Files: ', samba_files)
            for file in reversed(samba_o_files):
                line_list = []
                #                print('SambaFile: ', file)
                with open(file, 'r') as fh:
                    for line in fh:
                        a = reg_obj_smb.search(line)
                        if a is not None and pattern_found is None:
                            string = string + line
                            pattern_found = 1
                        elif a is None and pattern_found == 1:
                            string = string + line
                        elif a is not None and pattern_found == 1:
                            line_list.append(string)
                            string = ''
                            string = string + line
                            pattern_found = 1
                fileh = open(folder+ '/samba.csv','a+')
                csvoutput = csv.writer(fileh)
                for line in line_list:
                    mo = reg_obj3_smb.search(line)
                    try:
                        csvoutput.writerow([mo[1], mo[2], mo[3], mo[4], mo[5].strip('\n')])
                    except:
                        print('In except condition : line ==== m0[1]: ', mo[1])
                        print('In except condition : line ==== mo[2]: ', mo[2])
                        print('In except condition : line ==== mo[3]: ', mo[3])
                        print('In except condition : line ==== mo[4]: ', mo[4])
                        print('In except condition : line ==== mo[5]: ', mo[5])

                fileh.close()
    b = dt.datetime.now()
    print(b)
    return 'Success samba -', b - z


def radius_csv_creation():
    print('inside radius csv creation')
    a = dt.datetime.now()
    if len(radius_csv) == 0:
        fileh2 = open(radius_folder + '/lines_that_didnt_match.txt','a')
        fileh = open(radius_folder + '/radius.csv','a')
        csvoutput = csv.writer(fileh)
        regex_obj = re.compile(r'(\d{4}(-\d{2}){2} [\d:,]+) \[(.*?)\] ([A-Z]+?)\s+(.*?) - (.*?)\n')
        for file in radius_file_ordered:
            with open(file, 'a') as fh:
                fh.write('\n')  #last line of the file doesn't match if new line is not added.
        for file in radius_files:
            with open(file, 'r',encoding="utf8", errors='ignore' ) as fh3:
                for line in fh3:
                    mo=regex_obj.search(line)
                    if mo is not None:
                        csvoutput.writerow(mo.groups())
                    else:
                        fileh2.write(line)  #writing the lines that didnt match the regex.

        fileh.close()
        fileh2.close()
    b = dt.datetime.now()
    return 'Success radius -', b - a


def smb_df_generation():
    dfs = ['df_'+os.path.basename(folder) for folder in samba_folders]
    list_of_dfs = {}
    # Zipping the df and samba_files_csv
    for df, file in zip(dfs, samba_files_csv):
        list_of_dfs[df] = pd.read_csv(file, names = columns_smb, header=None)
    return list_of_dfs


def radius_df_generation():
    df_radius = pd.read_csv(radius_csv[0], header=None, names=columns_radius)
    return df_radius


def policy_df_generation():
    df_policy = pd.read_csv(policy_folder + '/policy.csv', header=None, names=columns_policy)
    df2_policy = df_policy[df_policy['Message'].str.contains('.time:')]
    return df_policy, df2_policy
# function to return samba lines:


def smb_log_line_extraction(start_time, end_time, netbios_name):
    for name in dfs:
        print('this is the list of dfs: ',dfs)
        if netbios_name in name:
            print('inside smb_log_line_extraction function')
            list_of_dfs[name].set_index(['Time'], inplace=True)
            print(list_of_dfs[name])
        return list_of_dfs[name].loc[start_time:end_time]


def auth_request(session_id, df_radius, list_of_dfs):
    df5_radius = df_radius[df_radius['Thread/RequestNo./SessionID'].str.contains(session_id)]
    df6_radius = df5_radius[df5_radius['Message'].str.contains("Service Categorization time|LDAP/AD User lookup time|MS-Chap User Authentication time|Policy Evaluation time|Request processing time|SQL User lookup time", regex=True)]
    df8_radius = df5_radius[df5_radius['Message'].str.contains("rlm_mschap: Using domain ")]
    df9_radius = df5_radius[df5_radius['Message'].str.contains('eap_peap')]
    df10_radius = df5_radius[df5_radius['Message'].str.contains('MS-Chap User Authentication time =')]
    df11_radius = df5_radius.set_index(['Time'])
    print(len(df9_radius))
    if len(df9_radius) != 0:
        if len(df8_radius) != 0:
            start_time = df8_radius.reset_index()['Time'][0]
            start_time_tmp = dt.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S,%f')
            start_time = dt.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S,%f').strftime('%Y/%m/%d %H:%M:%S.%f')
        else:
            start_time = None
            start_time_tmp = None
        mo = reg_obj5_smb.search(df10_radius.reset_index()['Message'][0])
        if mo is not None:
            milliseconds = mo.group(1)
            delta = dt.timedelta(milliseconds=int(milliseconds) + 10)
            if start_time_tmp is not None:
                end_time_tmp = start_time_tmp + delta
                end_time = end_time_tmp.strftime('%Y/%m/%d %H:%M:%S.%f')
            else:
                end_time = None
        else:
            end_time = None

        mo = reg_obj4_smb.search(str(df8_radius.reset_index()['Message'][0]))
        if mo is not None:
            netbios_name = mo.group(1)
        else:
            netbios_name = None
        if len(list_of_dfs) !=0:
            samba_lines = smb_log_line_extraction(start_time, end_time, netbios_name)
            return df5_radius, df6_radius, samba_lines, df11_radius
        else:
            samba_lines = None
            return df5_radius, df6_radius, samba_lines, df11_radius
    else:
        start_time = None
        end_time = None
        netbios_name = None
        samba_lines = None
        return df5_radius, df6_radius, samba_lines, df11_radius
# function to pull all the session ids for a specific users
def session_ids_per_username(username):

    return username_session_id_dict[username]
# function to create a dictionary of user with corresponding session ids as values in a list
def user_session_ids():

    username_session_id_dict = {}
    regex_obj2 = re.compile(r'.* user (.*?) in .*')
    regex_obj3 = re.compile(r'.*SessId (.*)')
    #    for line1, line2 in df7[['Thread/RequestNo./SessionID','Message']]:
    for i in df7.index:
        line1 = df7['Thread/RequestNo./SessionID'][i]
        line2 = df7['Message'][i]
        mo1 = regex_obj3.search(line1)
        mo2 = regex_obj2.search(line2)
        sess_id = mo1.group(1)
        name = mo2.group(1)
        if name not in username_session_id_dict:
            username_session_id_dict[name] = [sess_id]
        else:
            username_session_id_dict[name].append(sess_id)

    return username_session_id_dict

def allLogs(session_id):
    df5, df6, samba_lines, df11 = auth_request(session_id)
    df14 = filterSessionId(session_id)
    return df5, df6, samba_lines, df11, df14

def filterSessionId(sessionID):
    df14 = df12[df12['Hmmm...'].str.contains(sessionID)]
    #     print(df3)
    return df14
# unique session ids:
def unique_sessions():
    session_id_list = []
    username_session_id_dict_var = user_session_ids()
    for name, session_ids in username_session_id_dict_var.items():
        session_id_list = session_id_list + session_ids
    return session_id_list
# username - count
def user_vs_authcount():
    username_count_dict = {}
    username_session_id_dict_var = user_session_ids()
    for key, value in username_session_id_dict_var.items():
        username_count_dict[key] = len(value)
    sorted_username_count = sorted(username_count_dict.items(), key=operator.itemgetter(1), reverse= True)
    return sorted_username_count

#=============

def http_folder_files(path):
    http_ssl_files = []
    http_files = []
    http_csv = []
    http_ssl_csv = []
    for f, sf, files in os.walk(path):
        if '/SystemLogs/var/log/httpd' in f:
            for file in files:
                if 'ssl_csv' in file:
                    http_ssl_csv.append(f+'/'+file)
                elif 'http_csv' in file:
                    http_csv.append(f+'/'+file)
                elif 'ssl_access' in file:
                    http_ssl_files.append(f+'/'+file)
                elif 'access' in file:
                    http_files.append(f+'/'+file)
            return http_files, http_ssl_files, http_ssl_csv, http_csv

def http_csv_creation():
    print('inside http csv creation')
    z = dt.datetime.now()
    if len(http_ssl_csv) == 0 and len(http_csv) == 0:
        for i in range(len(http_ssl_files)):

            fh2 = open(os.path.dirname(http_ssl_files[i])+'/ssl_csv'+'.'+ str(i), 'a')
            with open(http_ssl_files[i], 'r') as fh:
                for line in fh:
                    line = line.strip()
                    a = line.split()
                    fh2.write(a[0] + ',' + a[3].split('[')[1]+','+ a[5].split('"')[1] + ',' + a[-1].split('µ')[0] +',' + a[6]+','+ a[7].split('"')[0] + '\n')
            fh2.close()

        for i in range(len(http_files)):

            fh2 = open(os.path.dirname(http_files[i])+'/http_csv'+'.'+ str(i), 'a')
            with open(http_files[i], 'r') as fh:
                for line in fh:
                    line = line.strip()
                    a = line.split()
                    fh2.write(a[0] + ',' + a[3].split('[')[1]+','+ a[5].split('"')[1] + ',' + a[-1].split('µ')[0] +',' + a[6]+','+ a[7].split('"')[0] + '\n')
            fh2.close()
    b = dt.datetime.now()
    return 'Success httpd - ', b - z

def postgresql_logs_folder(path):
    postgresql_files = []
    postgresql_files_csv = []
    for f, sf, files in os.walk(path):
        if '/SystemLogs/var/lib/pgsql/data/pg_log' in f:
            postgresql_folder = f
            for file in files:
                if 'csv' in file:
                    postgresql_files_csv.append(f+'/'+file)
                elif 'csv' not in file:
                    postgresql_files.append(f+'/'+file)
            return postgresql_files, postgresql_files_csv, postgresql_folder

def postgresql_csv_creation():
    print('inside postgresql csv creation')
    z = dt.datetime.now()
    string = ''
    listoflines = []
    if len(postgresql_files_csv) == 0 :
        for file in postgresql_files:
            with open( file, 'r') as fh:
                firstPatternFound = None
                secondPatternFound = None
                for line in fh.readlines():
                    b = regexobj_postgresql.search(line)
                    if b is not None and firstPatternFound is None:
                        firstPatternFound =1
                        string = string + line +'\n'
                    elif b is None and firstPatternFound == 1:
                        string = string + line +'\n'
                    elif b is not None and firstPatternFound == 1:
                        listoflines.append(string)
                        string = ''
                        string = string + line + '\n'


    with open( postgresql_folder + '/queries.csv', 'w') as fh2:
        outputwriter = csv.writer(fh2)
        for item in listoflines:
            if 'duration:' in item:
                #             print(item)
                c = regexobj2_postgresql.search(item)
                #             print(c.groups())
                outputwriter.writerow(c.groups())
            #             print(list(c.groups()))
            else:
                continue
    y = dt.datetime.now()
    return 'Success postgresql - ', y - z


def postgres_df_generation():
    df_postgres = pd.read_csv(postgresql_files_csv[0], names=columns_postgresql, header=None)
    return df_postgres


def system_load_monitor_folder_files(path):
    print('inside the System Load Monitor folder files now')
    print(path)
    system_load_files = []
    system_load_files_csv = []
    for f, sf, files in os.walk(path):
        if '/PolicyManagerLogs/system-load-monitor' in f:
            for file in files:
                if file == 'system-load-csv':
                    system_load_files_csv.append(f+'/'+file)
                elif 'system-load' in file:
                    system_load_files.append(f+'/'+file)
            return system_load_files, system_load_files_csv, f

def system_load_monitor_csv_creation():
    print('inside system_load_monitor_csv_creation')
    z = dt.datetime.now()
    if len(system_load_files_csv) == 0 :
        for j in range(len(system_load_files)):
            with open( system_load_files[j], 'r') as fh:
                a= fh.read()
                b = re.split('\n\s*\n', a)
                c = [ i for i in b if 'load average:' in i]
                #            with open(system_load_files[j] +'_csv_'+ str(j), 'w' ) as fh2:
                with open( f + '/system-load-csv' ,'a' ) as fh2:
                    csv_fh = csv.writer(fh2)
                    for i in c:
                        d = regex_system_load_monitor.search(i)
                        if d is not None:
                            csv_fh.writerow([d[2].strip(), d[5].strip(), d[6].strip(), d[7].strip(), d[9].strip(), d[10].strip(), d[11].strip(), d[12].strip(), d[13].strip(), d[14].strip(),d[15].strip(), d[16].strip(), d[18].strip(), d[19].strip(), d[20].strip(), d[21].strip(), d[23].strip(), d[24].strip(), d[25].strip(),d[26].strip()])
                        else:
                            continue
                            #print('printing else part -', i)
    y = dt.datetime.now()
    return 'Success system load monitor - ', y - z

def system_load_monitor_df_generation():
    df_system_load_monitor = pd.read_csv(f + '/system-load-csv', names=columns_system_load_monitor,  header=None)
    return df_system_load_monitor

def systemLoadMonitorLinesExtract(time):
    for file in system_load_files:
        fh = open(file)
        file_read = fh.read()
        count=file_read.count(time)
        print('Count =', count)
        if count == 2:
            regex_sys_load_mon_1 = re.compile(r'{}.*?{}.*?{}' .format(time, time, '\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]{2}'), re.DOTALL)
            mo = regex_sys_load_mon_1.search(file_read)
            if mo is not None:
                a = mo.group()
                return a
        elif count == 1:
            regex_sys_load_mon_2 = re.compile(r'{}.*?{}' .format(time, '\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]{2}'), re.DOTALL)
            print(regex_sys_load_mon_2)
            mo = regex_sys_load_mon_2.search(file_read)
            if mo is not None:
                a = mo.group()
                return a
            else:
                print('You are in this else block')
                regex_sys_load_mon_3 = re.compile(r'{}.*' .format(time), re.DOTALL)
                print(regex_sys_load_mon_3)
                mo = regex_sys_load_mon_3.search(file_read)
                if mo is not None:
                    a = mo.group()
                    return a
        elif count == 0:
            continue

with concurrent.futures.ThreadPoolExecutor() as executor:
    radius_files, radius_config,radius_config_csv, radius_csv, radius_folder = executor.submit(radius_folder_files, path).result()
    policy_files, policy_files_csv, policy_folder = executor.submit(policy_folder_files, path).result()
    samba_files, samba_files_csv, samba_folders = executor.submit(samba_folder_files, path).result()
    http_files, http_ssl_files, http_ssl_csv, http_csv = executor.submit(http_folder_files, path).result()
    postgresql_files, postgresql_files_csv, postgresql_folder = executor.submit(postgresql_logs_folder, path).result()
    system_load_files, system_load_files_csv, f = executor.submit(system_load_monitor_folder_files, path).result()

with concurrent.futures.ThreadPoolExecutor() as executor:
    policy_file_ordered = executor.submit(policy_file_reordering).result()
    radius_file_ordered = executor.submit(radius_file_reordering).result()


with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(func) for func in [radius_csv_creation, policy_csv_creation, smb_csv_creation, http_csv_creation, postgresql_csv_creation, system_load_monitor_csv_creation]]

    for result in results:
        print(result.result()[0], result.result()[1])

with concurrent.futures.ThreadPoolExecutor() as executor:
    radius_files, radius_config,radius_config_csv, radius_csv, radius_folder = executor.submit(radius_folder_files, path).result()
    policy_files, policy_files_csv, policy_folder = executor.submit(policy_folder_files, path).result()
    samba_files, samba_files_csv, samba_folders = executor.submit(samba_folder_files, path).result()
    http_files, http_ssl_files, http_ssl_csv, http_csv = executor.submit(http_folder_files, path).result()
    postgresql_files, postgresql_files_csv, postgresql_folder = executor.submit(postgresql_logs_folder, path).result()
    system_load_files, system_load_files_csv, f = executor.submit(system_load_monitor_folder_files, path).result()

with concurrent.futures.ThreadPoolExecutor() as executor:
    radius_result, policy_result, postgres_result, systemLoadMonitor_result = [executor.submit(func) for func in [radius_df_generation, policy_df_generation, postgres_df_generation, system_load_monitor_df_generation]]
    df_radius = radius_result.result()
    df_policy = policy_result.result()[0]
    df2_policy = policy_result.result()[1]
    df_postgres = postgres_result.result()
    df_system_load_monitor = systemLoadMonitor_result.result()

end = dt.datetime.now()

print(end - start)












'''
To-do:
>>> print(a)
2019-11-06 01:04:38.621840
a.strftime('%Y/%m/%d %H:%M:%S.%f)
'2019/11/06 01:04:38.621840'   ---> samba logs time format


target:
1.  session_id, Username, service, times - 
2.  we should be able to  filter based on the request processing time, service categorization time, user look up time, mschap v2 authentication time , Policy evaluation time ?
3.  Should be able to plot a graph based on above times 
4.  Should be able to plot graph based on the frequency of authentications. per 1 min, 5 mins, 10, 15, 30min, 1 hour, 2, 4, 8 hrs. 1 day.
5.  

#df5, df6, samba_lines, df11, df14 = allLogs('R0012ba0f-01-5db1ca8c')
#
# for index in df14.index:
#     print('Policy-Server')
#     print(df14['Time'][index], df14['Hmmm...'][index], df14['Level'][index], df14['Module'][index], df14['Message'][index])
# radius_files, radius_config,radius_config_csv, radius_csv, radius_folder = radius_folder_files(path)
# policy_files, policy_files_csv, policy_folder = policy_folder_files(path)
# samba_files, samba_files_csv, samba_folders = samba_folder_files(path)


'''





















