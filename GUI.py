import tkinter as tk

from tkinter import *
from tkinter import messagebox

def Register():

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
    tk.Radiobutton(formWindow, text="Customer", variable=var, value=2).place(x=350, y=600)

    #submit
    tk.Button(formWindow, text="submit",
                 width=10, fg='black',
                 font=('Arial', 16, 'bold'), command=lambda:artist()).place(x=450, y=650)

    formWindow.mainloop()

def artist():
    formWindow = tk.Tk()
    formWindow.title("Artist options")
    formWindow.geometry("700x500")
    tk.Button(formWindow, text="Art",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:artwork()).place(x=250, y=100)
    tk.Button(formWindow, text="Exhibition",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:exhibition()).place(x=250, y=300)


def artwork():
    formWindow = tk.Tk()
    formWindow.title("Artist options")
    formWindow.geometry("900x700")
    tk.Label(formWindow, text="Art name", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=100)

    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=100)

    tk.Label(formWindow, text="Art info", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=200)

    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=200)
    tk.Label(formWindow, text="price", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=300)

    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=300)
    tk.Label(formWindow, text="Art ID", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=400)

    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=400)

    tk.Button(formWindow, text="submit",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:confirm()).place(x=350, y=550)

def exhibition():
    formWindow = tk.Tk()
    formWindow.title("Exhibitions")
    formWindow.geometry("1100x950")
    tk.Label(formWindow, text="Exhibition id", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=100)

    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=100)

    tk.Label(formWindow, text="Exhibition name", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=200)

    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=200)
    tk.Label(formWindow, text="Exhibition location", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=300)

    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=300)
    tk.Label(formWindow, text="Ticket price", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=400)

    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=400)

    tk.Label(formWindow, text="Start date", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=500)

    tk.Entry(formWindow,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=500)

    #last name
    tk.Label(formWindow, text="End date", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=500, y=500)

    tk.Entry(formWindow,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=750, y=500)

    tk.Label(formWindow, text="Open time", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=600)

    tk.Entry(formWindow,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=600)

    #last name
    tk.Label(formWindow, text="Close time", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=500, y=600)

    tk.Entry(formWindow,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=750, y=600)

    tk.Button(formWindow, text="submit",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:confirm()).place(x=350, y=700)


def customer():
    formWindow = tk.Tk()
    formWindow.title("Review form")
    formWindow.geometry("1100x800")
    tk.Label(formWindow, text="Art work's ID", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=200)

    tk.Entry(formWindow,width=40, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=200)

    tk.Label(formWindow, text="Review", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=400)

    tk.Entry(formWindow,width=40, fg='black',
                    font=('Arial', 16, 'bold')).place(x=250, y=400)
    tk.Button(formWindow, text="submit",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:confirm()).place(x=450, y=650)
def confirm():
    tk.messagebox.showinfo("message","success!!")

def Data_page():

    openWindow.destroy()
    dataWindow = tk.Tk()
    dataWindow.title("FATHY Gallery")
    dataWindow.geometry("650x400")

    #insert
    tk.Button(dataWindow, text="Insert",
             width=10, fg='black',
            font=('Arial', 16, 'bold'),command=lambda: Register()).place(x=250, y=100)
    #view
    tk.Button(dataWindow, text="View",
             width=10, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=200)
    #delete
    tk.Button(dataWindow, text="Delete",
             width=10, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=300)

    dataWindow.mainloop()

openWindow = tk.Tk()
openWindow.title("Welcome to el 7ag FATHY w law7ato")
openWindow.geometry("500x300")
tk.Label(openWindow, text="Welcome to Artify", width=20, fg='black',
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
tk.Button(openWindow, text="Login",command=lambda: Data_page(),
             width=10, fg='black',
            font=('Arial', 16, 'bold')).place(x=300, y=200)

openWindow.mainloop()
