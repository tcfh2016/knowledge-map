import dearpygui.dearpygui as dpg
from math import sin
import pandas as pd

dpg.create_context()

# creating data
df = pd.read_csv(r"C:\N-21AJPF49T110-Data\lianbche\Documents\2024\12\26-l2lens-test\31411_10.17.54.150_20241216T113224_5G_L2_component_dl.csv")

x = [v for v in range(0, 1000)]
xtime = pd.to_datetime(df['timeStamp'])[0:1000].to_list()
xtick_pairs = tuple((str(xtime[i]), i) for i in x )
print(type(xtick_pairs))
y = df['sfn'].astype(float)[0:1000].to_list()

with dpg.window(label="Tutorial"):
    # create plot
    with dpg.plot(label="Line Series", height=400, width=400):
        # optionally create legend
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        dpg.set_axis_ticks(dpg.last_item(), xtick_pairs)
        dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")

        # series belong to a y axis
        dpg.add_line_series(x, y, label="test", parent="y_axis")
        

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()