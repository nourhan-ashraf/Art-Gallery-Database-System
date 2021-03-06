import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox
import cx_Oracle
db=cx_Oracle.connect(user="hr", password="hr", dsn="localhost:1521/xe")

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

    p1="\"username\""
    p2="\"exhibitionID\""
    p3="\"artID\""
    p4="\"paymentID\""
    p5="\"exposPaymentID\""


    tk.Button(delete_W, text="Artist",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T1,p1)).place(x=350, y=50)


    tk.Button(delete_W, text="Customer",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T2,p1)).place(x=350, y=100)

    tk.Button(delete_W, text="Exhibitions",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T3,p2)).place(x=350, y=150)

    tk.Button(delete_W, text="Artworks",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T4,p3)).place(x=350, y=200)

    tk.Button(delete_W, text="art_Payment",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T5,p4)).place(x=350, y=250)

    tk.Button(delete_W, text="likes",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T6,p3)).place(x=350, y=300)

    tk.Button(delete_W, text="reviews",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T7,p3)).place(x=350, y=350)

    tk.Button(delete_W, text="ex_Payment",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T8,p5)).place(x=350, y=400)
    def delete_row(T,p):
        del_W = tk.Tk()
        del_W.geometry("800x500")
        del_W.config(bg='#dbc6ed')
        del_W.title("Condition form")

        tk.Label(del_W, text="condition", width=14, fg='#C679A5',
                    font=('Arial', 16, 'bold')).place(x=170, y=150)

        condition=tk.StringVar(del_W)
        tk.Entry(del_W, textvariable=condition, width=20, fg='black',
                    font=('Arial', 16, 'bold')).place(x=370, y=150)

        tk.Button(del_W, text="submit",
                        width=10, fg='black',
                        font=('Arial', 16, 'bold'), command=lambda: del_row(T, p, condition)).place(x=320, y=250)

        def del_row(T, p, condition):

            c = condition.get()
            if(p == p1):
                c="\'"+c+"\'"


            cur = db.cursor()
            cur.execute('DELETE FROM '+T+ ' WHERE '+p+' ='+c)
            db.commit()



