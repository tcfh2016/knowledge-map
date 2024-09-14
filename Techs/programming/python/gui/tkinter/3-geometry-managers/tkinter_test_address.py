import tkinter as tk

window = tk.Tk()

# Frame Entry
frame_entry = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=1)
frame_entry.pack()

labels = ['First Name', 'Last Name', 'Address Line 1', 'Address Line 2', 'City', 'State/Province', 'Postal Code', 'Country']
for i in range(len(labels)):
    frame_label = tk.Frame(master=frame_entry)
    frame_label.grid(row=i)

    label = tk.Label(
        master=frame_label,
        width=15,
        text=f"{labels[i]}:",
        anchor='e')
    label.pack(side=tk.LEFT)
    entry = tk.Entry(master=frame_label, width=50)
    entry.pack(side=tk.RIGHT)

# Frame Button
frame_button = tk.Frame(master=window)
frame_button.pack(fill=tk.X, ipadx=5, ipady=5)

button_submit = tk.Button(master=frame_button, text="Submit")
button_submit.pack(side=tk.RIGHT, ipadx=10, padx=10)

button_clear = tk.Button(master=frame_button, text="Clear")
button_clear.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()