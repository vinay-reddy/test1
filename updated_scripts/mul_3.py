import pandas as pd
import concurrent.futures
import multiprocessing
import datetime as dt
import re, timeit

start = dt.datetime.now()

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

columns_radius = ['Time', 'drop', 'Thread/RequestNo./SessionID', 'Level','Module', 'Message']
df_radius = pd.read_csv('/Users/vinayreddy/Desktop/logs/chandra-long/tmpA_8bYH/PolicyManagerLogs/tips-radius-server/radius.csv', names=columns_radius)
#df_radius = pd.read_csv('/testing/tmpF3p6JB/PolicyManagerLogs/tips-radius-server/radius.csv', names = columns_radius)
lines_count = df_radius.shape[0]

#s1 = dt.datetime.now()
df_session_lines = df_radius[df_radius['Thread/RequestNo./SessionID'].str.contains(' SessId ')]
session_lines_count = df_session_lines.shape[0]
#print(dt.datetime.now() - s1)


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
s1 = dt.datetime.now()
with concurrent.futures.ProcessPoolExecutor() as executor:
    df_service_start,df_service_time, df_service, df_user_found_in, df_lookup_time, df_dot1x, df_tree_count, df_domain, df_usr_auth_time, df_policy_time, df_request_time = executor.map(common_df_func, range(1,12))
print(f'Dataframe creation time {dt.datetime.now() - s1}')
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

with concurrent.futures.ProcessPoolExecutor() as executor:
    S1, S2, S3, (S4_1, S4_2), S5, S6, S7, S8, S9, S10, S11= executor.map(common_func, range(1,12))

df_final = pd.DataFrame(S1, columns = ['Start Time'])
for column_name, series in zip(['Service Categorization time','Service','Username', 'Auth Source', 'User Lookup time', 'Dot1x', 'Requests in request tree', 'Domain', 'User Authentication Time', 'Policy Evaluation time', 'Request Processing time' ], [S2, S3, S4_1, S4_2, S5, S6, S7, S8, S9, S10, S11]):
    df_final[column_name] = series

end = dt.datetime.now()

print(end - start)