def view():
    vieWindow = tk.Tk()
    vieWindow.title("Review form")
    vieWindow.geometry("650x400")
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
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T1)).place(x=250, y=0)


    tk.Button(vieWindow, text="Customer",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T2)).place(x=250, y=50)

    tk.Button(vieWindow, text="Exhibitions",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T3)).place(x=250, y=100)

    tk.Button(vieWindow, text="Artworks",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T4)).place(x=250, y=150)

    tk.Button(vieWindow, text="art_Payment",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T5)).place(x=250, y=200)

    tk.Button(vieWindow, text="likes",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T6)).place(x=250, y=250)

    tk.Button(vieWindow, text="reviews",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T7)).place(x=250, y=300)

    tk.Button(vieWindow, text="ex_Payment",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T8)).place(x=250, y=350)

    def view_Table(T):
        artist_W = tk.Tk()
        artist_W.geometry("1100x500")
        artist_W.config(bg='#c7b2e9')
        cur = db.cursor()
        artist_W = tk.Tk()
        artist_W.geometry("1100x500")
        cur = db.cursor()
        main_frame= Frame(artist_W)
        main_frame.pack(fill=BOTH,expand=1)
        my_canvas=Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar=tk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame= Frame(my_canvas)
        my_canvas.create_window((0,0),window=second_frame, anchor="nw")
        cur.execute('select * from '+T )
        var = cur.fetchall() #return list of tuples
        if(len(var) > 0):
            totalcolums = len(var[0])
            totalrows = len(var)
            for i in range(totalrows):
                for j in range(totalcolums):
                    v = tk.Entry(second_frame, width=20,
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
    tk.Label(formWindow, text="Please fill this From", width=30, fg='#C679A5',
            font=('Arial', 26, 'bold')).place(x=200, y=20)
    #first name
    tk.Label(formWindow, text="First Name", width=15, fg='#C679A5',
            font=('Arial', 16, 'bold')).place(x=0, y=100)
    fname = tk.StringVar(formWindow)
    tk.Entry(formWindow,textvariable=fname,width=20, fg='#C679A5',
            font=('Arial', 16, 'bold')).place(x=250, y=100)

    #last name
    tk.Label(formWindow, text="Last Name", width=15, fg='#C679A5',
            font=('Arial', 16, 'bold')).place(x=570, y=100)
    lname = tk.StringVar(formWindow)
    tk.Entry(formWindow,textvariable=lname,width=20, fg='#C679A5',
            font=('Arial', 16, 'bold')).place(x=800, y=100)

    #User name
    tk.Label(formWindow, text="User Name", width=15, fg='#C679A5',
            font=('Arial', 16, 'bold')).place(x=0, y=150)

    uname = tk.StringVar(formWindow)
    user=tk.Entry(formWindow,textvariable=uname,width=40, fg='#C679A5',
            font=('Arial', 16, 'bold'))
    user.place(x=250, y=150)

    #email
    tk.Label(formWindow, text="E-mail", width=15, fg='#C679A5',
            font=('Arial', 16, 'bold')).place(x=0, y=200)
    email = tk.StringVar(formWindow)
    tk.Entry(formWindow, textvariable=email, width=40, fg='#C679A5',
            font=('Arial', 16, 'bold')).place(x=250, y=200)

    #phone number
    tk.Label(formWindow, text="Phone Number", width=15, fg='#C679A5',
            font=('Arial', 16, 'bold')).place(x=0, y=250)
    phone = StringVar(formWindow)
    tk.Entry(formWindow, textvariable=phone,width=40, fg='#C679A5',
            font=('Arial', 16, 'bold')).place(x=250, y=250)

    #Birthday
    tk.Label(formWindow, text="Birthday", width=15, fg='#C679A5',
            font=('Arial', 16, 'bold')).place(x=0, y=300)
    global cal
    cal = Calendar(formWindow, selectmode = 'day',
               year = 2022, month = 5,
               day = 1)

    cal.place(x=250, y=300)

    #user type
    tk.Label(formWindow, text="User", width=15, fg='#C679A5',
            font=('Arial', 16, 'bold')).place(x=0, y=595)

    var = IntVar(formWindow)

    tk.Radiobutton(formWindow, text="Artist",indicatoron=0, variable=var, value=1).place(x=250, y=600)
    tk.Radiobutton(formWindow, text="Customer",indicatoron=0, variable=var, value=2).place(x=300, y=600)

    #submit


    tk.Button(formWindow, text="submit",
                 width=10, fg='white', bg='#C679A5',
                 font=('Arial', 16, 'bold'), command=lambda: [submitform(var,uname,fname,lname,phone,email, user)]).place(x=450, y=650)

    def submitform(var,uname,fname,lname,phone,email, user):
        u=uname.get()

        cur = db.cursor()
        cur.execute('select * from "Artist"')
        db.commit()
        ul = cur.fetchall()
        flag = False
        for i in ul:
            if u in i[0]:
                flag = True
                break

        if flag == True:
            user.delete(0,END)
            tk.Label(formWindow, text="Invalid User Name", width=50, fg='red',
                        font=('Arial', 8, 'bold')).place(x=750, y=150)
        else:
        formWindow.destroy()
        if var.get() == 1:
            artist(uname,fname,lname,phone,email)
        elif var.get() == 2:
            customer(uname,fname,lname,phone,email)

    formWindow.mainloop()

def artist(uname,fname,lname,phone,email):

    u=uname.get()
    f=fname.get()
    l=lname.get()
    p=phone.get()
    e=email.get()


    cur = db.cursor()
    cur.execute('insert into "Artist" ("username", "firstName", "lastName", "phoneNumber", "Email") VALUES(:1, :2, :3, :4, :5)', (u, f, l, p, e))

    db.commit()
    formWindow = tk.Tk()
    formWindow.title("Artist options")
    formWindow.geometry("700x500")
    formWindow.config(bg='#dbc6ed')
    tk.Button(formWindow, text="Art",
                    width=10, fg='white', bg = '#C679A5',
                    font=('Arial', 16, 'bold'), command=lambda: artwork(u)).place(x=280, y=150)
    tk.Button(formWindow, text="Exhibition",
                    width=10, fg='white', bg = '#C679A5',
                    font=('Arial', 16, 'bold'), command=lambda: exhibition(u)).place(x=280, y=250)


    def artwork(u):
        formWindow = tk.Tk()
        formWindow.title("Artist options")
        formWindow.geometry("900x500")
        formWindow.config(bg='#dbc6ed')

        #art name
        tk.Label(formWindow, text="Art Name", width=12, fg='white', bg='#a341f6',
                font=('Arial', 16, 'bold')).place(x=5, y=100)
        art_name = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=art_name,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=200, y=100)

        #art info
        tk.Label(formWindow, text="Art Info", width=12, fg='white', bg='#a341f6',
                font=('Arial', 16, 'bold')).place(x=460, y=100)
        art_info = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=art_info,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=650, y=100)

        #price
        tk.Label(formWindow, text="Price", width=12, fg='white', bg='#a341f6',
                font=('Arial', 16, 'bold')).place(x=5, y=150)

        price = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=price,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=200, y=150)


        tk.Button(formWindow, text="submit",
                        width=10, fg='white', bg='#a341f6',
                        font=('Arial', 16, 'bold'), command=lambda:[submitart(art_name, art_info, price),confirm(),formWindow.destroy()]).place(x=350, y=300)

        def submitart(art_name, art_info, price):
            cur = db.cursor()
            cur.execute('select * from "Artworks"')
            var = cur.fetchall()
            art_id=len(var)+1

            n=art_name.get()
            info=art_info.get()
            p=int(price.get())

            cur.execute('insert into "Artworks" ("artID", "artistName", "artworkName", "information", "price") VALUES(:1, :2, :3, :4, :5)', (art_id, u, n, info, p))
            db.commit()

        formWindow.mainloop()


    def exhibition(u):
        formWindow = tk.Tk()
        formWindow.title("Exhibitions")
        formWindow.geometry("1100x1100")
        formWindow.config(bg='#dbc6ed')

        #exposName
        tk.Label(formWindow, text="ExposName", width=15, fg='white', bg='#a341f6',
                font=('Arial', 16, 'bold')).place(x=5, y=20)
        ex_Name = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=ex_Name,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=20)

        #location
        tk.Label(formWindow, text="Location", width=15, fg='white', bg='#a341f6',
                font=('Arial', 16, 'bold')).place(x=0, y=70)
        location = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=location,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=70)

        #ticketPrice
        tk.Label(formWindow, text="Ticket Price", width=15, fg='white', bg='#a341f6',
                font=('Arial', 16, 'bold')).place(x=0, y=120)

        tprice = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=tprice,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=120)

        #startDate
        tk.Label(formWindow, text="Start Date", width=15, fg='white', bg='#a341f6',
                font=('Arial', 16, 'bold')).place(x=0, y=170)
        global sd
        sd = Calendar(formWindow, selectmode = 'day',
                   year = 2022, month = 5,
                   day = 1)
        sd.place(x=250, y=170)

        #endDate
        tk.Label(formWindow, text="End Date", width=15, fg='white', bg='#a341f6',
                font=('Arial', 16, 'bold')).place(x=0, y=320)
        global ed
        ed = Calendar(formWindow, selectmode = 'day',
                   year = 2022, month = 5,
                   day = 1)
        ed.place(x=250, y=320)

        #openTime
        tk.Label(formWindow, text="Open Time", width=15, fg='white', bg='#a341f6',
                font=('Arial', 16, 'bold')).place(x=0, y=470)
        open = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=open,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=470)

        #closeTime
        tk.Label(formWindow, text="Close Time", width=15, fg='white', bg='#a341f6',
                font=('Arial', 16, 'bold')).place(x=0, y=520)

        close = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=close,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=520)


        tk.Button(formWindow, text="submit",
                        width=10, fg='white', bg='#a341f6',
                        font=('Arial', 16, 'bold'), command=lambda:[submitexpos(ex_Name, u, location, tprice, open, close),confirm(),formWindow.destroy()]).place(x=450, y=600)

        def submitexpos(ex_Name, u, location, tprice,open, close):
            cur = db.cursor()
            cur.execute('select * from "Exhibitions"')
            var = cur.fetchall()
            ex_id=len(var)+1

            n=ex_Name.get()
            l=location.get()
            t=int(tprice.get())
            o=open.get()
            c=close.get()
            cur.execute('insert into "Exhibitions" ("exhibitionID", "artistName", "exposName", "location", "ticketPrice", "startDate", "endDate", "openTime", "closeTime") VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9)', (ex_id, u, n, l, t, sd.get_date(), ed.get_date(), o, c))
            db.commit()


        formWindow.mainloop()

