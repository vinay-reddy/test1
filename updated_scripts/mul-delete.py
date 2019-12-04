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
    dict_of_dict.setdefault(mo.group(1), {})
#    dict_of_dict[mo.group(1)]['Start_time']=series['Time']
    a = dict_of_dict[mo.group(1)]
    a['Start_time'] = series['Time']
    dict_of_dict[mo.group(1)] = a

def f2(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), {})
    mo1 = f2_ro1.search(series['Message'])
#    dict_of_dict[mo.group(1)]['Service Categorization time'] = mo1.group(1)
    a = dict_of_dict[mo.group(1)]
    a['Service Categorization time'] = mo1.group(1)
    dict_of_dict[mo.group(1)] = a

def f3(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), {})
    mo1 = f3_ro1.search(series['Message'])
#    dict_of_dict[mo.group(1)]['Service'] = mo1.group(1)
    a = dict_of_dict[mo.group(1)]
    a['Service'] = mo1.group(1)
    dict_of_dict[mo.group(1)] = a

def f4(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), {})
    mo1 = f4_ro1.search(series['Message'])
#    dict_of_dict[mo.group(1)]['Username'] = mo1.group(1)
#    dict_of_dict[mo.group(1)]['Auth Source'] = mo1.group(2)
    a = dict_of_dict[mo.group(1)]
    a['Username'] = mo1.group(1)
    a['Auth Source'] = mo1.group(2)
    dict_of_dict[mo.group(1)] = a

def f5(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), {})
    mo1 = f5_ro1.search(series['Message'])
    a = dict_of_dict[mo.group(1)]
    a['User Lookup time'] = mo1.group(1)
    dict_of_dict[mo.group(1)] = a
#    dict_of_dict[mo.group(1)]['User Lookup time'] = mo1.group(1)

def f6(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), {})
    mo1 = f6_ro1.search(series['Message'])
    if mo1 is not None:
        a = dict_of_dict[mo.group(1)]
        a['Dot1x'] = True
        dict_of_dict[mo.group(1)] = a
    else:
        a = dict_of_dict[mo.group(1)]
        a['Dot1x'] = False
        dict_of_dict[mo.group(1)] = a
#        dict_of_dict[mo.group(1)]['Dot1x'] = False

def f7(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), {})
    mo1 = f7_ro1.search(series['Message'])
#    dict_of_dict[mo.group(1)]['Requests in request tree'] = mo1.group(1)
    a = dict_of_dict[mo.group(1)]
    a['Requests in request tree'] = mo1.group(1)
    dict_of_dict[mo.group(1)] = a

def f8(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), {})
    mo1 = f8_ro1.search(series['Message'])
#    print(mo1.group(1))
#    dict_of_dict[mo.group(1)]['Domain'] = mo1.group(1)
    a = dict_of_dict[mo.group(1)]
    a['Domain'] = mo1.group(1)
    dict_of_dict[mo.group(1)] = a

def f9(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), {})
    mo1 = f9_ro1.search(series['Message'])
    if mo1 is not None:
        a = dict_of_dict[mo.group(1)]
        a['Authenticated'] = True
        dict_of_dict[mo.group(1)] = a
    else:
        a = dict_of_dict[mo.group(1)]
        a['Authenticated'] = False
        dict_of_dict[mo.group(1)] = a
#        dict_of_dict[mo.group(1)]['Authenticated'] = False

def f10(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), {})
    mo1 = f10_ro1.search(series['Message'])
    a = dict_of_dict[mo.group(1)]
    a['User Authentication Time'] = mo1.group(1)
    dict_of_dict[mo.group(1)] = a
#    dict_of_dict[mo.group(1)]['User Authentication Time'] = mo1.group(1)

def f11(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), {})
    mo1 = f11_ro1.search(series['Message'])
    a = dict_of_dict[mo.group(1)]
    a['Policy Evaluation time'] = mo1.group(1)
    dict_of_dict[mo.group(1)] = a
#    dict_of_dict[mo.group(1)]['Policy Evaluation time'] = mo1.group(1)

def f12(series):
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
#    dict_of_dict.setdefault(mo.group(1), {})
    mo1 = f12_ro1.search(series['Message'])
    a = dict_of_dict[mo.group(1)]
    a['Request Processing time'] = mo1.group(1)
    dict_of_dict[mo.group(1)] = a
#    print(dict_of_dict[mo.group(1)]['Request Processing time'])




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

dict_of_dict = multiprocessing.Manager().dict()
dict_dummy = multiprocessing.Manager().dict()
start_index = 1
end_index = lines
p1 = multiprocessing.Process(target=value_extraction, args= (start_index, end_index))
# start_index = 50001
# end_index = 100001
# p2 = multiprocessing.Process(target=value_extraction, args= (start_index, end_index))
# start_index = 100001
# end_index = 150001
# p3 = multiprocessing.Process(target=value_extraction, args= (start_index, end_index))
# start_index = 150001
# end_index = lines
# p4 = multiprocessing.Process(target=value_extraction, args= (start_index, end_index))

p1.start()
# p2.start()
# p3.start()
# p4.start()
p1.join()
# p2.join()
# p3.join()
# p4.join()

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     result = executor.submit(value_extraction)

end = dt.datetime.now()

pprint.pprint(dict_of_dict)
df = pd.DataFrame(dict_of_dict).T
print(f'Total time taken: {end - start}')