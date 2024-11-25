import sqlite3 , hashlib
from tkinter import *

window = Tk()

window.title("password vault")

def firstscreen():
    window.geometry("350x150")
    lbl = Label(window, text="create master password")
    lbl.config(anchor="center")
    lbl.pack()

    txt = Entry(window, width=20)
    txt.pack()
    txt.focus()

    lbl1 = Label(window , text=" re-enter password")
    lbl1.pack()

    txt1 = Entry(window, width=20)
    txt1.pack()
    txt1.focus()

    def savepassword():
        if txt.get() == txt1.get():
            pass
        else:
            lbl.configure(text="password do not match")

    btn = Button(window, text="Save", command=savepassword)
    btn.pack()
    btn.pack( pady=10)

def loginScreen():
    window.geometry("350x150")
    lbl = Label(window, text="Enter master password")
    lbl.config(anchor="center")
    lbl.pack()


    txt = Entry(window , width=20 , show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.pack()

    def checkpassword():
        password = "test"
        if password == txt.get():
           passwordVaultScreen()
        else:
            txt.delete(0, END)
            lbl1.config(text="wrong password")

    btn = Button(window, text="submit" , command=checkpassword)
    btn.pack()
    btn.pack(padx=10, pady=10)

def passwordVaultScreen():
    for widget in window.winfo_children():
        widget.destroy()
        window.geometry("750x350")

        lbl = Label(window)
        lbl.config(anchor="center")
        lbl.pack()

# loginScreen()
firstscreen()
window.mainloop()

