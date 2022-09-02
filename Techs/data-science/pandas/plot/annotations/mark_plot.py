import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
print(df["Pulse"])
ax = df["Pulse"].plot()

# 简单标记
y_max = df["Pulse"].max()
x_max = df["Pulse"].idxmax()
ax.annotate('max=' + str(y_max),
            xy=(x_max, y_max),
            xytext=(x_max, y_max+5),
            arrowprops=dict(arrowstyle="->"),
            )

# 指定箭头形状
y_min = df["Pulse"].min()
x_min = df["Pulse"].idxmin()
ax.annotate('min=' + str(y_min), xy=(x_min, y_min), xytext=(x_min, y_min+5),
            arrowprops=dict(arrowstyle="fancy", facecolor='red'),
            )

plt.show()
#print(df)