def customer(uname, fname, lname, phone, email,):
    u=uname.get()
    f=fname.get()
    l=lname.get()
    p=phone.get()
    e=email.get()
    cur = db.cursor()
    cur.execute('insert into "Customer" ("username", "firstName", "lastName", "birthDay", "phoneNumber", "Email") VALUES(:1, :2, :3, :4, :5, :6)', (u, f, l, cal.get_date(), p, e))
    db.commit()


    customer_Window = tk.Tk()
    customer_Window.title("Review form")
    customer_Window.geometry("700x500")
    customer_Window.config(bg='#dbc6ed')


    tk.Button(customer_Window, text="Art Payment",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda:artworkPayment(u)).place(x=280, y=80)

    tk.Button(customer_Window, text="E Payment",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda:exhibitionsPayment(u)).place(x=280, y=180)

    tk.Button(customer_Window, text="Review",
                    width=10, fg='white', bg='#a341f6',
                    font=('Arial', 16, 'bold'), command=lambda:reviews(u)).place(x=280, y=280)

    def artworkPayment(u):
        formWindow = tk.Tk()
        formWindow.title("Art work Payment")
        formWindow.geometry("700x500")
        formWindow.config(bg='#dbc6ed')

        #artworkID
        tk.Label(formWindow, text="Artwork ID", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=10)
        artworkID = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=artworkID,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=10)

        #nameOnCard
        tk.Label(formWindow, text="Name On Card", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=60)
        C_Name = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=C_Name,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=60)

        #cardNumber
        tk.Label(formWindow, text="Card Number", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=110)
        cardNumber = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=cardNumber,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=110)

        #expiryDate
        tk.Label(formWindow, text="Expiry Date", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=160)

        expiryDate = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=expiryDate,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=160)


        #CVV
        tk.Label(formWindow, text="CVV", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=210)
        CVV = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=CVV,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=210)


        tk.Button(formWindow, text="submit",
                        width=30, fg='black', bg='#C679A5',
                        font=('Arial', 16, 'bold'), command=lambda:[submit_artPayment(artworkID,C_Name, u, cardNumber, expiryDate, CVV),confirm(),formWindow.destroy()]).place(x=135, y=300)

        def submit_artPayment(artworkID,C_Name, u, cardNumber, expiryDate, CVV):
            cur = db.cursor()
            cur.execute('select * from "artworkPayment"')
            var = cur.fetchall()
            pay_id=len(var)+1

            i=artworkID.get()
            cn=C_Name.get()
            num=cardNumber.get()
            eDate=expiryDate.get()
            cvv=CVV.get()

            print(pay_id,i,cn,num,eDate,cvv)


            cur.execute('insert into "artworkPayment" ("paymentID", "username", "artworkID", "nameOnCard", "cardNumber", "expiryDate", "CVV") VALUES(:1, :2, :3, :4, :5, :6, :7)', (pay_id, u, i, cn, num, eDate, cvv))
            db.commit()


        formWindow.mainloop()

    def exhibitionsPayment(u):
        formWindow = tk.Tk()
        formWindow.title("exhibitions Payment")
        formWindow.geometry("700x500")
        formWindow.config(bg='#dbc6ed')


        #exhibitionID
        tk.Label(formWindow, text="Exhibition ID", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=10)
        exhibitionID = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=exhibitionID,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=10)

        #nameOnCard
        tk.Label(formWindow, text="Name On Card", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=60)
        C_Name = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=C_Name,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=60)

        #cardNumber
        tk.Label(formWindow, text="Card Number", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=110)
        cardNumber = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=cardNumber,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=110)

        #expiryDate
        tk.Label(formWindow, text="Expiry Date", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=160)

        expiryDate = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=expiryDate,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=160)


        #CVV
        tk.Label(formWindow, text="CVV", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=210)
        CVV = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=CVV,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=210)


        tk.Button(formWindow, text="submit",
                        width=30, fg='black', bg='#C679A5',
                        font=('Arial', 16, 'bold'), command=lambda:[submit_exposPayment(exhibitionID,C_Name, u, cardNumber, expiryDate, CVV),confirm(),formWindow.destroy()]).place(x=135, y=300)

        def submit_exposPayment(exhibitionID,C_Name, u, cardNumber, expiryDate, CVV):
            cur = db.cursor()
            cur.execute('select * from "exhibitionsPayment"')
            var = cur.fetchall()
            pay_id=len(var)+1

            i=exhibitionID.get()
            cn=C_Name.get()
            num=cardNumber.get()
            eDate=expiryDate.get()
            cvv=CVV.get()



            cur.execute('insert into "exhibitionsPayment" ("exposPaymentID", "username", "exhibitionID", "nameOnCard", "cardNumber", "expiryDate", "CVV") VALUES(:1, :2, :3, :4, :5, :6, :7)', (pay_id, u, i, cn, num, eDate, cvv))
            db.commit()


        formWindow.mainloop()

    def reviews(u):
        formWindow = tk.Tk()
        formWindow.title("exhibitions Payment")
        formWindow.geometry("700x500")
        formWindow.config(bg='#dbc6ed')

        #artID
        tk.Label(formWindow, text="Art ID", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=10)
        artID = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=artID,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=10)

        #review
        tk.Label(formWindow, text="Review", width=15, fg='white', bg='#C679A5',
                font=('Arial', 16, 'bold')).place(x=5, y=60)
        review = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=review,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=60)



        tk.Button(formWindow, text="submit",
                        width=30, fg='black' , bg='#C679A5',
                        font=('Arial', 16, 'bold'), command=lambda:[submit_review(artID, u, review), confirm(), formWindow.destroy()]).place(x=135, y=160)

        def submit_review(artID, u, review):
            cur = db.cursor()

            i=artID.get()
            r=review.get()
            cur = db.cursor()
            cur.execute('insert into "reviews" ("username", "artID", "review") VALUES(:1, :2, :3)', (u, i, r))
            db.commit()


        formWindow.mainloop()

