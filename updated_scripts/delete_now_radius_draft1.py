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

f1_ro1 = re.compile(r'.*SessId (.*)')
f2_ro1 = re.compile(r'Service Categorization time = (.*)ms')
f3_ro1 = re.compile(r'.*The request has been categorized into service (.*)')
f4_ro1 = re.compile(r'.*user(.*) in (.*)')
f5_ro1 = re.compile(r'.*= (.*)ms')
f6_ro1 = re.compile(r'eap_peap')
f7_ro1 = re.compile(r'No.of requests in request processing tree: (.*)')
f8_ro1 = re.compile(r'.*user .*, domain (.*)')
f9_ro1 = re.compile(r'.*= (.*)ms')
f10_ro1 = re.compile(r'.*= (.*)ms')
f11_ro1 = re.compile(r'.*= (.*)ms')

#path = '/Users/vinayreddy/Desktop/logs/chandra-long/tmpA_8bYH/'
path = '/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl'

columns_smb = ['Time', 'Some Number', 'pid', 'Some info', 'Last Column']
columns_policy = ['Time', 'drop', 'Hmmm...', 'Level', 'Module', 'Message']
columns_radius = ['Time', 'drop', 'Thread/RequestNo./SessionID', 'Level','Module', 'Message']


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


def smb_df_generation():
    list_of_dfs = {}
    # Zipping the df and samba_files_csv
    for df, file in zip(dfs, samba_files_csv):
        list_of_dfs[df] = pd.read_csv(file, names = columns_smb, header=None)
    return list_of_dfs


def radius_df_generation():
    return pd.read_csv(radius_csv[0], header=None, names=columns_radius)


def policy_df_generation():
    df_policy = pd.read_csv(policy_folder + '/policy.csv', header=None, names=columns_policy)
    df2_policy = df_policy[df_policy['Message'].str.contains('.time:')]
    return df_policy, df2_policy


def f1(df_service_start):
    print('Entered into function f1')
    dict = {}
    for index in df_service_start.index:
        mo = f1_ro1.search(df_service_start.loc[index]['Thread/RequestNo./SessionID'])
        dict.setdefault(mo.group(1), 0)
        dict[mo.group(1)]=df_service_start.loc[index]['Time']
    return pd.Series(dict)

def f2(df_service_time):
    print('Entered into function f2')
    dict = {}
    for index in df_service_time.index:
        mo = f1_ro1.search(df_service_time.loc[index]['Thread/RequestNo./SessionID'])
        dict.setdefault(mo.group(1), 0)
        mo1 = f2_ro1.search(df_service_time.loc[index]['Message'])
        dict[mo.group(1)] = mo1.group(1)
    return pd.Series(dict)

def f3(df_service):
    print('Entered into function f3')
    dict = {}
    for index in df_service.index:
        mo = f1_ro1.search(df_service.loc[index]['Thread/RequestNo./SessionID'])
        dict.setdefault(mo.group(1), 0)
        mo1 = f3_ro1.search(df_service.loc[index]['Message'])
        dict[mo.group(1)] = mo1.group(1)
    return pd.Series(dict)

def f4(df_user_found_in):
    print('Entered into function f4')
    dict = {}
    dict2 = {}
    for index in df_user_found_in.index:
        mo = f1_ro1.search(df_user_found_in.loc[index]['Thread/RequestNo./SessionID'])
        dict.setdefault(mo.group(1), 0)
        dict2.setdefault(mo.group(1), 0)
        mo1 = f4_ro1.search(df_user_found_in.loc[index]['Message'])
        dict[mo.group(1)] = mo1.group(1)
        dict2[mo.group(1)] = mo1.group(2)
    return pd.Series(dict), pd.Series(dict2)

def f5(df_lookup_time):
    print('Entered into function f5')
    dict = {}
    for index in df_lookup_time.index:
        mo = f1_ro1.search(df_lookup_time.loc[index]['Thread/RequestNo./SessionID'])
        dict.setdefault(mo.group(1), 0)
        mo1 = f5_ro1.search(df_lookup_time.loc[index]['Message'])
        dict[mo.group(1)] = mo1.group(1)
    return pd.Series(dict)

