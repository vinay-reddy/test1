import re, csv

import pandas as pd




reg_obj_policy = re.compile(r'(\d{4}(-\d{2}){2} [\d:,]+) \[(.*?)\] ([A-Z]+?)\s+(.*?) - (.*?)\n')

fileh2 = open('/Users/vinayreddy/Desktop/logs/vijay_escalation/tmpaMlez1/PolicyManagerLogs/policy-server/lines_that_didnt_match_policy.txt','w+')

fileh = open('/Users/vinayreddy/Desktop/logs/vijay_escalation/tmpaMlez1/PolicyManagerLogs/policy-server/policy.csv','w+')
csvoutput = csv.writer(fileh)

with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/tmpaMlez1/PolicyManagerLogs/policy-server/policy-server.log.2', 'a') as fh:
    fh.write('\n')  #last line of the file doesn't match if new line is not added.

with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/tmpaMlez1/PolicyManagerLogs/policy-server/policy-server.log.2', 'r') as fh_read:
    for line in fh_read:
        mo=reg_obj_policy.search(line)
        if mo is not None:
            csvoutput.writerow(mo.groups())
        else:
            fileh2.write(line)  #writing the lines that didnt match the regex.

fileh.close()
fileh2.close()

columns = ['Time', 'drop', 'Hmmm...', 'Level', 'Module', 'Message']

df = pd.read_csv('/Users/vinayreddy/Desktop/logs/vijay_escalation/tmpaMlez1/PolicyManagerLogs/policy-server/policy.csv', header= None, names = columns)

# a = df['Message'].to_frame()
# print(a)

# for item in df['Hmmm...']:
#     # item.split()
#     # print(list(item.split()))
#     map(l=)

df2 = df[df['Message'].str.contains('.time:')]

def filterSessionId(sessionID):
    df3 = df[df['Hmmm...'].str.contains(sessionID)]
#     print(df3)
    return df3

df4 = filterSessionId('R000196b2-02-5d7a8955')