import tkinter as tk

window = tk.Tk()

# Frame Entry
frame_entry = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=1)

labels = ['First Name', 'Last Name', 'Address Line 1', 'Address Line 2', 'City', 'State/Province', 'Postal Code', 'Country']
for i in range(len(labels)):
    frame_label = tk.Frame(master=frame_entry)
    frame_label.grid(row=i)

    label = tk.Label(
        master=frame_label,
        width=15,
        text="{}:".format(labels[i]))
    label.pack(side=tk.LEFT)
    entry = tk.Entry(master=frame_label, width=50)
    entry.pack(side=tk.RIGHT)

frame_entry.pack()


# Frame Button
frame_button = tk.Frame(master=window)
frame_button.pack()

button_clear = tk.Button(master=frame_button, text="Clear")
button_clear.pack(side=tk.LEFT)
button_submit = tk.Button(master=frame_button, text="Submit")
button_submit.pack(side=tk.RIGHT)


window.mainloop()