def f6(df_dot1x):
    print('Entered into function f6')
    dict = {}
    for index in df_dot1x.index:
        mo = f1_ro1.search(df_dot1x.loc[index]['Thread/RequestNo./SessionID'])
        dict.setdefault(mo.group(1), 0)
        mo1 = f6_ro1.search(df_dot1x.loc[index]['Message'])
        if mo1 is not None:
            dict[mo.group(1)] = True
        else:
            dict[mo.group(1)] = False
    return pd.Series(dict)

def f7(df_tree_count):
    print('Entered into function f7')
    dict = {}
    for index in df_tree_count.index:
        mo = f1_ro1.search(df_tree_count.loc[index]['Thread/RequestNo./SessionID'])
        dict.setdefault(mo.group(1), 0)
        mo1 = f7_ro1.search(df_tree_count.loc[index]['Message'])
        dict[mo.group(1)]= mo1.group(1)
    return pd.Series(dict)

def f8(df_domain):
    print('Entered into function f8')
    dict = {}
    for index in df_domain.index:
        mo = f1_ro1.search(df_domain.loc[index]['Thread/RequestNo./SessionID'])
        dict.setdefault(mo.group(1), 0)
        mo1 = f8_ro1.search(df_domain.loc[index]['Message'])
        dict[mo.group(1)]= mo1.group(1)
    return pd.Series(dict)

def f9(df_usr_auth_time):
    print('Entered into function f9')
    dict = {}
    for index in df_usr_auth_time.index:
        mo = f1_ro1.search(df_usr_auth_time.loc[index]['Thread/RequestNo./SessionID'])
        dict.setdefault(mo.group(1), 0)
        mo1 = f9_ro1.search(df_usr_auth_time.loc[index]['Message'])
        dict[mo.group(1)]= mo1.group(1)
    return pd.Series(dict)

def f10(df_policy_time):
    print('Entered into function f10')
    dict = {}
    for index in df_policy_time.index:
        mo = f1_ro1.search(df_policy_time.loc[index]['Thread/RequestNo./SessionID'])
        dict.setdefault(mo.group(1), 0)
        mo1 = f10_ro1.search(df_policy_time.loc[index]['Message'])
        dict[mo.group(1)]= mo1.group(1)
    return pd.Series(dict)

def f11(df_request_time):
    print('Entered into function f11')
    dict = {}
    for index in df_request_time.index:
        mo = f1_ro1.search(df_request_time.loc[index]['Thread/RequestNo./SessionID'])
        dict.setdefault(mo.group(1), 0)
        mo1 = f11_ro1.search(df_request_time.loc[index]['Message'])
        dict[mo.group(1)]= mo1.group(1)
    return pd.Series(dict)


def df_f1(df_session_lines):
    return df_session_lines[df_session_lines['Message'].str.contains('Starting Service Categorization')]

def df_f2(df_session_lines):
    return df_session_lines[df_session_lines['Message'].str.contains('Service Categorization time')]

def df_f3(df_session_lines):
    return df_session_lines[df_session_lines['Message'].str.contains('The request has been categorized into service')]

def df_f4(df_session_lines):
    return df_session_lines[df_session_lines['Message'].str.contains('found user')]

def df_f5(df_session_lines):
    return df_session_lines[df_session_lines['Message'].str.contains('User lookup time')]

def df_f6(df_session_lines):
    return df_session_lines[df_session_lines['Message'].str.contains('rlm_eap_peap: Initiate')]

def df_f7(df_session_lines):
    return df_session_lines[df_session_lines['Message'].str.contains('No.of requests in request processing tree')]

def df_f8(df_session_lines):
    return df_session_lines[df_session_lines['Message'].str.contains(' authenticating user ')]

def df_f9(df_session_lines):
    return df_session_lines[df_session_lines['Message'].str.contains('User Authentication time')]

