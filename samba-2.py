import re, csv, sys
import pandas as pd

reg_obj = re.compile(r'^\[[\d/]+')
reg_obj2 = re.compile(r'([\d/ :.]+),\s+(\d),\s+pid=(\d+)\]\s+(.*)\n(.*)')
reg_obj3 = re.compile(r'\[([\d/ :.]+),\s+(\d),\s+pid=(\d+)\]\s+(.*?)\n(.*)',re.DOTALL)
pattern_found = None
string = ''
line_list = []
with open('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/log.wb-NT_WEB', 'r') as fh:
    for line in fh:
        a = reg_obj.search(line)
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
print("printing this line:" ,line_list[:11])
# for i in range(11):
#     print('line ' + str(i) + ':', line_list[i])
# sys.exit()
fileh = open('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/samba.csv','w+')
csvoutput = csv.writer(fileh)

for line in line_list:
#    mo = reg_obj2.search(line)
    mo = reg_obj3.search(line)
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

df = pd.read_csv('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/samba.csv',  names=columns,  header=None)

df2=df[df['Last Column'].str.contains('NT_STATUS')]
df3=df[df['Last Column'].str.contains(' user:')]