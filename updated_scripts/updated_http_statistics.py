
import os
import sys
import pandas as pd
import subprocess

# define a function to find the start and end time
#start_time would be first line of last file
#end_time would be last line of first file

def start_and_end_time(file_list):
    end_time = subprocess.check_output(['tail', '-1', file_list[0]]).decode('utf8').split(',')[1]
    start_time = subprocess.check_output(['head', '-1', file_list[-1]]).decode('utf8').split(',')[1]
    return end_time, start_time

# finding the list of files present in the http folder.
# no. of http, ssl files and corresponding csv files as lists.
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

'''
generating / skipping the generation of csv files for each ssl and http_access files.

'''

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

pd.options.display.max_rows = 120000
pd.options.display.max_colwidth = 10000
pd.set_option('display.max_columns', 30)

columns = ['IP address','Date and Time','HTTP Methods', 'Time taken', 'URL', 'HTTP']

http_files, http_ssl_files, http_ssl_csv, http_csv = http_folder_files('/Users/vinayreddy/Desktop/logs/gregory-server-performance/')
http_ssl_csv.sort()

# Generation of dataframe names
df = ['dframe'+str(i) for i in range(len(http_ssl_csv))]
list_of_dfs = {}
# Zipping the df and ssl_csv files
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

date = concated.sort_values(by=['Date and Time'], ascending=False)

# SSL -- concated files sorted by highest time taken (b)
b = concated.sort_values(by=['Time taken'], ascending=False)
#print(b)

# SSL -- URL to count (c_count)
series = b['URL']
c = series.value_counts(sort=True).to_frame()
c.reset_index(inplace=True)
c_count = c.rename(columns={'index': 'URL', 'URL':'Count'})
#print(c_count[:30])
# print('=======o=======')
# print(c_count[~c_count['URL'].str.contains("battery/")][:30])
# print('=======o=======')

# SSL -- IP to count (ip_series_count)
ip_series = b['IP address'].value_counts(sort=True).to_frame()

ip_series.reset_index(inplace=True)
ip_series_count = ip_series.rename(columns={'index': 'IP address', 'IP address': 'Count'})
#print(ip_series_count)

#============ need to add this ========


concated_http = pd.concat(list_to_cat_http, ignore_index=True )

# HTTP -- concated files sorted by highest time taken (b_http)
b_http = concated_http.sort_values(by=['Time taken'], ascending=False)

#print(b_http[:500])

# HTTP -- URL to count (c_http_count)
series_http = b_http['URL']

c_http = series_http.value_counts(sort=True).to_frame()
c_http.reset_index(inplace=True)
c_http_count = c_http.rename(columns={'index': 'URL', 'URL':'Count'})
#print(c_http_count[:30])

# HTTP -- IP to count (ip_series_count_http)

ip_series_http = b_http['IP address'].value_counts(sort=True).to_frame()

ip_series_http.reset_index(inplace=True)
ip_series_count_http = ip_series_http.rename(columns={'index': 'IP address', 'IP address': 'Count'})
print(ip_series_count_http)


# function with parameter as IP address and returns all the http requests done by that IP.

# def http_requests_per_ip(ip_address):
#     req_per_ip = b.loc[b['IP address'] == ip_address]
#     return req_per_ip
#
# req_per_ip =http_requests_per_ip('10.147.243.37')
# print(req_per_ip)


ssl_end_time, ssl_start_time = start_and_end_time(http_ssl_csv)

http_end_time, http_start_time = start_and_end_time(http_csv)

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
Issues fixed:

1. 'ValueError: No objects to concatenate' when you run the script for the first time. (Fixed)
2.  Fixed csv files size increasing issue every time we run the script. Now, csv files gets created first time you run the script and will not increase every time you run the script.
3.  fixed start and end time issue
4.  fixed the wrong index on URL - count


'''
# print('end time http:', http_end_time)
# print('start time http:', http_start_time)
# print('end time SSL:', ssl_end_time)
# print('start time SSL:', ssl_start_time)