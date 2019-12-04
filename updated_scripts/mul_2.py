import pandas as pd
import csv, re
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
path = '/testing/tmpF3p6JB/PolicyManagerLogs/tips-radius-server/'
columns_radius = ['Time', 'drop', 'Thread/RequestNo./SessionID', 'Level','Module', 'Message']

a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10, a_11, a_12 = [multiprocessing.Manager().list() for i in range(1, 13)]

main_loop = []
main_loop_2  = []

df_radius = pd.read_csv('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/PolicyManagerLogs/tips-radius-server/test.csv', names=columns_radius)

def f1(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    #    dict_of_dict[mo.group(1)]['Start_time']=series['Time']
    a = dict_of_dict[mo.group(1)]
    a['Start_time'] = series['Time']
    # dict_of_dict[mo.group(1)] = a
    s7 = dt.datetime.now()
    a_1.append(s7 - s6)

def f2(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    mo1 = f2_ro1.search(series['Message'])
    #    dict_of_dict[mo.group(1)]['Service Categorization time'] = mo1.group(1)
    a = dict_of_dict[mo.group(1)]
    a['Service Categorization time'] = mo1.group(1)
    dict_of_dict[mo.group(1)] = a
    #dict_of_dict[mo.group(1)] = mo1.group(1)
    s7 = dt.datetime.now()
    a_2.append(s7 - s6)
def f3(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    mo1 = f3_ro1.search(series['Message'])
    #    dict_of_dict[mo.group(1)]['Service'] = mo1.group(1)
    a = dict_of_dict[mo.group(1)]
    a['Service'] = mo1.group(1)
    #dict_of_dict[mo.group(1)] = a
    s7 = dt.datetime.now()
    a_3.append(s7 - s6)
def f4(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    mo1 = f4_ro1.search(series['Message'])
    #    dict_of_dict[mo.group(1)]['Username'] = mo1.group(1)
    #    dict_of_dict[mo.group(1)]['Auth Source'] = mo1.group(2)
    a = dict_of_dict[mo.group(1)]
    a['Username'] = mo1.group(1)
    a['Auth Source'] = mo1.group(2)
    #dict_of_dict[mo.group(1)] = a
    s7 = dt.datetime.now()
    a_4.append(s7 - s6)

def f5(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    mo1 = f5_ro1.search(series['Message'])
    a = dict_of_dict[mo.group(1)]
    a['User Lookup time'] = mo1.group(1)
    #dict_of_dict[mo.group(1)] = a
#    dict_of_dict[mo.group(1)]['User Lookup time'] = mo1.group(1)
    s7 = dt.datetime.now()
    a_5.append(s7 - s6)

def f6(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    mo1 = f6_ro1.search(series['Message'])
    if mo1 is not None:
        a = dict_of_dict[mo.group(1)]
        a['Dot1x'] = True
        #dict_of_dict[mo.group(1)] = a
    else:
        a = dict_of_dict[mo.group(1)]
        a['Dot1x'] = False
        #dict_of_dict[mo.group(1)] = a
#        dict_of_dict[mo.group(1)]['Dot1x'] = False
    s7 = dt.datetime.now()
    a_6.append(s7 - s6)

def f7(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    mo1 = f7_ro1.search(series['Message'])
    #    dict_of_dict[mo.group(1)]['Requests in request tree'] = mo1.group(1)
    a = dict_of_dict[mo.group(1)]
    a['Requests in request tree'] = mo1.group(1)
    #dict_of_dict[mo.group(1)] = a
    s7 = dt.datetime.now()
    a_7.append(s7 - s6)

def f8(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    mo1 = f8_ro1.search(series['Message'])
    #    print(mo1.group(1))
    #    dict_of_dict[mo.group(1)]['Domain'] = mo1.group(1)
    a = dict_of_dict[mo.group(1)]
    a['Domain'] = mo1.group(1)
    #dict_of_dict[mo.group(1)] = a
    s7 = dt.datetime.now()
    a_8.append(s7 - s6)

def f9(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    mo1 = f9_ro1.search(series['Message'])
    if mo1 is not None:
        a = dict_of_dict[mo.group(1)]
        a['Authenticated'] = True
        #dict_of_dict[mo.group(1)] = a
    else:
        a = dict_of_dict[mo.group(1)]
        a['Authenticated'] = False
        #dict_of_dict[mo.group(1)] = a
#        dict_of_dict[mo.group(1)]['Authenticated'] = False
    s7 = dt.datetime.now()
    a_9.append(s7 - s6)

def f10(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    mo1 = f10_ro1.search(series['Message'])
    a = dict_of_dict[mo.group(1)]
    a['User Authentication Time'] = mo1.group(1)
    #dict_of_dict[mo.group(1)] = a
#    dict_of_dict[mo.group(1)]['User Authentication Time'] = mo1.group(1)
    s7 = dt.datetime.now()
    a_10.append(s7 - s6)

def f11(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    mo1 = f11_ro1.search(series['Message'])
    a = dict_of_dict[mo.group(1)]
    a['Policy Evaluation time'] = mo1.group(1)
    #dict_of_dict[mo.group(1)] = a
#    dict_of_dict[mo.group(1)]['Policy Evaluation time'] = mo1.group(1)
    s7 = dt.datetime.now()
    a_11.append(s7 - s6)

def f12(series):
    s6 = dt.datetime.now()
    mo = f1_ro1.search(series['Thread/RequestNo./SessionID'])
    dict_of_dict.setdefault(mo.group(1), manager.dict())
    mo1 = f12_ro1.search(series['Message'])
    a = dict_of_dict[mo.group(1)]
    a['Request Processing time'] = mo1.group(1)
    #dict_of_dict[mo.group(1)] = a
#    print(dict_of_dict[mo.group(1)]['Request Processing time'])
    s7 = dt.datetime.now()
    a_12.append(s7 - s6)



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

def value_extraction(start_index, end_index, dict_of_dict):
    s10 = dt.datetime.now()
    for index in df_radius.index[start_index:end_index]:
        s11 = dt.datetime.now()
        main_loop.append(s11-s10)
        # def value_extraction():
        #     for index in df_radius.index:
        if ' SessId ' in df_radius['Thread/RequestNo./SessionID'][index]:                   #we can completely remove this check by filtering lines out based on
            for item in list_of_items_to_check:
                if item in df_radius['Message'][index]:
                    list_of_items_to_check[item](df_radius.iloc[index])


processes = []
if __name__ == '__main__':
    manager = multiprocessing.Manager()
    dict_of_dict = manager.dict()

    lines =  len(df_radius)
    print(lines)
    repeater = int(lines /24)
    s1 = dt.datetime.now()
    print(f'From import to start of for loop which contains process creation: {s1 - start}')
    for i in range(1,25):
        if i == 1:
            start_index = i
            end_index = repeater + int(1)
            p = multiprocessing.Process(target=value_extraction, args= [start_index, end_index, dict_of_dict])
            p.start()
            processes.append(p)
        elif i != 24:
            start_index = end_index
            end_index = repeater * i + 1
            p = multiprocessing.Process(target=value_extraction, args= [start_index, end_index, dict_of_dict])
            p.start()
            processes.append(p)
        else:
            start_index = end_index
            end_index = -1
            p = multiprocessing.Process(target=value_extraction, args= [start_index, end_index, dict_of_dict])
            p.start()
            processes.append(p)
    s2 = dt.datetime.now()
    print(f'From the for loop which contains process creation to its end: {s2 - s1}')
    for process in processes:
        process.join()
    s3 = dt.datetime.now()
    print(f'From end of process creation to the join: {s3-s2}')
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     result = executor.submit(value_extraction)

    end = dt.datetime.now()
    pd.options.display.max_columns = 15
    #pprint.pprint(dict_of_dict)
    s4 = dt.datetime.now()
    for key, value in dict_of_dict.items():
        dict_of_dict[key] = dict(value)
    s5 = dt.datetime.now()
    print(f'Time taken to convert inner dict proxy to dictionary : {s5-s4}')
    df = pd.DataFrame(dict(dict_of_dict)).T
    print(f'Time taken to create the dataframe and transpose it: {s5 - dt.datetime.now()}')
    print(df)
    #print(f'Total time taken: {end - start}')
    for i in [a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10, a_11, a_12]:
        print(i)
    print('Time taken: ', end - start)




