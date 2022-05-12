import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox
import cx_Oracl
import cx_Oracle

db=cx_Oracle.connect(user="hr",password="hr",dsn="localhost:1521/xe")


def delete():

    delete_W = tk.Tk()
    delete_W.geometry("800x500")
    delete_W.config(bg='#c7b2e9')
    T1="\"Artist\""
    T2="\"Customer\""
    T3="\"Exhibitions\""
    T4="\"Artworks\""
    T5="\"artworkPayment\""
    T6="\"likes\""
    T7="\"reviews\""
    T8="\"exhibitionsPayment\""

    tk.Button(delete_W, text="Artist",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T1)).place(x=450, y=0)


    tk.Button(delete_W, text="Customer",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T2)).place(x=450, y=50)

    tk.Button(delete_W, text="Exhibitions",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T3)).place(x=450, y=100)

    tk.Button(delete_W, text="Artworks",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T4)).place(x=450, y=150)

    tk.Button(delete_W, text="art_Payment",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T5)).place(x=450, y=200)

    tk.Button(delete_W, text="likes",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T6)).place(x=450, y=250)

    tk.Button(delete_W, text="reviews",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T7)).place(x=450, y=300)

    tk.Button(delete_W, text="ex_Payment",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T8)).place(x=450, y=350)
    def delete_row(T):
        del_W = tk.Tk()
        del_W.geometry("800x500")
        condition=tk.StringVar(del_W)
        tk.Entry(del_W, textvariable=condition, width=20, fg='black',
                    font=('Arial', 16, 'bold')).place(x=0, y=100)

        tk.Button(del_W, text="submit",
                        width=10, fg='black',
                        font=('Arial', 16, 'bold'), command=lambda: del_row(T,condition)).place(x=450, y=350)

        def del_row(T,condition):
            print(T)
            c = condition.get()
            c="\'"+c+"\'"
            print(c)
            cur = db.cursor()
            cur.execute('DELETE FROM '+T+ ' WHERE  \"username\"='+c)
            db.commit()



def view():
    vieWindow = tk.Tk()
    vieWindow.title("Review form")
    vieWindow.geometry("1100x500")
    vieWindow.config(bg='#c7b2e9')

    T1="\"Artist\""
    T2="\"Customer\""
    T3="\"Exhibitions\""
    T4="\"Artworks\""
    T5="\"artworkPayment\""
    T6="\"likes\""
    T7="\"reviews\""
    T8="\"exhibitionsPayment\""

    tk.Button(vieWindow, text="Artist",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T1)).place(x=450, y=0)


    tk.Button(vieWindow, text="Customer",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T2)).place(x=450, y=50)

    tk.Button(vieWindow, text="Exhibitions",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T3)).place(x=450, y=100)

    tk.Button(vieWindow, text="Artworks",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T4)).place(x=450, y=150)

    tk.Button(vieWindow, text="art_Payment",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T5)).place(x=450, y=200)

    tk.Button(vieWindow, text="likes",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T6)).place(x=450, y=250)

    tk.Button(vieWindow, text="reviews",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T7)).place(x=450, y=300)

    tk.Button(vieWindow, text="ex_Payment",
                    width=10, fg='black', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T8)).place(x=450, y=350)

    def view_Table(T):
        artist_W = tk.Tk()
        artist_W.geometry("1100x500")

        cur = db.cursor()
        cur.execute('select * from '+T )
        var = cur.fetchall()
        print(var)
        totalcolums = len(var[0])
        totalrows = len(var)
        for i in range(totalrows):
            for j in range(totalcolums):
                v = tk.Entry(artist_W, width=20,
                            #bg='#3F5955',
                            #fg='#0F242E',
                            borderwidth=2,
                            font=('calibri', 16, 'bold'))
                v.grid(row=i, column=j)
                v.insert(tk.END, var[i][j])
        db.commit()



