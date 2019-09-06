
import os
import sys
import pandas as pd



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

http_files, http_ssl_files, http_ssl_csv, http_csv = http_folder_files('/Users/vinayreddy/Desktop/logs/gregory-server-performance/')
http_ssl_csv.sort()

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


pd.options.display.max_rows = 1200
pd.options.display.max_colwidth = 1000
columns = ['IP address','Date and Time','HTTP Methods', 'Time taken', 'URL', 'HTTP']



http_files, http_ssl_files, http_ssl_csv, http_csv = http_folder_files('/Users/vinayreddy/Desktop/logs/gregory-server-performance/')
http_ssl_csv.sort()

#==========
df = ['dframe'+str(i) for i in range(len(http_ssl_csv))]
list_of_dfs = {}
for dfra, file in zip(df, http_ssl_csv):
    list_of_dfs[dfra] = pd.read_csv(file, names = columns, header=None)

list_to_cat = []
for i in range(len(df)):
    df[i] = list_of_dfs[df[i]]
    list_to_cat.append(df[i])

#==========  need to add this ===>
df_http = ['dframe_http'+str(i) for i in range(len(http_csv))]
list_of_dfs_http = {}
for dfra, file in zip(df_http, http_csv):
    list_of_dfs_http[dfra] = pd.read_csv(file, names = columns, header=None)

list_to_cat_http = []
for i in range(len(df_http)):
    df_http[i] = list_of_dfs_http[df_http[i]]
    list_to_cat_http.append(df_http[i])

#==========

concated = pd.concat(list_to_cat, ignore_index=True)

end_time = concated['Date and Time'][0]
start_time = concated['Date and Time'].tail(1)


b = concated.sort_values(by=['Time taken'], ascending=False)
print(b)

series = b['URL']
c = series.value_counts(sort=True).to_frame()
print(c[:30])

ip_series = b['IP address'].value_counts(sort=True).to_frame()

ip_series.reset_index(inplace=True)
ip_series_count = ip_series.rename(columns={'index': 'IP address', 'IP address': 'Count'})
print(ip_series_count)

#============ need to add this ========


concated_http = pd.concat(list_to_cat_http, ignore_index=True)

end_time_http = concated_http['Date and Time'][0]
start_time_http = concated_http['Date and Time'].tail(1)


b_http = concated_http.sort_values(by=['Time taken'], ascending=False)
print(b_http)

series_http = b_http['URL']

c_http = series.value_counts(sort=True).to_frame()
print(c_http[:30])



ip_series = b_http['IP address'].value_counts(sort=True).to_frame()

ip_series.reset_index(inplace=True)
ip_series_count = ip_series.rename(columns={'index': 'IP address', 'IP address': 'Count'})
print(ip_series_count)


# function with parameter as IP address and returns all the http requests done by that IP.

# def http_requests_per_ip(ip_address):
#     req_per_ip = b.loc[b['IP address'] == ip_address]
#     return req_per_ip
#
# req_per_ip =http_requests_per_ip('10.147.243.37')
# print(req_per_ip)


'''
    To-Do in this:
    
        1. Use regex to generate the csv not split method.      (NOt done yet)
        2. 
'''
'''
Requirements:
1. Filter based on response times   (done)
2. URLs -- count                    (done)
3. IP address -- No. of requests    (done)
4. IP address -- URLs by that IP.   (partially done)
5. If the script is run already, it should not redo every thing if we run again.    (made it considerably faster)
6. Fix the http_csv file also       (done)
7. Comment the code wherever you can.

'''
'''
Issues:

1. 'ValueError: No objects to concatenate' when you run the script for the first time. (Fixed)
2.  Fixed csv files size increasing issue everytime we run the script. Now, csv files gets created first time you run the script and will not increase everytime you run the script.

'''