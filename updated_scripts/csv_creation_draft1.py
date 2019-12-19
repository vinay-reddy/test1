import re, csv
import subprocess, os
import pprint
import operator
import pandas as pd
import datetime as dt
import concurrent.futures

start = dt.datetime.now()

reg_obj_smb = re.compile(r'^\[[\d/]+')
reg_obj2_smb = re.compile(r'([\d/ :.]+),\s+(\d),\s+pid=(\d+)\]\s+(.*)\n(.*)')
reg_obj3_smb = re.compile(r'\[([\d/ :.]+),\s+(\d),\s+pid=(\d+)\]\s+(.*?)\n(.*)',re.DOTALL)
reg_obj4_smb = re.compile(r'.*domain (.*) from .*')
reg_obj5_smb = re.compile(r'.*= (.*) ms')
reg_obj_policy = re.compile(r'(\d{4}(-\d{2}){2} [\d:,]+) \[(.*?)\] ([A-Z]+?)\s+(.*?) - (.*?)\n')
regexobj2_postgresql = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3,}) (\w+) (\w+) (\d+) .* duration: ([\d.]+) .*?: (.*)', re.DOTALL) #good perfectly working one.
regexobj_postgresql= re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3}) ')
regex_system_load_monitor = re.compile(r'(([\d -:]+(PM|AM))\n(.*?load average: ([\d .]+),([\d .]+),([\d .]+))\n.*\n([%\w():]+([\d. ]+)[\w,]+([\d. ]+)[\w,]+([\d. ]+)ni, ([\d. ]+)id, ([\d. ]+)wa, ([\d. ]+)hi, ([\d. ]+)si, ([\d. ]+)st)\n(KiB Mem : ([\d ]+)total,([\d ]+)free,([\d ]+)used,([\d ]+)buff/cache)\n(KiB Swap:([\d ]+)total,([\d ]+)free,([\d ]+)used.([\d ]+)avail Mem))')


path = '/Users/vinayreddy/Desktop/logs/chandra-long/tmpA_8bYH/'
#path = '/Users/vinayreddy/Desktop/logs/kushal/tmp505h5X/'
#path = '/Users/vinayreddy/Desktop/logs/rohit-1/tmpDAUyYu'



def radius_folder_files(path):
    radius_files = []
    radius_csv = []
    radius_config = []
    radius_config_csv = []
    radius_folder = ''

    for f, sf, files in os.walk(path):
        if '/PolicyManagerLogs/tips-radius-server' in f:
            radius_folder = f
            for file in files:
                if 'csv' in file:
                    radius_csv.append(f+'/'+file)
                elif 'radius_config_csv' in file:
                    radius_config_csv.append(f+'/'+file)
                elif 'radius.log' in file:
                    radius_files.append(f+'/'+file)
                elif 'radius_config' in file:
                    radius_config.append(f+'/'+file)

            return radius_files, radius_config,radius_config_csv, radius_csv, radius_folder


def policy_folder_files(path):
    policy_files = []
    policy_files_csv = []
    policy_folder = ''
    for f, sf, files in os.walk(path):
        if 'PolicyManagerLogs/policy-server' in f:
            policy_folder = f
            for file in files:
                if 'csv' in file:
                    policy_files_csv.append(f + '/' + file)
                elif 'policy-server.log' in file:
                    policy_files.append(f + '/' + file)
            return policy_files, policy_files_csv, policy_folder


def policy_file_reordering():
    policy_file_ordered = []
    path = os.path.dirname(policy_files[0])
    for i in range(len(policy_files)):
        policy_file_ordered.append(path+ '/policy-server.log.' + str(i))
    return policy_file_ordered


def radius_file_reordering():
    radius_file_ordered = []
    path = os.path.dirname(radius_files[0])
    for i in range(len(radius_files)):
        radius_file_ordered.append(path+ '/radius.log.' + str(i))
    return radius_file_ordered


def samba_folder_files(path):
    samba_files = []
    samba_files_csv = []
    samba_folders = []
    for f, fs, files in os.walk(path):
        if '/PolicyManagerLogs/samba/' in f:
            samba_folders.append(f)
            for file in files:
                if 'csv' in file:
                    samba_files_csv.append(f + '/' + file)
                elif 'log.wb' in file:
                    samba_files.append(f + '/' + file)
    return samba_files, samba_files_csv, samba_folders


