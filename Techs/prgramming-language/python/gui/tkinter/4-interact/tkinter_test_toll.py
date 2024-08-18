import random
import tkinter as tk

def roll():
    number = random.randint(1, 6)
    label['text'] = f"{number}"


window = tk.Tk()
window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

button_decrease = tk.Button(master=window, text="Roll", command=roll)
button_decrease.grid(row=0, column=0, sticky="nsew")

label = tk.Label(master=window, text=".")
label.grid(row=1, column=0)

window.mainloop()