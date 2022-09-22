from time import sleep
from tkinter import *
from threading import *
import win32api
import win32con


root = Tk()
root.title("AutoClick")
root.geometry("450x150+50+250")

convert = Entry(root, width=20)
convert.place(relx=0.1, rely=0.1, width=150, height=25)


def threading():
    t1 = Thread(target=click)
    t1.start()
    note = Label(root, text=f"{enter_time.get()}")
    note.place(relx=0.15, rely=0.7, width=300, height=30)
    note.config(font=10)


def converter():
    try:
        time_in_seconds = int(convert.get())*60
        convertion_result = Label(root, text=time_in_seconds)
        convertion_result.place(relx=0.75, rely=0.1, width=50, height=25)
    except:
        pass


def click():
    try:
        sleep(int(enter_time.get()))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    except:
        fail_text = Label(root, text="Error")
        fail_text.place(relx=0.75, rely=0.4, width=50, height=25)


button2 = Button(root, text="Convert (min - sec)", padx=20, command=converter)
button2.place(relx=0.4, rely=0.1, width=150, height=25)

enter_time = Entry(root, width=20)
enter_time.place(relx=0.1, rely=0.4, width=150, height=25)

button = Button(root, text=f"Click in ({enter_time.get()}) seconds", command=threading, padx=24)
button.place(relx=0.4, rely=0.4, width=150, height=25)

root.mainloop()