import pandas as pd
import csv, re, os
import datetime as dt
import pprint
import concurrent.futures
import multiprocessing
import csv

# with open('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/PolicyManagerLogs/tips-radius-server/test.csv', 'r') as f:
#     reader = csv.reader(f)
#     your_list = list(reader)
# #
# print(your_list)
start = dt.datetime.now()
#list = [['2019-10-23 15:35:12,353', '-23', 'Th 31707 Req 10364795 SessId R0011c034-01-5db0d5a0', "'INFO'", "'RadiusServer.Radius'", "'rlm_service: Starting Service Categorization - 62:220:7CA1AE0940FD']"], ['2019-10-23 15:35:12,358', '-23"', 'Th 31707 Req 10364795 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'Service Categorization time = 5 ms'], ['2019-10-23 15:35:12,358', '-23', 'Th 31707 Req 10364795 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'rlm_service: The request has been categorized into service "WLAN eduroam 802.1X - csudh.edu"'], ['2019-10-23 15:35:12,360', '-23', 'Th 31707 Req 10364795 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'rlm_ldap: found user mjauregui14 in AD:campus.csudh.edu'], ['2019-10-23 15:35:12,360', '-23', 'Th 31707 Req 10364795 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'LDAP/AD User lookup time = 2 ms'], ['2019-10-23 15:35:12,360', '-23', 'Th 31707 Req 10364795 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'rlm_eap_peap: Initiate'], ['2019-10-23 15:35:12,462', '-23', 'Th 31705 Req 10364804 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'No.of requests in request processing tree: 50'], ['2019-10-23 15:35:12,574', '-23', 'Th 31704 Req 10364818 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'rlm_mschap: authenticating user mjauregui14, domain CAMPUS'], ['2019-10-23 15:35:12,578', '-23', 'Th 31704 Req 10364818 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'rlm_mschap: user mjauregui14 authenticated successfully'], ['2019-10-23 15:35:12,578', '-23', 'Th 31704 Req 10364818 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'MS-Chap User Authentication time = 4 ms'], ['2019-10-23 15:35:12,612', '-23', 'Th 31702 Req 10364820 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'Policy Evaluation time = 20 ms'], ['2019-10-23 15:35:12,612', '-23', 'Th 31702 Req 10364820 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'rlm_policy: Received Accept Enforcement Profile'], ['2019-10-23 15:35:12,618', '-23', 'Th 31710 Req 10364822 SessId R0011c034-01-5db0d5a0', 'INFO', 'RadiusServer.Radius', 'Request processing time = 267 ms']]
path = '/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/PolicyManagerLogs/tips-radius-server/'
columns_radius = ['Time', 'drop', 'Thread/RequestNo./SessionID', 'Level','Module', 'Message']

#df_radius = pd.Datarame( your_list, columns=columns_radius)
df_radius = pd.read_csv( path + 'test.csv', names=columns_radius)

