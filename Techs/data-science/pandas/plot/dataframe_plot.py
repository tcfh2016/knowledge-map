import pandas as pd
import numpy as np

df = pd.read_csv("ex_plot.csv", index_col=0)
df = df.sort_values(by=['Date'])
df = df.set_index('Date')
composite_index_df = df['C&P Composite Index'].tail(31)
#print(df)
#fig = df['C&P Composite Index'].plot(figsize=(20, 10)).get_figure()
ax = composite_index_df.plot(figsize=(20, 10))

# Y轴的grid：Major ticks every 20, minor ticks every 5
major_ticks = np.arange(50, 151, 20)
minor_ticks = np.arange(50, 151, 5)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

# X轴的grid：
x_ticks = np.arange(0, 31, 5)
x_ticks_labels = [list(composite_index_df.index)[x] for x in x_ticks]
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_ticks_labels)

ax.grid(which='both')
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

fig = ax.get_figure()
fig.savefig('ex_plot.png')