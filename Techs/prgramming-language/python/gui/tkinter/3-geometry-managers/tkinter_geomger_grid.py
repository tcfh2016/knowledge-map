import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=50)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(3):
        frame = tk.Frame(
            master=window, 
            width=50, 
            height=50,
            relief=tk.RAISED,
            borderwidth=2)
        
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()


window.mainloop()