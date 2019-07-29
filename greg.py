
import re
import matplotlib.pyplot as plt
import pandas as pd
#
# regex_object=re.compile(r'([\d -:]*(PM|AM))\n(.*?)load average: ([\d .,]*)')
#
# with open('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/PolicyManagerLogs/system-load-monitor/system-load.2019-07-01.log', 'r') as file:
#     a= file.read()
#     b=regex_object.findall(a)
#
# with open('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/PolicyManagerLogs/system-load-monitor/csv.csv','w' ) as fh:
#     for i in range(len(b)):
#         fh.write(b[i][0]+', '+ b[i][3]+'\n')      '''fh.write(b[i][0].strip()+', '+ b[i][3]+'\n')  ---> to avoid space before the date'''


#plotting the graph

columns = ['time', '1 min', '5 mins', '15 mins']

dateparse = lambda x: pd.datetime.strptime(x, '%m-%d-%y %H:%M:%S %p')
pandas_plot = pd.read_csv('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/PolicyManagerLogs/system-load-monitor/csv.csv', names=columns, header=None, parse_dates=['time'], date_parser=dateparse,verbose=True)
x_axis = pandas_plot['time']
y_axis_1min = pandas_plot['1 min']
y_axis_5min = pandas_plot['5 mins']
y_axis_15min = pandas_plot['15 mins']

plt.xlabel("times")
plt.ylabel("CPU load")
plt.title("Graph")

plt.plot(x_axis, y_axis_1min, label='1min load avg')
plt.plot(x_axis, y_axis_5min, label='5min load avg')
plt.plot(x_axis, y_axis_15min, label='15min load avg')
plt.xticks(rotation='vertical')
plt.legend()

#plt.grid(True)
plt.show()
"""

1. radius thread count.
2. policy thread count
3. HTTP Statistics 
4. memory plot
5. io plot (iotop)
6. long running queries
7. SNMP GET count like http statistics
8. No. of authentications .
9. No. of endpoints
10. no. of profiled endpoints and their list
11. extracting the licenses.
12. network details.
13. 


HTTP Statistics 



"""


