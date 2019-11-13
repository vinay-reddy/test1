
import os
import sys
import pandas as pd

# extract the ssl_access_logs and access_logs


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
# ssl_csv creation
    for i in range(len(http_ssl_files)):

        fh2 = open(os.path.dirname(http_ssl_files[i])+'/ssl_csv'+'.'+ str(i), 'a')      #fh2 = open('./')
        with open(http_ssl_files[i], 'r') as fh:
            for line in fh:
                line = line.strip()
                a = line.split()
                fh2.write(a[0] + ',' + a[3].split('[')[1]+','+ a[5].split('"')[1] + ',' + a[-1].split('µ')[0] +',' + a[6]+','+ a[7].split('"')[0] + '\n')
        fh2.close()

    # http_csv creation.
    for i in range(len(http_files)):

        fh2 = open(os.path.dirname(http_files[i])+'/http_csv'+'.'+ str(i), 'a')      #fh2 = open('./')
        with open(http_files[i], 'r') as fh:
            for line in fh:
                line = line.strip()
                a = line.split()
                fh2.write(a[0] + ',' + a[3].split('[')[1]+','+ a[5].split('"')[1] + ',' + a[-1].split('µ')[0] +',' + a[6]+','+ a[7].split('"')[0] + '\n')
        fh2.close()


pd.options.display.max_rows = 1200
pd.options.display.max_colwidth = 1000
columns = ['IP address','Date and Time','HTTP Methods', 'Time taken', 'URL', 'HTTP']

# Creating the dataframes variables for each csv file

http_files, http_ssl_files, http_ssl_csv, http_csv = http_folder_files('/Users/vinayreddy/Desktop/logs/gregory-server-performance/')
http_ssl_csv.sort()


df = ['dframe'+str(i) for i in range(len(http_ssl_csv))]                # list comprehension
#print('df print:', df)    ===> output =  df print: ['dframe0', 'dframe1', 'dframe2', 'dframe3']

# Zipping the df and ssl_csv files

# zipped = { dframe: ssl_csv for dframe, ssl_csv in zip(df, http_ssl_csv) }           # dict comprehension
# print('this is zipped:', zipped)
'''
this is zipped: {'dframe0': '/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/SystemLogs/var/log/httpd/ssl_csv.0', 'dframe1': '/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/SystemLogs/var/log/httpd/ssl_csv.1', 'dframe2': '/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/SystemLogs/var/log/httpd/ssl_csv.2', 'dframe3': '/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/SystemLogs/var/log/httpd/ssl_csv.3'}
'''

list_of_dfs = {}
for dfra, file in zip(df, http_ssl_csv):
    list_of_dfs[dfra] = pd.read_csv(file, names = columns, header=None)
#print('list of dfrs:', list_of_dfs)                           #======================= list of dfrs =================#
'''
list_of_dfs is a dictionary. 
list of dfrs: {'dframe0':           IP address  ...      HTTP
0         10.0.17.93  ...  HTTP/1.1
1         10.0.17.93  ...  HTTP/1.0
2         10.0.17.14  ...       302
3       172.31.8.228  ...       302
4      10.148.135.92  ...  HTTP/1.0
5         10.0.17.92  ...  HTTP/1.0
'''

#
list_to_cat = []
for i in range(len(df)):
    df[i] = list_of_dfs[df[i]]
    list_to_cat.append(df[i])

print('list to cat:', list_to_cat)                           #======================= list to cat ============== #
# joining the dfs and re-order

concated = pd.concat(list_to_cat, ignore_index=True)

end_time = concated['Date and Time'][0]
start_time = concated['Date and Time'].tail(1)
#


b = concated.sort_values(by=['Time taken'], ascending=False)

series = b['URL']

# URL - Count

c = series.value_counts(sort=True).to_frame()
print(c[:30])


print(http_files)
print(http_ssl_files)
print(http_ssl_csv)
print(http_csv)
print(df)
#print(zipped)
print(list_of_dfs['dframe0'].head())
print('end time: ',end_time)
print('start time:', start_time)

# print(type(dframe0))
# print(type(dframe1))
# print(type(dframe2))
# print(type(dframe3))




'''
    To-Do in this:
    
        1. Use regex to generate the csv not split method.
        2. 
'''
'''
Requirements:
1. Filter based on response times   (done)
2. URLs -- count
3. IP address -- No. of requests
4. IP address -- URLs by that IP.
5. If the script is run already, it should not redo every thing if we run again.    (made it considerably faster)
6. Fix the http_csv file also
7. Comment the code wherever you can.

'''
'''
Issues:

1. 'ValueError: No objects to concatenate' when you run the script for the first time. (Fixed)
2.  Fixed csv files size increasing issue everytime we run the script. Now, csv files gets created first time you run the script and will not increase everytime you run the script.

'''