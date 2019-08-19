
import os
import sys
import pandas as pd

# extract the ssl_access_logs and access_logs

# ssl_access_logs_list = []
# access_logs_list = []

# function to get all the files in httpd folder.
def http_folder_files(path):
    for f, sf, files in os.walk(path):
        if '/SystemLogs/var/log/httpd' in f:
            return files

def http_files(files):
    http_files = []
    for item in files:
        if 'access' in item:
            http_files.append(item)



print(ssl_access_logs_list)
print(access_logs_list)

# Generating the csv files for the ssl

for i in range(len(ssl_access_logs_list)):

    fh2 = open(ssl_access_logs_list[i]+'_csv', 'a')      #fh2 = open('./')
    with open(ssl_access_logs_list[i], 'r') as fh:
        for line in fh:
            line = line.strip()
            a = line.split()
            fh2.write(a[0] + ',' + a[3].split('[')[1]+','+ a[5].split('"')[1] + ',' + a[-1].split('µ')[0] +',' + a[6]+','+ a[7].split('"')[0] + '\n')
    fh2.close()
pd.options.display.max_rows = 1200
pd.options.display.max_colwidth = 1000
columns = ['IP address','Date and Time','HTTP Methods', 'Time taken', 'URL', 'HTTP']

http_csv_files = []
for f, sf, files in os.walk('/Users/vinayreddy/Desktop/logs/gregory-server-performance/'):
    if '/SystemLogs/var/log/httpd' in f:
        for file in files:
            if 'csv' in file:
                http_csv_files.append(file)

http_csv_files.sort()
print(http_csv_files)

for file in http_csv_files:
    df



'''
steps:

1. extract the file paths
2. create csv of all the files
3. combine the appropriate csv files.


           if 'csv' in file:
                ssl_access_logs_list = []
                access_logs_list = []
                break
            if file.startswith('ssl_access_log'):
                ssl_access_logs_list.append(f+'/'+file)
            if file.startswith('access_log'):
                access_logs_list.append(f+'/' +  file)
        break
        
        path = /Users/vinayreddy/Desktop/logs/gregory-server-performance/

'''