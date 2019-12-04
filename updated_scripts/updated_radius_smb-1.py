import re, csv
import subprocess, os
import pprint
import operator
import pandas as pd
import datetime as dt

start = dt.datetime.now()

reg_obj_smb = re.compile(r'^\[[\d/]+')
reg_obj2_smb = re.compile(r'([\d/ :.]+),\s+(\d),\s+pid=(\d+)\]\s+(.*)\n(.*)')
reg_obj3_smb = re.compile(r'\[([\d/ :.]+),\s+(\d),\s+pid=(\d+)\]\s+(.*?)\n(.*)',re.DOTALL)
reg_obj4_smb = re.compile(r'.*domain (.*) from .*')
reg_obj5_smb = re.compile(r'.*= (.*) ms')
reg_obj_policy = re.compile(r'(\d{4}(-\d{2}){2} [\d:,]+) \[(.*?)\] ([A-Z]+?)\s+(.*?) - (.*?)\n')


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

radius_files, radius_config, radius_config_csv, radius_csv, radius_folder = radius_folder_files('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl')

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

policy_files, policy_files_csv, policy_folder = policy_folder_files('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl')

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

samba_files, samba_files_csv, samba_folders = samba_folder_files('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl')

# samba csv file creation for each samba_%NETBOIS_NAME folder.

pattern_found = None
string = ''
line_list = []
if len(samba_files_csv) == 0:
    print('Samba Folders: ',samba_folders)
    for folder in samba_folders:
        samba_files, samba_files_csv, samba_folders = samba_folder_files(folder)
        print('Samba Files: ', samba_files)
        for file in reversed(samba_files):
            line_list = []
            print('SambaFile: ', file)
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

samba_files, samba_files_csv, samba_folders = samba_folder_files('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl')
#by now, there is one csv file for each samba_%NETBOIS_NAME folder. All these folders are present in samba_folders variable.
columns_smb = ['Time', 'Some Number', 'pid', 'Some info', 'Last Column']

# Generation of dataframe names
dfs = ['df_'+os.path.basename(folder) for folder in samba_folders]
list_of_dfs = {}
# Zipping the df and samba_files_csv
for df, file in zip(dfs, samba_files_csv):
    list_of_dfs[df] = pd.read_csv(file, names = columns_smb, header=None)

# function to return samba lines:

def smb_log_line_extraction(start_time, end_time, netbios_name):
    for name in dfs:
        print('this is the list of dfs: ',dfs)
        if netbios_name in name:
            print('inside smb_log_line_extraction function')
            list_of_dfs[name].set_index(['Time'], inplace=True)
            print(list_of_dfs[name])
        return list_of_dfs[name].loc[start_time:end_time]


########## Policy CSV file creation #########
policy_files, policy_files_csv, policy_folder = policy_folder_files('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl')

policy_file_ordered = []
path = os.path.dirname(policy_files[0])
for i in range(len(policy_files)):
    policy_file_ordered.append(path+ '/policy-server.log.' + str(i))
print(policy_file_ordered)


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

columns_policy = ['Time', 'drop', 'Hmmm...', 'Level', 'Module', 'Message']

df12 = pd.read_csv(policy_folder + '/policy.csv', header= None, names = columns_policy)
df13 = df12[df12['Message'].str.contains('.time:')]

def filterSessionId(sessionID):
    df14 = df12[df12['Hmmm...'].str.contains(sessionID)]
    #     print(df3)
    return df14



########## radius csv file creation #########

radius_file_ordered = []
path = os.path.dirname(radius_files[0])
for i in range(len(radius_files)):
    radius_file_ordered.append(path+ '/radius.log.' + str(i))
print(radius_file_ordered)

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

radius_files, radius_config, radius_config_csv, radius_csv, radius_folder = radius_folder_files('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl')
print(radius_csv)
columns = ['Time', 'drop', 'Thread/RequestNo./SessionID', 'Level','Module', 'Message']

