

import re
import csv
import os, sys
import pandas as pd

#regex_object=re.compile(r'([\d -:]*(PM|AM))\n(.*?)load average: ([\d .,]*)')

# regex_object = re.compile(r'(([\d -:]+(PM|AM))\n(.*?)load average: ([\d .]+),([\d .]+),([\d .]+)\n.*\n([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+ .*id, ([\d. ]+)wa))')
# regex_ob_first_pattern = re.compile(r'([\d -:]+(PM|AM))')
# regex_ob_second_pattern = re.compile(r'([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+ .*id, ([\d. ]+)wa)')
ro = re.compile(r'(([\d -:]+(PM|AM))\n(.*?load average: ([\d .]+),([\d .]+),([\d .]+))\n.*\n([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+ .*id, ([\d. ]+)wa, ([\d. ]+)hi, ([\d. ]+)si, ([\d. ]+)st)\n(KiB Mem : ([\d ]+)total,([\d ]+)free,([\d ]+)used,([\d ]+)buff/cache)\n(KiB Swap:([\d ]+)total,([\d ]+)free,([\d ]+)used.([\d ]+)avail Mem))')


def system_load_monitor_folder_files(path):
    system_load_files = []
    system_load_files_csv = []
    for f, sf, files in os.walk(path):
        if '/PolicyManagerLogs/system-load-monitor' in f:
            for file in files:
                if file == 'system-load-csv':
                    system_load_files_csv.append(f+'/'+file)
                elif 'system-load' in file:
                    system_load_files.append(f+'/'+file)

            return system_load_files, system_load_files_csv, f

system_load_files, system_load_files_csv, system_load_files_folder = system_load_monitor_folder_files('/Users/vinayreddy/Desktop/logs/gregory-server-performance/')

# print(system_load_files)
# print(system_load_files_csv)
# print(system_load_files_folder)

#
# if len(system_load_files_csv) == 0 :
#     for j in range(len(system_load_files)):
#         with open( system_load_files[j], 'r') as fh:
#             a= fh.read()
#             b = re.split('\n\s*\n', a)
#             c = [ i for i in b if '%Cpu(s)' in i]
#             #            with open(system_load_files[j] +'_csv_'+ str(j), 'w' ) as fh2:
#             with open( system_load_files_folder + '/system-load-csv' ,'a' ) as fh2:
#                 csv_fh = csv.writer(fh2)
#                 for i in c:
#                     d = regex_object.search(i)
#                     csv_fh.writerow([d[2].strip(), d[5].strip(), d[6].strip(), d[7].strip(), d[9].strip(), d[10].strip(), d[11].strip()])
#
# df = pd.read_csv(system_load_files_folder + '/system-load-csv',   header=None)

if len(system_load_files_csv) == 0 :
    for j in range(len(system_load_files)):
        with open( system_load_files[j], 'r') as fh:
            a = fh.read()
            b = ro.findall(a)
        print(b)
        print('=====================o=====================')
