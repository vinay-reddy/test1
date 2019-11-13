
import re, csv, os
import pandas as pd
import pprint
import operator

list_of_lines = []
list_of_macs = []
with open('/Users/vinayreddy/Desktop/logs/johnson_profiling_case/nov12/devicelogs/concated.log', 'r') as fh:
    for line in fh:
        if 'Profile update mac' in line:
            list_of_lines.append(line)
            mac = line.split(':')[3].split(" ")[0]
            list_of_macs.append(mac)

#regexobj=re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3}) ')
print(list_of_macs)
print(len(list_of_macs))
count = {}
for mac in list_of_macs:
    count.setdefault(mac, 0)
    count[mac] = count[mac] + 1

#pprint.pprint(count)
sorted_d = sorted(count.items(), key=operator.itemgetter(1), reverse= True)
print(type(sorted_d))
#pprint.pprint(sorted_d)
fh = open('/Users/vinayreddy/Desktop/logs/johnson_profiling_case/nov12/devicelogs/list.txt', 'w')
for item in sorted_d:
    print(item)
    fh.write(item[0] +" -- "+ str(item[1]) + '\n')

#fh = open('/Users/vinayreddy/Desktop/logs/johnson_profiling_case/device_profiler/list.txt', 'w')
#fh.write(pprint.pprint(sorted_d))
fh.close()

# 2019-10-03 12:15:01,405

# 2019-10-03 14:43:31,266
