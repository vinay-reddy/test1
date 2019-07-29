

import re
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
string = ''
listoflines = []
with open('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/SystemLogs/var/lib/pgsql/data/pg_log/postgresql-Mon.log', 'r') as fh:
    firstPatternFound = None
    secondPatternFound = None
    for line in fh.readlines():
        b = regexobj.search(line)
        if b is not None and firstPatternFound is None:
            firstPatternFound =1
            string = string + line +'\n'
        elif b is None and firstPatternFound == 1:
            string = string + line +'\n'
        elif b is not None and firstPatternFound == 1:
            listoflines.append(string)
            string = ''
            string = string + line + '\n'
            firstPatternFound = 1

print(listoflines)





