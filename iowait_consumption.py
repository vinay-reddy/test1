


import matplotlib.pyplot as plt
import pandas as pd


#plotting the graph

columns = ['time','us', 'sy', 'ni', 'id', 'wa', 'hi', 'si', 'st']

pandas_plot = pd.read_csv('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/PolicyManagerLogs/system-load-monitor/iowait.csv', names=columns, header=None)
x_axis = pandas_plot['time']
y_id = pandas_plot['id']
y_wa = pandas_plot['wa']
y_st = pandas_plot['st']


plt.plot(x_axis, y_id, label='Idle')
plt.plot(x_axis, y_wa, label='IOwait')
plt.plot(x_axis, y_st, label='% steal')


plt.legend()
plt.xticks(rotation='vertical')
plt.show()
