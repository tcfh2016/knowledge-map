import random
import tkinter as tk

def convert():
    temperature = entry_temperature.get()
    celsius = (5 / 9) * (float(temperature) - 32)
    label_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

frame_entry = tk.Frame(master=window)
entry_temperature = tk.Entry(master=frame_entry, width=20)
label_temperature = tk.Label(master=frame_entry, text="\N{DEGREE FAHRENHEIT}")
entry_temperature.grid(row=0, column=0, sticky="e")
label_temperature.grid(row=0, column=1, sticky="w")

button_covert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=convert)
label_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
frame_entry.grid(row=0, column=0, padx=10)
button_covert.grid(row=0, column=1, padx=10)
label_result.grid(row=0, column=2, padx=10)

window.mainloop()