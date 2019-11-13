import re, csv, sys
import pandas as pd
import datetime as dt

start = dt.datetime.now()

reg_obj_smb = re.compile(r'^\[[\d/]+')
reg_obj2_smb = re.compile(r'([\d/ :.]+),\s+(\d),\s+pid=(\d+)\]\s+(.*)\n(.*)')
reg_obj3_smb = re.compile(r'\[([\d/ :.]+),\s+(\d),\s+pid=(\d+)\]\s+(.*?)\n(.*)',re.DOTALL)

pattern_found = None
string = ''
line_list = []
with open('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/PolicyManagerLogs/samba/samba_CAMPUS/log.wb-CAMPUS', 'r') as fh:
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
#print("printing this line:" ,line_list[:11])
# for i in range(11):
#     print('line ' + str(i) + ':', line_list[i])
# sys.exit()
fileh = open('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/PolicyManagerLogs/samba/samba_CAMPUS/samba.csv','w+')
csvoutput = csv.writer(fileh)

for line in line_list:
    #    mo = reg_obj2_smb.search(line)
    mo = reg_obj3_smb.search(line)
    # print('line :',line)
    # print('mo: ',mo.groups())
    try:
        csvoutput.writerow([mo[1], mo[2], mo[3], mo[4], mo[5]])
    except:
        print('In except condition : line ==== m0[1]: ', mo[1])
        print('In except condition : line ==== mo[2]: ', mo[2])
        print('In except condition : line ==== mo[3]: ', mo[3])
        print('In except condition : line ==== mo[4]: ', mo[4])
        print('In except condition : line ==== mo[5]: ', mo[5])

fileh.close()

columns = ['Time', 'Some Number', 'pid', 'Some info', 'Last Column']

df = pd.read_csv('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/PolicyManagerLogs/samba/samba_CAMPUS/samba.csv',  names=columns,  header=None)

df2=df[df['Last Column'].str.contains('NT_STATUS')]
df3=df[df['Last Column'].str.contains(' user:')]
df2 = df2.reset_index(drop=True)
df3 = df3.reset_index(drop=True)
df4 = pd.concat([df3, df2], axis=1)

end = dt.datetime.now()

#function to pull entries between two timestamps

def smb_log_line_extraction(start_time, end_time, netbios_name):
    for name in dfs:
        if netbios_name in name:
            data_frame = list_of_dfs[name]
    data_frame = df.set_index(['Time'])
    return data_frame.loc[start_time:end_time]

smb_lines = smb_log_line_extraction('2019/10/23 20:24:26.072','2019/10/23 20:24:26.1')


print( end - start)