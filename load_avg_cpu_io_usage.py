

import re
import csv
import os

#regex_object=re.compile(r'([\d -:]*(PM|AM))\n(.*?)load average: ([\d .,]*)')

regex_object = re.compile(r'([\d -:]+(PM|AM))\n(.*?)load average: ([\d .]+),([\d .]+),([\d .]+)\n.*\n([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+ .*id, ([\d. ]+)wa)')

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

time=[]
one_min_load_avg = []
five_min_load_avg = []
fifteen_min_load_avg = []
cpu_us = []
cpu_sy = []
io = []
if len(system_load_files_csv) == 0 :
    for i in range(len(system_load_files)):

        with open(system_load_files[i], 'r') as fh2:
            a = fh2.read()
            b = regex_object.findall(a)
            for i in range(len(b)):
                time.append(b[i][0])
                one_min_load_avg.append(b[i][3].strip())
                five_min_load_avg.append(b[i][4].strip())
                fifteen_min_load_avg.append(b[i][5].strip())
                cpu_us.append(b[i][7].strip())
                cpu_sy.append(b[i][8].strip())
                io.append(b[i][9].strip())

            # for i in range(len(b)):
            #
            #     fh.write(b[i][0] + ',' + b[i][3] + ',' + b[i][5] + ',' + b[i][6] + ',' + b[i][7] + '\n')

print(time)
print(one_min_load_avg)
print(five_min_load_avg)
print(fifteen_min_load_avg)
print(cpu_sy)
print(cpu_us)
print(io)

