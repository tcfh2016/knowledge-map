import time, sys
import tkinter
import tkinter.messagebox


def query_ci():
    window = tkinter.Tk()
    window.title('my window')
    window.geometry('200x200')
    tkinter.messagebox.showwarning("CI Turns RED!")

    window.mainloop()
    print ("CI status")

delay_minute = 0.2
while (True):
    time.sleep(delay_minute * 60)
    query_ci()
