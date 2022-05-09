import tkinter as tk

from tkinter import *
from tkinter import messagebox

def Register():
    openWindow.destroy()
    formWindow = tk.Tk()
    formWindow.title("Registeration Form")
    formWindow.geometry("1100x800")
    tk.Label(formWindow, text="Please fill this From", width=30, fg='black',
            font=('Arial', 26, 'bold')).place(x=200, y=20)
    #first name
    tk.Label(formWindow, text="First Name", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=100)

    tk.Entry(formWindow,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=100)

    #last name
    tk.Label(formWindow, text="Last Name", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=500, y=100)

    tk.Entry(formWindow,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=750, y=100)

    #User name
    tk.Label(formWindow, text="User Name", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=200)

    tk.Entry(formWindow,width=40, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=200)

    #email
    tk.Label(formWindow, text="E-mail", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=300)

    tk.Entry(formWindow,width=40, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=300)

    #phone number
    tk.Label(formWindow, text="Phone Number", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=400)

    tk.Entry(formWindow,width=40, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=400)

    #Birth
    tk.Label(formWindow, text="Birth", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=500)

    tk.Entry(formWindow,width=40, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=500)

    #user type
    tk.Label(formWindow, text="User", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=595)

    var = IntVar()

    tk.Radiobutton(formWindow, text="Artist", variable=var, value=1).place(x=250, y=600)
    tk.Radiobutton(formWindow, text="Artist", variable=var, value=2).place(x=350, y=600)



    #submit
    tk.Button(formWindow, text="submit",
                 width=10, fg='black',
                 font=('Arial', 16, 'bold')).place(x=450, y=650)

    formWindow.mainloop()


openWindow = tk.Tk()
openWindow.title("Welcome to FATHY Gallery")
openWindow.geometry("500x300")
tk.Label(openWindow, text="Welcome to FATHY Gallery", width=20, fg='black',
        font=('Arial', 16, 'bold')).place(x=120, y=20)
tk.Label(openWindow, text="Enter User Name", width=20, fg='black',
        font=('Arial', 16, 'bold')).place(x=0, y=100)
name = tk.StringVar()
tk.Entry(openWindow, textvariable=name, width=20, fg='black',
        font=('Arial', 16, 'bold')).place(x=240, y=100)
tk.Label(openWindow, text="Enter Password", width=20, fg='black',
        font=('Arial', 16, 'bold')).place(x=0, y=150)
store = tk.StringVar()
tk.Entry(openWindow, textvariable=store, width=20, fg='black',
        font=('Arial', 16, 'bold')).place(x=240, y=150)
tk.Button(openWindow, text="Login",
         width=10, fg='black',
        font=('Arial', 16, 'bold')).place(x=50, y=200)

tk.Button(openWindow, text="Register",
            command=lambda: Register(),
             width=10, fg='black',
            font=('Arial', 16, 'bold')).place(x=300, y=200)
openWindow.mainloop()