df = pd.read_csv(radius_csv[0], header= None, names = columns)
df = df.drop(['drop'], axis=1)
df2 = df[df['Level'] == 'ERROR']
#df3 = df[df['Message'].str.contains('Session-Id = ')]
df7 = df[df['Message'].str.contains(' searching for user ')]

#function to give the entire authentication for a user per request Id (df5) and times taken (df6)
#to-do -- should include lines from samba and policy server logs.
def auth_request(session_id):
    df5 = df[df['Thread/RequestNo./SessionID'].str.contains(session_id)]
    df6 = df5[df5['Message'].str.contains("Service Categorization time|LDAP/AD User lookup time|MS-Chap User Authentication time|Policy Evaluation time|Request processing time|SQL User lookup time", regex=True)]
    df8 = df5[df5['Message'].str.contains("rlm_mschap: Using domain ")]
    df9 = df5[df5['Message'].str.contains('eap_peap')]
    df10 = df5[df5['Message'].str.contains('MS-Chap User Authentication time =')]
    df11 = df5.set_index(['Time'])
    print(len(df9))
    if len(df9) != 0:
        if len(df8) != 0:
            start_time =df8.reset_index()['Time'][0]
            start_time_tmp = dt.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S,%f')
            start_time = dt.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S,%f').strftime('%Y/%m/%d %H:%M:%S.%f')
        else:
            start_time = None
            start_time_tmp = None
        mo = reg_obj5_smb.search(df10.reset_index()['Message'][0])
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

        mo = reg_obj4_smb.search(str(df8.reset_index()['Message'][0]))
        if mo is not None:
            netbios_name = mo.group(1)
        else:
            netbios_name = None
        if len(list_of_dfs) !=0:
            samba_lines = smb_log_line_extraction(start_time, end_time, netbios_name)
            return df5, df6, samba_lines, df11
        else:
            samba_lines = None
            return df5, df6, samba_lines, df11
    else:
        start_time = None
        end_time = None
        netbios_name = None
        samba_lines = None
        return df5, df6, samba_lines, df11

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

username_session_id_dict= user_session_ids()

# unique session ids:
session_id_list = []

for name, session_ids in username_session_id_dict.items():
    session_id_list = session_id_list + session_ids


# username - count

username_count_dict = {}
for key, value in username_session_id_dict.items():
    username_count_dict[key] = len(value)

sorted_username_count = sorted(username_count_dict.items(), key=operator.itemgetter(1), reverse= True)
#print(sorted_username_count)

#pprint.pprint(username_session_id_dict)
# function to pull all users

def allLogs(session_id):
    df5, df6, samba_lines, df11 = auth_request(session_id)
    df14 = filterSessionId(session_id)
    return df5, df6, samba_lines, df11, df14

df5, df6, samba_lines, df11, df14 = allLogs('R0012ba0f-01-5db1ca8c')

for index in df14.index:
    print('Policy-Server')
    print(df14['Time'][index], df14['Hmmm...'][index], df14['Level'][index], df14['Module'][index], df14['Message'][index])

end = dt.datetime.now()

# lengths = []
# for session in session_id_list:
#     lengths.append(len(session))
#
# all_lengths = list(set(lengths))


###########----> start <----############

print(end - start)


'''
To-do:

>>> print(a)
2019-11-06 01:04:38.621840

a.strftime('%Y/%m/%d %H:%M:%S.%f)


'2019/11/06 01:04:38.621840'   ---> samba logs time format


1. 

target:

1.  session_id, Username, service, times - 

2.  we should be able to  filter based on the request processing time, service categorization time, user look up time, mschap v2 authentication time , Policy evaluation time ?

3.  Should be able to plot a graph based on above times 

4.  Should be able to plot graph based on the frequency of authentications. per 1 min, 5 mins, 10, 15, 30min, 1 hour, 2, 4, 8 hrs. 1 day.

5.  
'''





















