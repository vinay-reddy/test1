from bokeh.plotting import figure, output_file, show
import pandas as pd



columns = ['time', '1 min', '5 mins', '15 mins']
pandas_plot = pd.read_csv('/Users/vinayreddy/Desktop/logs/project_load_plotting/csv.csv', names=columns, header=None, parse_dates=['time'])

x = ["06-06-2019 06:47:04","06-06-2019 06:49:05","06-06-2019 06:51:05","06-06-2019 06:53:05","06-06-2019 06:55:05"]
y=[1,3,5,9,4,]
x_axis = pandas_plot['time']
y_axis_1min = pandas_plot['1 min']
y_axis_5min = pandas_plot['5 mins']
y_axis_15min = pandas_plot['15 mins']



# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_type = "datetime", x_axis_label='x', y_axis_label='y')


p.line(x, y, legend="Temp.", line_width=2)
# p.line(x_axis, y_axis_5min, legend="Temp.", line_width=2)
#
# p.line(x_axis, y_axis_15min, legend="Temp.", line_width=2)

# show the results
show(p)