import re, csv
import pandas as pd
import subprocess, os
import datetime as dt
import sys
import pprint
import operator

start = dt.datetime.now()

def start_and_end_time(file_list):
    end_time = subprocess.check_output(['tail', '-1', file_list[0]]).decode('utf8').split(',')[1]
    start_time = subprocess.check_output(['head', '-1', file_list[-1]]).decode('utf8').split(',')[1]
    return end_time, start_time

def radius_folder_files(path):
    radius_files = []
    radius_csv = []
    radius_config = []
    radius_config_csv = []
    for f, sf, files in os.walk(path):
        if '/PolicyManagerLogs/tips-radius-server' in f:
            for file in files:
                if 'csv' in file:
                    radius_csv.append(f+'/'+file)
                elif 'radius_config_csv' in file:
                    radius_config_csv.append(f+'/'+file)
                elif 'radius.log' in file:
                    radius_files.append(f+'/'+file)
                elif 'radius_config' in file:
                    radius_config.append(f+'/'+file)
            return radius_files, radius_config,radius_config_csv, radius_csv

radius_files, radius_config, radius_config_csv, radius_csv = radius_folder_files('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/')

radius_file_ordered = []
path = os.path.dirname(radius_files[0])
for i in range(len(radius_files)):
    radius_file_ordered.append(path+ '/radius.log.' + str(i))
print(radius_file_ordered)

if len(radius_csv) == 0:
    fileh2 = open('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/PolicyManagerLogs/tips-radius-server/lines_that_didnt_match.txt','a')
    fileh = open('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/PolicyManagerLogs/tips-radius-server/radius.csv','a')
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

columns = ['Time', 'drop', 'Thread/RequestNo./SessionID', 'Level','Module', 'Message']

df = pd.read_csv('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/PolicyManagerLogs/tips-radius-server/radius.csv', header= None, names = columns)
df=df.drop(['drop'], axis=1)

df2 = df[df['Level'] == 'ERROR']
df3 = df[df['Message'].str.contains('Session-Id = ')]

#df7 = df[df['Message'].str.contains('User-Name = ')]
df7 = df[df['Message'].str.contains(' searching for user ')]

session_id_list = []
for line in df3['Message']:
    if 'Acct-Session-Id' not in line and 'acct_broadcast' not in line :
        session_id = line.split('Session-Id = ')[-1].strip('"')
        session_id_list.append(session_id)
unique_sessions = list(set(session_id_list))

print(unique_sessions)
print(len(unique_sessions))

#function to give the entire authentication for a user per request Id (df5) and times taken (df6)
def auth_request(session_id, file):
    df5 = df[df['Thread/RequestNo./SessionID'].str.contains(session_id)]
    df6 =df5[df5['Message'].str.contains("Service Categorization time|LDAP/AD User lookup time|MS-Chap User Authentication time|Policy Evaluation time|Request processing time|SQL User lookup time", regex=True)]
    return df5, df6

df5, df6 = auth_request('R00125806-01-5db11969', '/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/PolicyManagerLogs/tips-radius-server/radius.csv' )

# for i in unique_sessions:
#     print('Session ID: ', i)
#     df5,df6 = auth_request(i, radius_csv)
#     print(df6)
end = dt.datetime.now()

# function to pull all the session ids for a specific users


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

# username - count

username_count_dict = {}
for key, value in username_session_id_dict.items():
    username_count_dict[key] = len(value)

sorted_username_count = sorted(username_count_dict.items(), key=operator.itemgetter(1), reverse= True)
print(sorted_username_count)

pprint.pprint(username_session_id_dict)
# function to pull all users

print(end - start)


'''
To-do:

>>> print(a)
2019-11-06 01:04:38.621840

a.strftime('%Y/%m/%d %H:%M:%S.%f)


'2019/11/06 01:04:38.621840'   ---> samba logs time format

'''





















#Acct-Session-Id
# "Service Categorization time|LDAP//AD User lookup time|MS-Chap User Authentication time|Policy Evaluation time|Request processing time|SQL User lookup time"
#Service Categorization time
#LDAP/AD User lookup time
#MS-Chap User Authentication time
#Policy Evaluation time
#Request processing time
#SQL User lookup time
#radius_file_ordered = ['/Users/vinayreddy/Desktop/logs/vijay_escalation/tmpaMlez1/PolicyManagerLogs/tips-radius-server/radius.log.0', '/Users/vinayreddy/Desktop/logs/vijay_escalation/tmpaMlez1/PolicyManagerLogs/tips-radius-server/radius.log.1', '/Users/vinayreddy/Desktop/logs/vijay_escalation/tmpaMlez1/PolicyManagerLogs/tips-radius-server/radius.log.2']
#regex_obj = re.compile(r'(\d{4}(-\d{2}){2} [\d:,]+) \[(.*?)\] ([A-Z]+?)\s+RadiusServer.Radius - (.*?)\n')
#regex_obj = re.compile(r'(\d{4}(-\d{2}){2} [\d:,]+) \[(.*?)\] ([A-Z]+?)\s+(.*)')
#radius_files.sort()
#print(radius_files)
# print(radius_config)
#print(radius_csv)
# print(radius_config_csv)
