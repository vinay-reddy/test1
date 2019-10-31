

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
    print('inside the function now')
    print(path)
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

system_load_files, system_load_files_csv, system_load_files_folder = system_load_monitor_folder_files('/Users/vinayreddy/Desktop/logs/gregory-server-performance')

print(system_load_files)
print(system_load_files_csv)
print(system_load_files_folder)


if len(system_load_files_csv) == 0 :
    for j in range(len(system_load_files)):
        with open( system_load_files[j], 'r') as fh:
            a= fh.read()
            b = re.split('\n\s*\n', a)
            c = [ i for i in b if 'load average:' in i]
            #            with open(system_load_files[j] +'_csv_'+ str(j), 'w' ) as fh2:
            with open( system_load_files_folder + '/system-load-csv' ,'a' ) as fh2:
                csv_fh = csv.writer(fh2)
                for i in c:
                    d = ro.search(i)
                    if d is not None:
                        csv_fh.writerow([d[2].strip(), d[5].strip(), d[6].strip(), d[7].strip(), d[9].strip(), d[10].strip(), d[11].strip(), d[12].strip(), d[13].strip(), d[14].strip(),d[15].strip(), d[16].strip(), d[18].strip(), d[19].strip(), d[20].strip(), d[21].strip(), d[23].strip(), d[24].strip(), d[25].strip(),d[26].strip()])
                    else:
                        print(i)
columns = ['Date-Time', '1 Min load avg', '5 Min load avg', '15 Min load avg', 'us', 'sy', 'ni', 'id','wa', 'hi', 'si', 'st', 'KiB Memory-Total', 'KiB Memory-free', 'KiB Memory-used', 'KiB Memory-Buff/Cache', 'KiB Swap-total', 'KiB Swap-free', 'KiB Swap-used', 'KiB Swap-available-Mem']
df = pd.read_csv(system_load_files_folder + '/system-load-csv', names=columns,  header=None)
# df['KiB Swap-available-Mem'] = df['KiB Swap-available-Mem'].astype(int)

print(len(columns))


# function to extract the between two timestamps

def systemLoadMonitorLinesExtract(time):
    for file in system_load_files:
        fh = open(file)
        file_read = fh.read()
        count=file_read.count(time)
        print('Count =', count)
        if count == 2:
            ro = re.compile(r'{}.*?{}.*?{}' .format(time, time, '\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]{2}'), re.DOTALL)
            mo = ro.search(file_read)
            if mo is not None:
                a = mo.group()
                return a
        elif count == 1:
            ro = re.compile(r'{}.*?{}' .format(time, '\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]{2}'), re.DOTALL)
            print(ro)
            mo = ro.search(file_read)
            if mo is not None:
                a = mo.group()
                return a
            else:
                print('You are in this else block')
                ro = re.compile(r'{}.*' .format(time), re.DOTALL)
                print(ro)
                mo = ro.search(file_read)
                if mo is not None:
                    a = mo.group()
                    return a
        elif count == 0:
            continue

extracted_text= systemLoadMonitorLinesExtract('06-29-19 03:43:06 PM')
print('extracted text is: ',extracted_text)

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

6.6.x

09-10-19 11:05:30 PM
top - 23:05:30 up 1 min,  0 users,  load average: 0.39, 0.13, 0.05
Tasks: 374 total,   2 running, 372 sleeping,   0 stopped,   0 zombie
Cpu(s):  0.6%us,  1.1%sy,  0.0%ni, 97.5%id,  0.8%wa,  0.0%hi,  0.0%si,  0.0%st
Mem:  32777112k total,   950376k used, 31826736k free,   103104k buffers
Swap:  3071996k total,        0k used,  3071996k free,   406012k cached

  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
 4127 root      20   0  186m  11m 3840 S 17.7  0.0   0:00.10 /usr/bin/python /usr/sbin/iotop -b -o -d 1800 -P -t
 3661 root      20   0 16820  508  360 S  7.9  0.0   0:00.47 jitterentropy-rngd -vvv -d -p /var/run/jitterentropy-rngd.pid
 4162 root      20   0  109m 1072  716 R  5.9  0.0   0:00.03 chown -R apache:apache /opt/amigopod/www
   73 root      20   0     0    0    0 S  2.0  0.0   0:00.33 [rcu_sched]
   85 root      20   0     0    0    0 S  2.0  0.0   0:00.02 [rcuos/11]
 3976 root      20   0  111m 1568 1304 S  2.0  0.0   0:00.01 /bin/sh /usr/local/avenda/platform/bin/run-onboot-tasks
 4128 root      20   0 21600 1480  920 R  2.0  0.0   0:00.01 top -b -c -d 120
    1 root      20   0 27744 1548 1252 S  0.0  0.0   0:01.42 /sbin/init
    
'''
'''
Issues to fix:
1. Breaks if python doesn't have permissions to access the files.
2. Breaks if file is not present. May be TAC didn't collect Policy Manager logs.
3. Breaks if run on 6.6.x logs as 'top c' output is different in two versions. Have to optimize the regex such that it works for both versions or display a message
that only works for 6.7 and above.
4. Handle the case when there are multiple system-load-monitor files.
5. Perform tests on             b = re.split('\n\s*\n', a).                         ==> works fine. No issues.
6. In case of multiple files, it is just appending the files one after the other. since system-load-monitor log file names don't end with a number but a date, it would be
difficult to order them. Fix it by sorting the dataframe by timestamp.

'''