def confirm():
    tk.messagebox.showinfo("message","success!!")

def Data_page():

    openWindow.destroy()
    dataWindow = tk.Tk()
    dataWindow.title("FATHY Gallery")
    dataWindow.config(bg='#dbc6ed')
    dataWindow.geometry("650x400")

    #insert
    tk.Button(dataWindow, text="Insert",
             width=10, fg='white', bg='#C679A5',
            font=('Arial', 16, 'bold'), command=lambda: Register()).place(x=250, y=80)
    #view
    tk.Button(dataWindow, text="View",
             width=10, fg='white', bg='#C679A5',
            font=('Arial', 16, 'bold'), command=lambda: view()).place(x=250, y=180)
    #delete
    tk.Button(dataWindow, text="Delete",
             width=10, fg='white', bg='#C679A5',
            font=('Arial', 16, 'bold'), command=lambda: delete()).place(x=250, y=280)

    dataWindow.mainloop()

openWindow = tk.Tk()
openWindow.title("Welcome to el 7ag FATHY w law7ato")
openWindow.geometry("500x300")
openWindow.config(bg='#dbc6ed')
tk.Label(openWindow, text="Welcome to Artify Gallery", width=20, fg='#230e34',
            font=('Arial', 16, 'bold')).place(x=120, y=20)
tk.Label(openWindow, text="Enter User Name", width=15, fg='#230e34',
            font=('Arial', 16, 'bold')).place(x=0, y=100)
name = tk.StringVar()
tk.Entry(openWindow, textvariable=name, width=20, fg='#230e34',
            font=('Arial', 16, 'bold')).place(x=240, y=100)
tk.Label(openWindow, text="Enter Password", width=15, fg='#230e34',
            font=('Arial', 16, 'bold')).place(x=0, y=150)
passw = tk.StringVar()
tk.Entry(openWindow, textvariable=passw, show="*", width=20, fg='#230e34',
            font=('Arial', 16, 'bold')).place(x=240, y=150)

tk.Button(openWindow, text="Login",command=lambda: submit(name, passw),
             width=10, fg='black',
            font=('Arial', 16, 'bold')).place(x=300, y=200)


def submit(name, passw):
    if name.get()=="admin" and passw.get()=="admin":
        Data_page()
    else:
        tk.Label(openWindow, text="Invalid User Name or Password", width=50, fg='red',
                    font=('Arial', 8, 'bold')).place(x=100, y=250)


openWindow.mainloop()