def Register():

    formWindow = tk.Tk()
    formWindow.title("Registeration Form")
    formWindow.geometry("1100x800")
    formWindow.config(bg='#c7b2e9')
    tk.Label(formWindow, text="Please fill this From", width=30, fg='#a341f6',
            font=('Arial', 26, 'bold')).place(x=200, y=20)
    #first name
    tk.Label(formWindow, text="First Name", width=20, fg='#a341f6',
            font=('Arial', 16, 'bold')).place(x=0, y=100)
    fname = tk.StringVar(formWindow)
    tk.Entry(formWindow,textvariable=fname,width=20, fg='#a341f6',
            font=('Arial', 16, 'bold')).place(x=250, y=100)

    #last name
    tk.Label(formWindow, text="Last Name", width=20, fg='#a341f6',
            font=('Arial', 16, 'bold')).place(x=500, y=100)
    lname = tk.StringVar(formWindow)
    tk.Entry(formWindow,textvariable=lname,width=20, fg='#a341f6',
            font=('Arial', 16, 'bold')).place(x=750, y=100)

    #User name
    tk.Label(formWindow, text="User Name", width=20, fg='#a341f6',
            font=('Arial', 16, 'bold')).place(x=0, y=150)

    uname = tk.StringVar(formWindow)
    tk.Entry(formWindow,textvariable=uname,width=40, fg='#a341f6',
            font=('Arial', 16, 'bold')).place(x=250, y=150)

    #email
    tk.Label(formWindow, text="E-mail", width=20, fg='#a341f6',
            font=('Arial', 16, 'bold')).place(x=0, y=200)
    email = tk.StringVar(formWindow)
    tk.Entry(formWindow, textvariable=email, width=40, fg='#a341f6',
            font=('Arial', 16, 'bold')).place(x=250, y=200)

    #phone number
    tk.Label(formWindow, text="Phone Number", width=20, fg='#a341f6',
            font=('Arial', 16, 'bold')).place(x=0, y=250)
    phone = StringVar(formWindow)
    tk.Entry(formWindow, textvariable=phone,width=40, fg='#a341f6',
            font=('Arial', 16, 'bold')).place(x=250, y=250)

    #Birthday
    tk.Label(formWindow, text="Birthday", width=20, fg='#a341f6',
            font=('Arial', 16, 'bold')).place(x=0, y=300)
    cal=Calendar(formWindow, selectmode = 'day',
               year = 2020, month = 5,
               day = 22).place(x=250, y=300)

    #user type
    tk.Label(formWindow, text="User", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=595)

    var = IntVar(formWindow)

    tk.Radiobutton(formWindow, text="Artist",indicatoron=0, variable=var, value=1).place(x=250, y=600)
    tk.Radiobutton(formWindow, text="Customer",indicatoron=0, variable=var, value=2).place(x=350, y=600)

    #submit


    tk.Button(formWindow, text="submit",
                 width=10, fg='black',
                 font=('Arial', 16, 'bold'), command=lambda: [submitform(var,uname,fname,lname,phone,email,cal),formWindow.destroy()]).place(x=450, y=650)

    def submitform(var,uname,fname,lname,phone,email,cal):
        if var.get() == 1:
            artist(uname,fname,lname,phone,email,cal)
        elif var.get() == 2:
            customer()

    formWindow.mainloop()


def artist(uname,fname,lname,phone,email,cal):
    #x=int(phone.get())
    #print(x)
    #cursor = db.cursor()
    #cursor.execute('insert into "Artist" values(uname.get(),fname.get(),lname.get(), 215615,email.get())')
    #cursor.execute('INSERT INTO "Artist" ("username","firstName","lastName") VALUES("klkld","sdnjs","snjcdj")')
    #db.commit()
    u=uname.get()
    f=fname.get()
    l=lname.get()
    p=phone.get()
    e=email.get()

    cur = db.cursor()
    #cur.execute('insert into Artist(username=?, firstName=?, lastName=?, phoneNumber=?, Email=?)',(u, f, l, p, e))
    cur.execute('insert into "Artist" ("username", "firstName", "lastName", "phoneNumber", "Email") VALUES(:1, :2, :3, :4, :5)', (u, f, l, p, e))
    db.commit()



    formWindow = tk.Tk()
    formWindow.title("Artist options")
    formWindow.geometry("700x500")
    tk.Button(formWindow, text="Art",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: artwork()).place(x=250, y=100)
    tk.Button(formWindow, text="Exhibition",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: exhibition()).place(x=250, y=300)