empty_dict = {'Start_time': None, 'Service Categorization time': None, 'Service':None, 'Username': None, 'Auth Source': None, 'User Lookup time': None, 'Dot1x':None, 'Requests in request tree': None, 'Domain':None, 'Authenticated':None, 'User Authentication Time':None, 'Policy Evaluation time':None, 'Request Processing time':None}
def f1(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    dict_of_dict[mo.group(1)]['Start_time']=series['Time']

def f2(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    mo1 = f2_ro1.search(series['Message'])
    dict_of_dict[mo.group(1)]['Service Categorization time'] = mo1.group(1)

def f3(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    mo1 = f3_ro1.search(series['Message'])
    dict_of_dict[mo.group(1)]['Service'] = mo1.group(1)

def f4(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    mo1 = f4_ro1.search(series['Message'])
    dict_of_dict[mo.group(1)]['Username'] = mo1.group(1)
    dict_of_dict[mo.group(1)]['Auth Source'] = mo1.group(2)

def f5(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    mo1 = f5_ro1.search(series['Message'])
    dict_of_dict[mo.group(1)]['User Lookup time'] = mo1.group(1)

def f6(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    mo1 = f6_ro1.search(series['Message'])
    if mo1 is not None:
        dict_of_dict[mo.group(1)]['Dot1x'] = True
    else:
        dict_of_dict[mo.group(1)]['Dot1x'] = False

def f7(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    mo1 = f7_ro1.search(series['Message'])
    dict_of_dict[mo.group(1)]['Requests in request tree'] = mo1.group(1)

def f8(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    mo1 = f8_ro1.search(series['Message'])
    dict_of_dict[mo.group(1)]['Domain'] = mo1.group(1)

def f9(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    mo1 = f9_ro1.search(series['Message'])
    if mo1 is not None:
        dict_of_dict[mo.group(1)]['Authenticated'] = True
    else:
        dict_of_dict[mo.group(1)]['Authenticated'] = False

def f10(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    mo1 = f10_ro1.search(series['Message'])
    dict_of_dict[mo.group(1)]['User Authentication Time'] = mo1.group(1)

def f11(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    mo1 = f11_ro1.search(series['Message'])
    dict_of_dict[mo.group(1)]['Policy Evaluation time'] = mo1.group(1)

def f12(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), empty_dict)
    mo1 = f12_ro1.search(series['Message'])
    dict_of_dict[mo.group(1)]['Request Processing time'] = mo1.group(1)


def value_extraction(start_index, end_index):
    for index in df_radius.index[start_index:end_index]:
        # def value_extraction():
        #     for index in df_radius.index:
        if ' SessId ' in df_radius['Thread/RequestNo./SessionID'][index]:
            for item in list_of_items_to_check:
                if item in df_radius['Message'][index]:
                    list_of_items_to_check[item](df_radius.iloc[index])

session_id_to_timestamps = {} # session id as key and timestamps as the list items.
#list_of_items_to_check = ['Starting Service Categorization', 'Service Categorization time ', 'The request has been categorized into service', 'found user', 'User lookup time',  'rlm_eap_peap: Initiate', 'No.of requests in request processing tree', 'authenticating user', 'authenticated successfully', 'User Authentication time', 'Policy Evaluation time', 'Enforcement Profile', 'Request processing time' ]
#list_of_items_to_check = {'Starting Service Categorization': f1, 'Service Categorization time': f2, 'The request has been categorized into service':f3, 'found user':f4, 'User lookup time':f5,  'rlm_eap_peap: Initiate':f6, 'No.of requests in request processing tree':f7, 'authenticating user':f8, 'authenticated successfully':f9, 'User Authentication time':f10, 'Policy Evaluation time':f11, 'Enforcement Profile':f12, 'Request processing time':f13 }
if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        dict_of_dict = manager.dict()

        list_of_items_to_check = {'Starting Service Categorization':f1, 'Service Categorization time': f2, 'The request has been categorized into service': f3, 'found user': f4, 'User lookup time':f5, 'rlm_eap_peap: Initiate':f6, 'No.of requests in request processing tree':f7, 'authenticating user':f8, 'authenticated successfully':f9, 'User Authentication time':f10, 'Policy Evaluation time':f11, 'Request processing time':f12}

        f1_ro1 = re.compile(r'.*SessId (.*)')
        f2_ro1 = re.compile(r'Service Categorization time = (.*)ms')
        f3_ro1 = re.compile(r'.*The request has been categorized into service (.*)')
        f4_ro1 = re.compile(r'.*user(.*) in (.*)')
        f5_ro1 = re.compile(r'.*= (.*)ms')
        f6_ro1 = re.compile(r'eap_peap')
        f7_ro1 = re.compile(r'No.of requests in request processing tree: (.*)')
        f8_ro1 = re.compile(r'.*user .*, domain (.*)')
        f9_ro1 = re.compile(r'.*authenticated successfully')
        f10_ro1 = re.compile(r'.*= (.*)ms')
        f11_ro1 = re.compile(r'.*= (.*)ms')
        f12_ro1 = re.compile(r'.*= (.*)ms')


        lines =  len(df_radius)
        print(lines)
        repeater = int(lines / 4)

        processes = []

        for i in range(1,5):
            if i == 1:
                start_index = i
                end_index = repeater + int(1)
                p = multiprocessing.Process(target=value_extraction, args= (start_index, end_index))
                p.start()
                print(f'Parent Pid: {os.getppid()}')
                print(f'Child process pid : {os.getpid()}')
                processes.append(p)
            elif i != 4:
                start_index = end_index
                end_index = repeater * i + 1
                p = multiprocessing.Process(target=value_extraction, args= (start_index, end_index))
                p.start()
                print(f'Parent Pid: {os.getppid()}')
                print(f'Child process pid : {os.getpid()}')
                processes.append(p)
            else:
                start_index = end_index
                end_index = lines
                p = multiprocessing.Process(target=value_extraction, args=(start_index, end_index))
                p.start()
                print(f'Parent Pid: {os.getppid()}')
                print(f'Child process pid : {os.getpid()}')
                processes.append(p)
        print(processes)
        for process in enumerate(processes):
            process[1].join()
            print(f'Printing {process[1]} join {process[1].join()}')

        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     result = executor.submit(value_extraction)

        end = dt.datetime.now()

        pprint.pprint(dict_of_dict)
        df = pd.DataFrame(dict_of_dict).T
        print(f'Total time taken: {end - start}')