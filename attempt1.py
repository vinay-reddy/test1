

import re, csv
import shutil

# a = []
#
# with open('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/SystemLogs/var/lib/pgsql/data/pg_log/postgresql-Sun.log', 'r') as fh:
#     for line in fh.readlines():
#         line=line.strip()
#         if 'duration: ' in line:
#             a.append(line)
#         else:
#             continue
#
#
# print(a)
#



regexobj=re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3}) ')
#base working one --> regexobj2 = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3,}) (\w+) (\w+) (\d+) .* duration: ([\d.].*( ms))\s.* statement: (.*)', re.DOTALL)

# regexobj2 = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3,}) (\w+) (\w+) (\d+) .* duration: ([\d.]+) .* statement: (.*)', re.DOTALL)
#regexobj2 = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3,}) (\w+) (\w+) (\d+) .* duration: ([\d.]+) .* (statement|execute <unnamed>): (.*)', re.DOTALL)

string = ''
regexobj2 = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3,}) (\w+) (\w+) (\d+) .* duration: ([\d.]+) .*?: (.*)', re.DOTALL) #good perfectly working one.
listoflines = []
with open('/Users/vinayreddy/Desktop/logs/balaji/postgresql-Sat.log', 'r') as fh:
    firstPatternFound = None
    secondPatternFound = None
    for line in fh.readlines():
        b = regexobj.search(line)
        if b is not None and firstPatternFound is None:
            firstPatternFound =1
            string = string + line
        elif b is None and firstPatternFound == 1:
            string = string + line
        elif b is not None and firstPatternFound == 1:
            listoflines.append(string)
            string = ''
            string = string + line

#print(listoflines)

with open('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/SystemLogs/var/lib/pgsql/data/pg_log/queries.csv', 'w') as fh2:
    outputwriter = csv.writer(fh2)
    for item in listoflines:
        if 'duration:' in item:
#             print(item)
             c = regexobj2.search(item)
#             print(c.groups())
             outputwriter.writerow(c.groups())
#             print(list(c.groups()))
        else:
            continue

print(c.groups())




'''
TO DO:

split the multiple line into each column and 
'''