def artwork():
    formWindow = tk.Tk()
    formWindow.title("Artist options")
    formWindow.geometry("900x700")
    tk.Label(formWindow, text="Art name", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=100)
    aname = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=100)

    tk.Label(formWindow, text="Art info", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=200)
    ainfo = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=200)
    tk.Label(formWindow, text="price", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=300)
    ap = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=300)
    tk.Label(formWindow, text="Art ID", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=400)
    aid = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=400)
            
    tk.Button(formWindow, text="submit",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:confirm()).place(x=350, y=550)
    name=aname.get()
    info=ainfo.get()
    price=ap.get()
    ID=aid.get()
    
    cur = db.cursor()
    cur.execute('insert into "Artworks" ("Art name", "Art info", "price", "Art ID") VALUES(:1, :2, :3, :4)', (name, info, price, ID))
    db.commit()

def exhibition():
    formWindow = tk.Tk()
    formWindow.title("Exhibitions")
    formWindow.geometry("1100x950")
    tk.Label(formWindow, text="Exhibition id", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=100)
    eid = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=100)

    tk.Label(formWindow, text="Exhibition name", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=200)
    ename = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=200)
    tk.Label(formWindow, text="Exhibition location", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=300)
    elocation = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=300)
    tk.Label(formWindow, text="Ticket price", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=400)
    tp = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=30, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=400)

    tk.Label(formWindow, text="Start date", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=500)
    sd = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=500)

    #last name
    tk.Label(formWindow, text="End date", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=500, y=500)
    ed = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=750, y=500)

    tk.Label(formWindow, text="Open time", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=600)
    ot = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=600)

    #last name
    tk.Label(formWindow, text="Close time", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=500, y=600)
    ct = tk.StringVar(formWindow)
    tk.Entry(formWindow,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=750, y=600)

    tk.Button(formWindow, text="submit",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:confirm()).place(x=350, y=700)
    exid=eid.get()
    exname=ename.get()
    location=elocation.get()
    ticket=tp.get()
    start=sd.get()
    end=ed.get()
    otime=ot.get()
    close=ct.get()
    
    cur = db.cursor()
    cur.execute('insert into "Exhibition" ("Exhibition id", "Exhibition name", "Exhibition location", "Ticket price", "Start date", "End date", "Open time", "Close time") VALUES(:1, :2, :3, :4, :5, :6, :7, :8)', (exid, exname, location, ticket, start, end, otime, close)
    db.commit()


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
    dataWindow.config(bg='#a341f6')
    dataWindow.geometry("650x400")

    #insert
    tk.Button(dataWindow, text="Insert",
             width=10, fg='white', bg='#dbb5fa',
            font=('Arial', 16, 'bold'), command=lambda: Register()).place(x=250, y=100)
    #view
    tk.Button(dataWindow, text="View",
             width=10, fg='white', bg='#dbb5fa',
            font=('Arial', 16, 'bold'), command=lambda: view()).place(x=250, y=200)
    #delete
    tk.Button(dataWindow, text="Delete",
             width=10, fg='white', bg='#dbb5fa',
            font=('Arial', 16, 'bold'), command=lambda: delete() ).place(x=250, y=300)

    dataWindow.mainloop()

openWindow = tk.Tk()
openWindow.title("Welcome to el 7ag FATHY w law7ato")
openWindow.geometry("500x300")
openWindow.config(bg='#dbc6ed')
tk.Label(openWindow, text="Welcome to Artify Gallery", width=20, fg='#230e34',
            font=('Arial', 16, 'bold')).place(x=120, y=20)
tk.Label(openWindow, text="Enter User Name", width=20, fg='#230e34',
            font=('Arial', 16, 'bold')).place(x=0, y=100)
name = tk.StringVar()
tk.Entry(openWindow, textvariable=name, width=20, fg='#230e34',
            font=('Arial', 16, 'bold')).place(x=240, y=100)
tk.Label(openWindow, text="Enter Password", width=20, fg='#230e34k',
            font=('Arial', 16, 'bold')).place(x=0, y=150)
passw = tk.StringVar()
tk.Entry(openWindow, textvariable=passw, width=20, fg='#230e34k',
            font=('Arial', 16, 'bold')).place(x=240, y=150)

tk.Button(openWindow, text="Login",command=lambda: Data_page(),
             width=10, fg='#230e34',
            font=('Arial', 16, 'bold')).place(x=300, y=200)


def submit(name,passw):
    if name.get()=="admin" and passw.get()=="admin":
        Data_page()
    else:
        tk.Label(openWindow, text="Invalid User Name or Password", width=50, fg='red',
                    font=('Arial', 8, 'bold')).place(x=100, y=250)


openWindow.mainloop()
