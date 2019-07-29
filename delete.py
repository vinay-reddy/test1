

from matplotlib import pyplot as plt

# print(plt.style.available)

# plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')
plt.xkcd()

width=0.25
x_axis = [1,2,3,4,5,6]
y_axis = [23,45,67,120,340,560]
sec_yaxis = [34,56,78,190,200,320]


plt.title("this is a dummy title")
plt.xlabel("this is x axis label")
plt.ylabel("this is a y axis label")

plt.plot(x_axis, y_axis, label="Python testing", marker = "o", linewidth = 1)
plt.plot(x_axis, sec_yaxis, label="javascript testing", marker = "o",linewidth= 1)
plt.legend()
plt.tight_layout()
plt.grid(True)

#plt.savefig("myimage.png")
plt.show()
