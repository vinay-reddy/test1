
import re, csv, os
import pandas as pd
import pprint
import operator

list_of_lines = []
list_of_macs = []
with open('/Users/vinayreddy/Desktop/logs/johnson-profiling-issue/deviceprofiler/concated.log', 'r') as fh:
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

#pprint.pprint(sorted_d)

print(sorted_d)