

import re
import csv
import os, sys

#regex_object=re.compile(r'([\d -:]*(PM|AM))\n(.*?)load average: ([\d .,]*)')

regex_object = re.compile(r'(([\d -:]+(PM|AM))\n(.*?)load average: ([\d .]+),([\d .]+),([\d .]+)\n.*\n([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+ .*id, ([\d. ]+)wa))')
regex_ob_first_pattern = re.compile(r'([\d -:]+(PM|AM))')
regex_ob_second_pattern = re.compile(r'([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+ .*id, ([\d. ]+)wa)')


def system_load_monitor_folder_files(path):
    system_load_files = []
    system_load_files_csv = []
    for f, sf, files in os.walk(path):
        if '/PolicyManagerLogs/system-load-monitor' in f:
            for file in files:
                if 'system-load' in file:
                    system_load_files.append(f+'/'+file)
                elif 'csv' in files:
                    system_load_files_csv.append(f+'/'+file)
            return system_load_files, system_load_files_csv

system_load_files, system_load_files_csv = system_load_monitor_folder_files('/Users/vinayreddy/Desktop/logs/gregory-server-performance/')

print(system_load_files)
print(system_load_files_csv)


#

string = ''
listoflines = []

if len(system_load_files_csv) == 0 :
    for file in system_load_files:
        with open( file, 'r') as fh:
            firstPatternFound = None
            secondPatternFound = None
            for line in fh.readlines():
                b = regex_ob_first_pattern.search(line)
                c = regex_ob_second_pattern.search(line)
                if b is not None and firstPatternFound is None and secondPatternFound is None and c is None:
                    print(line)
                    firstPatternFound =1
                    string = string + line
                elif b is None and firstPatternFound == 1 and secondPatternFound is None and c is None:
                    string = string + line
                elif c is not None and firstPatternFound == 1:
                    string = string + line
                    listoflines.append(string)
                    string = ''
                    firstPatternFound = None
                    secondPatternFound = None
                    print('in the final block')
                    print(listoflines[:])
                    sys.exit()
                else:
                    continue
print(listoflines[:])


# time=[]
# one_min_load_avg = []
# five_min_load_avg = []
# fifteen_min_load_avg = []
# cpu_us = []
# cpu_sy = []
# io = []
#
# for i in range(len(system_load_files)):
#     with open(system_load_files[i], 'r') as fh2:
#         a = fh2.read()
#         b = regex_object.findall(a)
#         for i in range(len(b)):
#             time.append(b[i][0].strip())
#             one_min_load_avg.append(b[i][3].strip())
#             five_min_load_avg.append(b[i][4].strip())
#             fifteen_min_load_avg.append(b[i][5].strip())
#             cpu_us.append(b[i][7].strip())
#             cpu_sy.append(b[i][8].strip())
#             io.append(b[i][9].strip())
#
#             # for i in range(len(b)):
#             #
#             #     fh.write(b[i][0] + ',' + b[i][3] + ',' + b[i][5] + ',' + b[i][6] + ',' + b[i][7] + '\n')
#
# print(time)
# print(one_min_load_avg)
# print(five_min_load_avg)
# print(fifteen_min_load_avg)
# print(cpu_sy)
# print(cpu_us)
# print(io)
#
#
# print(len(time))
# print(len(one_min_load_avg))
# print(len(five_min_load_avg))
# print(len(fifteen_min_load_avg))
# print(len(cpu_sy))
# print(len(cpu_us))
# print(len(io))
