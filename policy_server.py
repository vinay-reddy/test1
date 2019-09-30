import re, csv

import pandas as pd




regex_obj = re.compile(r'(\d{4}(-\d{2}){2} [\d:,]+) \[(.*?)\] ([A-Z]+?)\s+(.*?) - (.*?)\n')

fileh2 = open('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/lines_that_didnt_match_policy.txt','w+')

fileh = open('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/policy.csv','w+')
csvoutput = csv.writer(fileh)

with open('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/policy-server.log.0', 'a') as fh:
    fh.write('\n')  #last line of the file doesn't match if new line is not added.

with open('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/policy-server.log.0', 'r') as fh_read:
    for line in fh_read:
        mo=regex_obj.search(line)
        if mo is not None:
            csvoutput.writerow(mo.groups())
        else:
            fileh2.write(line)  #writing the lines that didnt match the regex.

fileh.close()
fileh2.close()

columns = ['Time', 'drop', 'Hmmm...', 'Level', 'Module', 'Message']

df = pd.read_csv('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/policy.csv', header= None, names = columns)

# a = df['Message'].to_frame()
# print(a)

# for item in df['Hmmm...']:
#     # item.split()
#     # print(list(item.split()))
#     map(l=)
