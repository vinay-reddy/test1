

import matplotlib.pyplot as plt
import pandas as pd

columns2 = ['time', 'Total Swap', 'Free Swap', 'Used', 'avail Mem']

pandas_plot2 = pd.read_csv('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/PolicyManagerLogs/system-load-monitor/swap.csv', names=columns2, header=None)
x_axis2 = pandas_plot2['time']
y_axis_total_swap = pandas_plot2['Total Swap']
y_axis_free_swap = pandas_plot2['Free Swap']
y_axis_Used2 = pandas_plot2['Used']
y_axis_avail_mem = pandas_plot2['avail Mem']


plt.plot(x_axis2, y_axis_total_swap, label='Total swap in KiB')
plt.plot(x_axis2, y_axis_free_swap, label='Free swap in KiB')
plt.plot(x_axis2, y_axis_Used2, label='Used in KiB')
plt.plot(x_axis2, y_axis_avail_mem, label='Avail Mem')

plt.xticks(rotation='vertical')

plt.legend()
#plt.grid(True)
plt.show()

