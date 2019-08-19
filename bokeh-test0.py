from bokeh.plotting import figure, output_file, show

output_file("bokeh.html")

p = figure(plot_width=500,  plot_height = 500, title = None)

p.patch([1,2,3,4,5], [6,7,2,4,5],color="navy", alpha =0.5)

show(p)

