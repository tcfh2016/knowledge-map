import tkinter as tk

window = tk.Tk()

# Frame
frame_a = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=5
)
frame_b = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=5
)

# Label
greeting = tk.Label(
    master=frame_a,
    text='Hello Tkinter!',
    foreground='white',
    background='black',
    width = 25,
    height = 5)
greeting.pack()

# Button
button = tk.Button(
    master=frame_b,
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

# Entry
label = tk.Label(
    master=frame_b, 
    text="Name") # 自动将Entry上的Label居中
entry = tk.Entry(
    master=frame_b, 
    fg="black", 
    bg="gray")
label.pack()
entry.pack()

# Text
text_box = tk.Text(
    master=frame_b
)
text_box.pack()


frame_a.pack()
frame_b.pack()

window.mainloop()