def policy_csv_creation():
    print('inside policy csv creation')
    a = dt.datetime.now()
    if len(policy_files_csv) == 0:
        for file in policy_file_ordered[::-1]:
            fileh2 = open(policy_folder + '/lines_that_didnt_match_policy.txt','w+')

            fileh = open(policy_folder + '/policy.csv','a+')
            csvoutput = csv.writer(fileh)

            with open(file, 'a') as fh:
                fh.write('\n')  #last line of the file doesn't match if new line is not added.

            with open(file, 'r') as fh_read:
                for line in fh_read:
                    mo=reg_obj_policy.search(line)
                    if mo is not None:
                        csvoutput.writerow(mo.groups())
                    else:
                        fileh2.write(line)  #writing the lines that didnt match the regex.

            fileh.close()
            fileh2.close()
    b = dt.datetime.now()
    return 'Success policy- ', b - a


def smb_csv_creation():
    print('inside smb csv creation')
    z = dt.datetime.now()
    #    print(z)
    pattern_found = None
    string = ''
    line_list = []
    if len(samba_files_csv) == 0:
        #        print('Samba Folders: ',samba_folders)
        for folder in samba_folders:
            samba_o_files, samba_o_csv, samba_o_folders= samba_folder_files(folder)
            #            print('Samba Files: ', samba_files)
            for file in reversed(samba_o_files):
                line_list = []
                #                print('SambaFile: ', file)
                with open(file, 'r') as fh:
                    for line in fh:
                        a = reg_obj_smb.search(line)
                        if a is not None and pattern_found is None:
                            string = string + line
                            pattern_found = 1
                        elif a is None and pattern_found == 1:
                            string = string + line
                        elif a is not None and pattern_found == 1:
                            line_list.append(string)
                            string = ''
                            string = string + line
                            pattern_found = 1
                fileh = open(folder+ '/samba.csv','a+')
                csvoutput = csv.writer(fileh)
                for line in line_list:
                    mo = reg_obj3_smb.search(line)
                    try:
                        csvoutput.writerow([mo[1], mo[2], mo[3], mo[4], mo[5].strip('\n')])
                    except:
                        print('In except condition : line ==== m0[1]: ', mo[1])
                        print('In except condition : line ==== mo[2]: ', mo[2])
                        print('In except condition : line ==== mo[3]: ', mo[3])
                        print('In except condition : line ==== mo[4]: ', mo[4])
                        print('In except condition : line ==== mo[5]: ', mo[5])

                fileh.close()
    b = dt.datetime.now()
    print(b)
    return 'Success samba -', b - z


def radius_csv_creation():
    print('inside radius csv creation')
    a = dt.datetime.now()
    if len(radius_csv) == 0:
        fileh2 = open(radius_folder + '/lines_that_didnt_match.txt','a')
        fileh = open(radius_folder + '/radius.csv','a')
        csvoutput = csv.writer(fileh)
        regex_obj = re.compile(r'(\d{4}(-\d{2}){2} [\d:,]+) \[(.*?)\] ([A-Z]+?)\s+(.*?) - (.*?)\n')
        for file in radius_file_ordered:
            with open(file, 'a') as fh:
                fh.write('\n')  #last line of the file doesn't match if new line is not added.
        for file in radius_files:
            with open(file, 'r',encoding="utf8", errors='ignore' ) as fh3:
                for line in fh3:
                    mo=regex_obj.search(line)
                    if mo is not None:
                        csvoutput.writerow(mo.groups())
                    else:
                        fileh2.write(line)  #writing the lines that didnt match the regex.

        fileh.close()
        fileh2.close()
    b = dt.datetime.now()
    return 'Success radius -', b - a

#=============

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

def http_csv_creation():
    print('inside http csv creation')
    z = dt.datetime.now()
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
    b = dt.datetime.now()
    return 'Success httpd - ', b - z

def postgresql_logs_folder(path):
    postgresql_files = []
    postgresql_files_csv = []
    for f, sf, files in os.walk(path):
        if '/SystemLogs/var/lib/pgsql/data/pg_log' in f:
            postgresql_folder = f
            for file in files:
                if 'csv' in file:
                    postgresql_files_csv.append(f+'/'+file)
                elif 'csv' not in file:
                    postgresql_files.append(f+'/'+file)
            return postgresql_files, postgresql_files_csv, postgresql_folder

