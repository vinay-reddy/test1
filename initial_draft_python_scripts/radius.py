import re, csv

import pandas as pd

'''
format:

<time> [....] <MSG LEVEL> RadiusServer.Radius - <msg>

'''
fileh2 = open('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/lines_that_didnt_match.txt','w+')

fileh = open('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/radius.csv','w+')
csvoutput = csv.writer(fileh)

regex_obj = re.compile(r'(\d{4}(-\d{2}){2} [\d:,]+) \[(.*?)\] ([A-Z]+?)\s+RadiusServer.Radius - (.*?)\n')
with open('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/radius.log.0', 'a') as fh:
    fh.write('\n')  #last line of the file doesn't match if new line is not added.

with open('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/radius.log.0', 'r') as fh:
    for line in fh:
        mo=regex_obj.search(line)
        if mo is not None:
            csvoutput.writerow(mo.groups())
        else:
            fileh2.write(line)  #writing the lines that didnt match the regex.

fileh.close()
fileh2.close()


columns = ['Time', 'drop', 'Hmmm...', 'Level', 'Message']

df = pd.read_csv('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/radius.csv', header= None, names = columns)

df2 = df[df['Level'] == 'ERROR']

