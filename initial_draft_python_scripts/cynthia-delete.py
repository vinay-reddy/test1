

import re, csv
import matplotlib.pyplot as plt
import pandas as pd



regex_object=re.compile(r'([\d -:]*(PM|AM))\n((.*?)\n){2}(.*?)\nKiB Mem : (.*?)\nKiB Swap: (.*?)\n')

with open('/Users/vinayreddy/Desktop/logs/cynthia-iowait/system-load.2019-09-24.log', 'r') as file:
    a= file.read()
    b=regex_object.findall(a)

fh = open('/Users/vinayreddy/Desktop/logs/cynthia-iowait/ram.csv', 'w')

outputwriter = csv.writer(fh)

fh2 = open('/Users/vinayreddy/Desktop/logs/cynthia-iowait/swap.csv', 'w')

outputwriter2 = csv.writer(fh2)

fh3 = open('/Users/vinayreddy/Desktop/logs/cynthia-iowait/iowait.csv','w')

outputwriter3 = csv.writer(fh3)

for i in range(len(b)):
    ram = re.findall('\d+', b[i][5])
    swap = re.findall('\d+', b[i][6])
    iowait = re.findall('[\d.]+', b[i][4])
    ram.insert(0, b[i][0].strip())
    swap.insert(0, b[i][0].strip())
    iowait.insert(0,b[i][0].strip())
    outputwriter.writerow(ram)
    outputwriter2.writerow(swap)
    outputwriter3.writerow(iowait)
    ram = []
    swap =[]
    iowait =[]

fh.close()
fh2.close()
fh3.close()
#plotting the graph

columns = ['time', 'Total Ram', 'Free Ram', 'Used', 'buff/cache']

pandas_plot = pd.read_csv('/Users/vinayreddy/Desktop/logs/cynthia-iowait/ram.csv', names=columns, header=None)
x_axis = pandas_plot['time']
y_axis_total_ram = pandas_plot['Total Ram']
y_axis_free_ram = pandas_plot['Free Ram']
y_axis_Used = pandas_plot['Used']
y_axis_buffer_cache = pandas_plot['buff/cache']

plt.plot(x_axis, y_axis_total_ram, label='Total Ram in KiB')
plt.plot(x_axis, y_axis_free_ram, label='Free Ram in KiB')
plt.plot(x_axis, y_axis_Used, label='Used in KiB')
plt.plot(x_axis, y_axis_buffer_cache, label='buff/cache')

plt.legend()
plt.xticks(rotation='vertical')
plt.show()
# plt.xlabel("times")
# plt.ylabel("Ram Usage")
# plt.title("Graph")