def postgresql_csv_creation():
    print('inside postgresql csv creation')
    z = dt.datetime.now()
    string = ''
    listoflines = []
    if len(postgresql_files_csv) == 0 :
        for file in postgresql_files:
            with open( file, 'r') as fh:
                firstPatternFound = None
                secondPatternFound = None
                for line in fh.readlines():
                    b = regexobj_postgresql.search(line)
                    if b is not None and firstPatternFound is None:
                        firstPatternFound =1
                        string = string + line +'\n'
                    elif b is None and firstPatternFound == 1:
                        string = string + line +'\n'
                    elif b is not None and firstPatternFound == 1:
                        listoflines.append(string)
                        string = ''
                        string = string + line + '\n'


    with open( postgresql_folder + '/queries.csv', 'w') as fh2:
        outputwriter = csv.writer(fh2)
        for item in listoflines:
            if 'duration:' in item:
                #             print(item)
                c = regexobj2_postgresql.search(item)
                #             print(c.groups())
                outputwriter.writerow(c.groups())
            #             print(list(c.groups()))
            else:
                continue
    y = dt.datetime.now()
    return 'Success postgresql - ', y - z


def system_load_monitor_folder_files(path):
    print('inside the System Load Monitor folder files now')
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

def system_load_monitor_csv_creation():
    print('inside system_load_monitor_csv_creation')
    z = dt.datetime.now()
    if len(system_load_files_csv) == 0 :
        for j in range(len(system_load_files)):
            with open( system_load_files[j], 'r') as fh:
                a= fh.read()
                b = re.split('\n\s*\n', a)
                c = [ i for i in b if 'load average:' in i]
                #            with open(system_load_files[j] +'_csv_'+ str(j), 'w' ) as fh2:
                with open( f + '/system-load-csv' ,'a' ) as fh2:
                    csv_fh = csv.writer(fh2)
                    for i in c:
                        d = regex_system_load_monitor.search(i)
                        if d is not None:
                            csv_fh.writerow([d[2].strip(), d[5].strip(), d[6].strip(), d[7].strip(), d[9].strip(), d[10].strip(), d[11].strip(), d[12].strip(), d[13].strip(), d[14].strip(),d[15].strip(), d[16].strip(), d[18].strip(), d[19].strip(), d[20].strip(), d[21].strip(), d[23].strip(), d[24].strip(), d[25].strip(),d[26].strip()])
                        else:
                            continue
                            #print('printing else part -', i)
    y = dt.datetime.now()
    return 'Success system load monitor - ', y - z

def com_func_files(f):
    if f == 1:
        return radius_folder_files(path)
    elif f == 2:
        return policy_folder_files(path)
    elif f == 3:
        return samba_folder_files(path)
    elif f == 4:
        return http_folder_files(path)
    elif f == 5:
        return postgresql_logs_folder(path)
    elif f == 6:
        return system_load_monitor_folder_files(path)


def com_func_reorderfiles(f):
    if f == 1:
        return policy_file_reordering()
    elif f == 2:
        return radius_file_reordering()

def com_func_csv_creation(f):
    if f == 1:
        return radius_csv_creation()
    elif f == 2:
        return policy_csv_creation()
    elif f == 3:
        return smb_csv_creation()
    elif f == 4:
        return http_csv_creation()
    elif f == 5:
        return postgresql_csv_creation()
    elif f == 6:
        return system_load_monitor_csv_creation()

with concurrent.futures.ThreadPoolExecutor() as executor:
    (radius_files, radius_config,radius_config_csv, radius_csv, radius_folder), (policy_files, policy_files_csv, policy_folder), (samba_files, samba_files_csv, samba_folders), (http_files, http_ssl_files, http_ssl_csv, http_csv ), (postgresql_files, postgresql_files_csv, postgresql_folder), (system_load_files, system_load_files_csv, f) = executor.map(com_func_files, range(1,7))


with concurrent.futures.ThreadPoolExecutor() as executor:
    policy_file_ordered, radius_file_ordered = executor.map(com_func_reorderfiles, range(1,3))


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(com_func_csv_creation, range(1,7))


with concurrent.futures.ThreadPoolExecutor() as executor:
    (radius_files, radius_config,radius_config_csv, radius_csv, radius_folder), (policy_files, policy_files_csv, policy_folder), (samba_files, samba_files_csv, samba_folders), (http_files, http_ssl_files, http_ssl_csv, http_csv ), (postgresql_files, postgresql_files_csv, postgresql_folder), (system_load_files, system_load_files_csv, f) = executor.map(com_func_files, range(1,7))


end = dt.datetime.now()

print(end - start)


























