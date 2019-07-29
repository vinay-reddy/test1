
import re
import matplotlib.pyplot as plt
import pandas as pd

# regex_object=re.compile(r'([\d -:]*(PM|AM))\n(.*?)load average: ([\d .,]*)')
#
# with open('/Users/vinayreddy/Desktop/logs/project_load_plotting/a.log', 'r') as file:
#     a= file.read()
#     b=regex_object.findall(a)
#
# with open('/Users/vinayreddy/Desktop/logs/project_load_plotting/csv.csv','w' ) as fh:
#     for i in range(len(b)):
#         fh.write(b[i][0]+', '+ b[i][3]+'\n')


#plotting the graph

columns = ['time', '1 min', '5 mins', '15 mins']
pandas_plot = pd.read_csv('/Users/vinayreddy/Desktop/logs/project_load_plotting/csv.csv', names=columns, header=None)
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

