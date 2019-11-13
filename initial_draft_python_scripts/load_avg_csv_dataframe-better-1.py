

import re
import csv
import os, sys
import pandas as pd

#regex_object=re.compile(r'([\d -:]*(PM|AM))\n(.*?)load average: ([\d .,]*)')
#
# regex_object = re.compile(r'(([\d -:]+(PM|AM))\n(.*?)load average: ([\d .]+),([\d .]+),([\d .]+)\n.*\n([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+ .*id, ([\d. ]+)wa))')
# regex_ob_first_pattern = re.compile(r'([\d -:]+(PM|AM))')
# regex_ob_second_pattern = re.compile(r'([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+ .*id, ([\d. ]+)wa)')
ro = re.compile(r'(([\d -:]+(PM|AM))\n(.*?load average: ([\d .]+),([\d .]+),([\d .]+))\n.*\n([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+([\d. ]+)ni, ([\d. ]+)id, ([\d. ]+)wa, ([\d. ]+)hi, ([\d. ]+)si, ([\d. ]+)st)\n(KiB Mem : ([\d ]+)total,([\d ]+)free,([\d ]+)used,([\d ]+)buff/cache)\n(KiB Swap:([\d ]+)total,([\d ]+)free,([\d ]+)used.([\d ]+)avail Mem))')


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


if len(system_load_files_csv) == 0 :
    for j in range(len(system_load_files)):
        with open( system_load_files[j], 'r') as fh:
            a= fh.read()
            b = re.split('\n\s*\n', a)
            c = [ i for i in b if '%Cpu(s)' in i]
#            with open(system_load_files[j] +'_csv_'+ str(j), 'w' ) as fh2:
            with open( system_load_files_folder + '/system-load-csv' ,'a' ) as fh2:
                csv_fh = csv.writer(fh2)
                for i in c:
                    d = ro.search(i)
                    csv_fh.writerow([d[2].strip(), d[5].strip(), d[6].strip(), d[7].strip(), d[9].strip(), d[10].strip(), d[11].strip(), d[12].strip(), d[13].strip(), d[14].strip(),d[15].strip(), d[16].strip(), d[18].strip(), d[19].strip(), d[20].strip(), d[21].strip(), d[23].strip(), d[24].strip(), d[25].strip(),d[26].strip()])

columns = ['Date-Time', '1 Min load avg', '5 Min load avg', '15 Min load avg', 'us', 'sy', 'ni', 'id','wa', 'hi', 'si', 'st', 'KiB Memory-Total', 'KiB Memory-free', 'KiB Memory-used', 'KiB Memory-Buff/Cache', 'KiB Swap-total', 'KiB Swap-free', 'KiB Swap-used', 'KiB Swap-available-Mem']
df = pd.read_csv(system_load_files_folder + '/system-load-csv', names=columns,  header=None)
# df['KiB Swap-available-Mem'] = df['KiB Swap-available-Mem'].astype(int)

print(len(columns))






'''

regex:

(([\d -:]+(PM|AM))\n(.*?load average: ([\d .]+),([\d .]+),([\d .]+))\n.*\n([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+([\d. ]+)ni, ([\d. ]+)id, ([\d. ]+)wa, ([\d. ]+)hi, ([\d. ]+)si, ([\d. ]+)st)\n(KiB Mem : ([\d ]+)total,([\d ]+)free,([\d ]+)used,([\d ]+)buff/cache)\n(KiB Swap:([\d ]+)total,([\d ]+)free,([\d ]+)used.([\d ]+)avail Mem))


postgres: appadmin tipsLogDb 127.0.0.1(58686) idle
31754 postgres 20 0 2294604 5348 3884 S 0.0 0.1 0:00.00 postgres: appuser tipsdb [local] idle
31863 root 20 0 0 0 0 S 0.0 0.0 0:00.00 [kworker/u16:1]

06-26-19 08:23:38 PM
top - 20:23:38 up 62 days, 5:59, 0 users, load average: 2.89, 2.41, 2.06
Tasks: 325 total, 1 running, 324 sleeping, 0 stopped, 0 zombie
%Cpu(s): 7.3 us, 4.8 sy, 0.0 ni, 80.3 id, 7.4 wa, 0.0 hi, 0.2 si, 0.0 st
KiB Mem : 8009232 total, 140608 free, 4208120 used, 3660504 buff/cache
KiB Swap: 3071996 total, 0 free, 3071996 used. 1377344 avail Mem

PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
4084 appuser 20 0 5017464 156512 5900 S 7.9 2.0 20827:23 /usr/local/avenda/tips/sbin/policy_server
5256 root 20 0 12812 36 0 S 3.6 


Match 1
1.	06-26-19 08:23:38 PM top - 20:23:38 up 62 days, 5:59, 0 users, load average: 2.89, 2.41, 2.06 Tasks: 325 total, 1 running, 324 sleeping, 0 stopped, 0 zombie %Cpu(s): 7.3 us, 4.8 sy, 0.0 ni, 80.3 id, 7.4 wa, 0.0 hi, 0.2 si, 0.0 st KiB Mem : 8009232 total, 140608 free, 4208120 used, 3660504 buff/cache KiB Swap: 3071996 total, 0 free, 3071996 used. 1377344 avail Mem
2.	06-26-19 08:23:38 PM
3.	PM
4.	top - 20:23:38 up 62 days, 5:59, 0 users, load average: 2.89, 2.41, 2.06
5.	2.89
6.	2.41
7.	2.06
8.	%Cpu(s): 7.3 us, 4.8 sy, 0.0 ni, 80.3 id, 7.4 wa, 0.0 hi, 0.2 si, 0.0 st
9.	7.3
10.	4.8
11.	0.0
12.	80.3
13.	7.4
14.	0.0
15.	0.2
16.	0.0
17.	KiB Mem : 8009232 total, 140608 free, 4208120 used, 3660504 buff/cache
18.	8009232
19.	140608
20.	4208120
21.	3660504
22.	KiB Swap: 3071996 total, 0 free, 3071996 used. 1377344 avail Mem
23.	3071996
24.	0
25.	3071996
26.	1377344 

'''