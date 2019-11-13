

import re
import csv
import os

#regex_object=re.compile(r'([\d -:]*(PM|AM))\n(.*?)load average: ([\d .,]*)')

regex_object = re.compile(r'([\d -:]+(PM|AM))\n(.*?)load average: ([\d .,]+)\n.*\n([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+ .*id, ([\d. ]+)wa)')

def system_load_monitor_folder_files(path):
    system_load_files = []
    system_load_files_csv = []
    for f, sf, files in os.walk(path):
        if '/PolicyManagerLogs/system-load-monitor' in f:
            for file in files:
                if 'csv' in file and 'system' in file:
                    system_load_files_csv.append(f+'/'+file)
                elif 'system-load' in file and 'csv' not in file:
                    system_load_files.append(f+'/'+file)
            return system_load_files, system_load_files_csv

system_load_files, system_load_files_csv = system_load_monitor_folder_files('/Users/vinayreddy/Desktop/logs/gregory-server-performance/')

print(system_load_files)
print(system_load_files_csv)



if len(system_load_files_csv) == 0 :
    for i in range(len(system_load_files)):

        fh = open(system_load_files[i] +'_csv'+'.'+ str(i), 'a')
        with open(system_load_files[i], 'r') as fh2:
            a = fh2.read()
            b = regex_object.findall(a)
            for i in range(len(b)):
                fh.write(b[i][0] + ',' + b[i][3] + ',' + b[i][5] + ',' + b[i][6] + ',' + b[i][7] + '\n')
        fh.close()

time=[]
one_min_load_avg = []
five_min_load_avg = []
fifteen_min_load_avg = []
cpu_us = []
cpu_sy = []






#
# with open('/Users/vinayreddy/Desktop/logs/project_load_plotting/a.log', 'r') as file:
#     a= file.read()
#     b=regex_object.findall(a)
#
# with open('/Users/vinayreddy/Desktop/logs/project_load_plotting/csv.csv','w' ) as fh:
#     for i in range(len(b)):
#         fh.write(b[i][0]+', '+ b[i][3]+'\n')