def df_f10(df_session_lines):
    return df_session_lines[df_session_lines['Message'].str.contains('Policy Evaluation time ')]

def df_f11(df_session_lines):
    return df_session_lines[df_session_lines['Message'].str.contains('Request processing time')]

def common_df_func(f):
    if f == 1:
        return df_f1(df_session_lines)
    elif f == 2:
        return df_f2(df_session_lines)
    elif f == 3:
        return df_f3(df_session_lines)
    elif f == 4:
        return df_f4(df_session_lines)
    elif f == 5:
        return df_f5(df_session_lines)
    elif f == 6:
        return df_f6(df_session_lines)
    elif f == 7:
        return df_f7(df_session_lines)
    elif f == 8:
        return df_f8(df_session_lines)
    elif f == 9:
        return df_f9(df_session_lines)
    elif f == 10:
        return df_f10(df_session_lines)
    elif f == 11:
        return df_f11(df_session_lines)

def common_func(f):
    if f == 1:
        return f1(df_service_start)
    elif f == 2:
        return f2(df_service_time)
    elif f == 3:
        return f3(df_service)
    elif f == 4:
        s_4_1, s_4_2 = f4(df_user_found_in)
        return s_4_1, s_4_2
    elif f == 5:
        return f5(df_lookup_time)
    elif f == 6:
        return f6(df_dot1x)
    elif f == 7:
        return f7(df_tree_count)
    elif f == 8:
        return f8(df_domain)
    elif f == 9:
        return f9(df_usr_auth_time)
    elif f == 10:
        return f10(df_policy_time)
    elif f == 11:
        return f11(df_request_time)


with concurrent.futures.ThreadPoolExecutor() as executor:
    radius_files, radius_config,radius_config_csv, radius_csv, radius_folder = executor.submit(radius_folder_files, path).result()
    policy_files, policy_files_csv, policy_folder = executor.submit(policy_folder_files, path).result()
    samba_files, samba_files_csv, samba_folders = executor.submit(samba_folder_files, path).result()


with concurrent.futures.ThreadPoolExecutor() as executor:
    policy_file_ordered = executor.submit(policy_file_reordering).result()
    radius_file_ordered = executor.submit(radius_file_reordering).result()


with concurrent.futures.ThreadPoolExecutor() as executor:
    radius_result, policy_result  = [executor.submit(func) for func in [radius_df_generation, policy_df_generation]]
    df_radius = radius_result.result()
    df_policy = policy_result.result()[0]
    df2_policy = policy_result.result()[1]

dfs = ['df_'+os.path.basename(folder) for folder in samba_folders]
list_of_dfs = smb_df_generation()
lines_count = df_radius.shape[0]
df_session_lines = df_radius[df_radius['Thread/RequestNo./SessionID'].str.contains(' SessId ')]
session_lines_count = df_session_lines.shape[0]

with concurrent.futures.ProcessPoolExecutor() as executor:
    df_service_start,df_service_time, df_service, df_user_found_in, df_lookup_time, df_dot1x, df_tree_count, df_domain, df_usr_auth_time, df_policy_time, df_request_time = executor.map(common_df_func, range(1,12))


with concurrent.futures.ProcessPoolExecutor() as executor:
    S1, S2, S3, (S4_1, S4_2), S5, S6, S7, S8, S9, S10, S11 = executor.map(common_func, range(1,12))

df_final = pd.DataFrame(S1, columns=['Start Time'])
for column_name, series in zip(['Service Categorization time', 'Service', 'Username', 'Auth Source', 'User Lookup time', 'Dot1x', 'Requests in request tree', 'Domain', 'User Authentication Time', 'Policy Evaluation time', 'Request Processing time'], [S2, S3, S4_1, S4_2, S5, S6, S7, S8, S9, S10, S11]):
    df_final[column_name] = series


df_final.index.name = 'Session ID'
df_final = df_final.reset_index().set_index('Start Time')
df_final.index = pd.to_datetime(df_final.index)

df_final.to_json(path + '/radius_overview.json')

end = dt.datetime.now()

print(end - start)