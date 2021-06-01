from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Login Form")
window.geometry("700x700")
window.config(bg="#222222")

# Defining functions

username = ["Thabo", "Winnie", "Ayanda", "Oscar"]
key = ["Apple", "Banana", "Pear", "Orange"]


def membership():

    for x in range(len(key)):
        if name_entry.get() == username[x] and password_entry.get() == key[x]:
            found = True
            if found == True:
                messagebox.showinfo(title="Status", message="Access Granted!")
                window.destroy()
                import Lotto
        else:
            messagebox.showerror(title="Error", message="Access Denied!")
            window.destroy()


def clear_btn():
    name_entry.delete(0, END)
    password_entry.delete(0, END)


def exit_btn():
    return window.destroy()


# Frame
myframe = Frame(window, bg="#ed2d34")
myframe.place(x=10, y=10, width=500, height=500)

# Labels
name = Label(myframe, text="Username: ")
name.place(x=20, y=20)
password = Label(myframe, text="Password: ")
password.place(x=20, y=50)

# Entry
name_entry = Entry(myframe)
name_entry.place(x=110, y=20)
password_entry = Entry(myframe, show="*")
password_entry.place(x=110, y=50)

# Button
verify = Button(myframe, text="Login", command=membership)
verify.place(x=30, y=150)
clear = Button(myframe, text="Clear")
clear.place(x=100, y=150)
fin = Button(myframe, text="Exit", command=exit_btn)
fin.place(x=170, y=150)

# Image
canvas = Canvas(myframe, width=400, height=300)
canvas.pack(side=BOTTOM)
img = PhotoImage(file="index.png")
canvas.create_image(20, 20, anchor=NW, image=img)


window.mainloop()
