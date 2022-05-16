import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox
import cx_Oracle
#Omda

db=cx_Oracle.connect(user="ART", password="password", dsn="localhost:1521/xe")



def delete():

    delete_W = tk.Tk()
    delete_W.geometry("800x500")
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
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T1,p1)).place(x=450, y=0)


    tk.Button(delete_W, text="Customer",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T2,p1)).place(x=450, y=50)

    tk.Button(delete_W, text="Exhibitions",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T3,p2)).place(x=450, y=100)

    tk.Button(delete_W, text="Artworks",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T4,p3)).place(x=450, y=150)

    tk.Button(delete_W, text="art_Payment",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T5,p4)).place(x=450, y=200)

    tk.Button(delete_W, text="likes",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T6,p3)).place(x=450, y=250)

    tk.Button(delete_W, text="reviews",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T7,p3)).place(x=450, y=300)

    tk.Button(delete_W, text="ex_Payment",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: delete_row(T8,p5)).place(x=450, y=350)
    def delete_row(T,p):
        del_W = tk.Tk()
        del_W.geometry("800x500")

        tk.Label(del_W, text="condition", width=20, fg='black',
                    font=('Arial', 16, 'bold')).place(x=0, y=100)

        condition=tk.StringVar(del_W)
        tk.Entry(del_W, textvariable=condition, width=20, fg='black',
                    font=('Arial', 16, 'bold')).place(x=200, y=100)

        tk.Button(del_W, text="submit",
                        width=10, fg='black',
                        font=('Arial', 16, 'bold'), command=lambda: del_row(T, p, condition)).place(x=450, y=350)

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
    vieWindow.geometry("1100x500")

    T1="\"Artist\""
    T2="\"Customer\""
    T3="\"Exhibitions\""
    T4="\"Artworks\""
    T5="\"artworkPayment\""
    T6="\"likes\""
    T7="\"reviews\""
    T8="\"exhibitionsPayment\""

    tk.Button(vieWindow, text="Artist",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T1)).place(x=450, y=0)


    tk.Button(vieWindow, text="Customer",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T2)).place(x=450, y=50)

    tk.Button(vieWindow, text="Exhibitions",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T3)).place(x=450, y=100)

    tk.Button(vieWindow, text="Artworks",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T4)).place(x=450, y=150)

    tk.Button(vieWindow, text="art_Payment",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T5)).place(x=450, y=200)

    tk.Button(vieWindow, text="likes",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T6)).place(x=450, y=250)

    tk.Button(vieWindow, text="reviews",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T7)).place(x=450, y=300)

    tk.Button(vieWindow, text="ex_Payment",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: view_Table(T8)).place(x=450, y=350)

    def view_Table(T):
        artist_W = tk.Tk()
        artist_W.geometry("1100x500")

        cur = db.cursor()
        cur.execute('select * from '+T )
        var = cur.fetchall() #return list of tuples
        if(len(var) > 0):
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
    tk.Label(formWindow, text="Please fill this From", width=30, fg='black',
            font=('Arial', 26, 'bold')).place(x=200, y=20)
    #first name
    tk.Label(formWindow, text="First Name", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=100)
    fname = tk.StringVar(formWindow)
    tk.Entry(formWindow,textvariable=fname,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=100)

    #last name
    tk.Label(formWindow, text="Last Name", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=500, y=100)
    lname = tk.StringVar(formWindow)
    tk.Entry(formWindow,textvariable=lname,width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=750, y=100)

    #User name
    tk.Label(formWindow, text="User Name", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=150)

    uname = tk.StringVar(formWindow)
    user=tk.Entry(formWindow,textvariable=uname,width=40, fg='black',
            font=('Arial', 16, 'bold'))
    user.place(x=250, y=150)

    #email
    tk.Label(formWindow, text="E-mail", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=200)
    email = tk.StringVar(formWindow)
    tk.Entry(formWindow, textvariable=email, width=40, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=200)

    #phone number
    tk.Label(formWindow, text="Phone Number", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=250)
    phone = StringVar(formWindow)
    tk.Entry(formWindow, textvariable=phone,width=40, fg='black',
            font=('Arial', 16, 'bold')).place(x=250, y=250)

    #Birthday
    tk.Label(formWindow, text="Birthday", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=300)
    cal = Calendar(formWindow, selectmode = 'day')

    cal.place(x=250, y=300)

    date=cal.get_date()

    #user type
    tk.Label(formWindow, text="User", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=595)

    var = IntVar(formWindow)

    tk.Radiobutton(formWindow, text="Artist",indicatoron=0, variable=var, value=1).place(x=250, y=600)
    tk.Radiobutton(formWindow, text="Customer",indicatoron=0, variable=var, value=2).place(x=350, y=600)

    #submit


    tk.Button(formWindow, text="submit",
                 width=10, fg='black',
                 font=('Arial', 16, 'bold'), command=lambda: [submitform(var,uname,fname,lname,phone,email,date, user)]).place(x=450, y=650)

    def submitform(var,uname,fname,lname,phone,email,date, user):

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
                customer(uname,fname,lname,phone,email,date)

    formWindow.mainloop()



def artist(uname,fname,lname,phone,email):

    u=uname.get()
    f=fname.get()
    l=lname.get()
    p=int(phone.get())
    e=email.get()


    cur = db.cursor()

    cur.execute('insert into "Artist" ("username", "firstName", "lastName", "phoneNumber", "Email") VALUES(:1, :2, :3, :4, :5)', (u, f, l, p, e))

    db.commit()
    formWindow = tk.Tk()
    formWindow.title("Artist options")
    formWindow.geometry("700x500")
    tk.Button(formWindow, text="Art",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: artwork(u)).place(x=250, y=100)
    tk.Button(formWindow, text="Exhibition",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda: exhibition(u)).place(x=250, y=300)




    def artwork(u):
        formWindow = tk.Tk()
        formWindow.title("Artist options")
        formWindow.geometry("900x700")



        #art name
        tk.Label(formWindow, text="Art Name", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=100)
        art_name = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=art_name,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=100)

        #art info
        tk.Label(formWindow, text="Art Info", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=500, y=100)
        art_info = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=art_info,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=750, y=100)

        #price
        tk.Label(formWindow, text="Price", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=150)

        price = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=price,width=40, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=150)


        tk.Button(formWindow, text="submit",
                        width=10, fg='black',
                        font=('Arial', 16, 'bold'), command=lambda:[submitart(art_name, art_info, price),confirm(),formWindow.destroy()]).place(x=350, y=550)

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
        formWindow.geometry("1100x950")


        #exposName
        tk.Label(formWindow, text="ExposName", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=0)
        ex_Name = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=ex_Name,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=0)

        #location
        tk.Label(formWindow, text="Location", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=50)
        location = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=location,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=50)

        #ticketPrice
        tk.Label(formWindow, text="Ticket Price", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=100)

        tprice = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=tprice,width=40, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=100)

        #startDate
        tk.Label(formWindow, text="Start Date", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=200)
        sd = Calendar(formWindow, selectmode = 'day',
                   year = 2022, month = 5,
                   day = 1)
        sd.place(x=250, y=200)

        s_date=sd.get_date()



        #endDate
        tk.Label(formWindow, text="End Date", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=400)

        ed = Calendar(formWindow, selectmode = 'day',
                   year = 2022, month = 5,
                   day = 1)
        ed.place(x=250, y=400)

        e_date=sd.get_date()

        #openTime
        tk.Label(formWindow, text="Open Time", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=500)
        open = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=open,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=500)

        #closeTime
        tk.Label(formWindow, text="Close Time", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=550)

        close = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=close,width=40, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=550)


        tk.Button(formWindow, text="submit",
                        width=10, fg='black',
                        font=('Arial', 16, 'bold'), command=lambda:[submitexpos(ex_Name, u, location, tprice, s_date, e_date, open, close),confirm(),formWindow.destroy()]).place(x=350, y=700)

        def submitexpos(ex_Name, u, location, tprice, s_date, e_date, open, close):
            cur = db.cursor()
            cur.execute('select * from "Exhibitions"')
            var = cur.fetchall()
            ex_id=len(var)+1

            n=ex_Name.get()
            l=location.get()
            t=int(tprice.get())
            o=open.get()
            c=close.get()


            cur.execute('insert into "Exhibitions" ("exhibitionID", "artistName", "exposName", "location", "ticketPrice", "startDate", "endDate", "openTime", "closeTime") VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9)', (ex_id, u, n, l, t, s_date, e_date, o, c))
            db.commit()


        formWindow.mainloop()



def customer(uname, fname, lname, phone, email, date):

    u=uname.get()
    f=fname.get()
    l=lname.get()
    p=int(phone.get())
    e=email.get()
    print("Date: "+date)
    print(type(date))
    cur = db.cursor()
    cur.execute('insert into "Customer" ("username", "firstName", "lastName", "birthDay", "phoneNumber", "Email") VALUES(:1, :2, :3, :4, :5, :6)', (u, f, l, date, p, e))
    db.commit()


    customer_Window = tk.Tk()
    customer_Window.title("Review form")
    customer_Window.geometry("1100x800")


    tk.Button(customer_Window, text="Art Payment",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:artworkPayment(u)).place(x=450, y=0)

    tk.Button(customer_Window, text="E Payment",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:exhibitionsPayment(u)).place(x=450, y=100)

    tk.Button(customer_Window, text="likes",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:likes(u)).place(x=450, y=200)

    tk.Button(customer_Window, text="Review",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:reviews(u)).place(x=450, y=300)

    tk.Button(customer_Window, text="submit",
                    width=10, fg='black',
                    font=('Arial', 16, 'bold'), command=lambda:confirm()).place(x=450, y=500)

    def artworkPayment(u):
        formWindow = tk.Tk()
        formWindow.title("Art work Payment")
        formWindow.geometry("1100x950")


        #artworkID
        tk.Label(formWindow, text="Artwork ID", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=0)
        artworkID = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=artworkID,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=0)

        #nameOnCard
        tk.Label(formWindow, text="Name On Card", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=50)
        C_Name = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=C_Name,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=50)

        #cardNumber
        tk.Label(formWindow, text="Card Number", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=100)
        cardNumber = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=cardNumber,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=100)

        #expiryDate
        tk.Label(formWindow, text="Expiry Date", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=150)

        expiryDate = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=expiryDate,width=40, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=150)


        #CVV
        tk.Label(formWindow, text="CVV", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=200)
        CVV = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=CVV,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=200)


        tk.Button(formWindow, text="submit",
                        width=10, fg='black',
                        font=('Arial', 16, 'bold'), command=lambda:[submit_artPayment(artworkID,C_Name, u, cardNumber, expiryDate, CVV),confirm(),formWindow.destroy()]).place(x=350, y=700)

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
        formWindow.geometry("1100x950")


        #exhibitionID
        tk.Label(formWindow, text="Exhibition ID", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=0)
        exhibitionID = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=exhibitionID,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=0)

        #nameOnCard
        tk.Label(formWindow, text="Name On Card", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=50)
        C_Name = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=C_Name,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=50)

        #cardNumber
        tk.Label(formWindow, text="Card Number", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=100)
        cardNumber = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=cardNumber,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=100)

        #expiryDate
        tk.Label(formWindow, text="Expiry Date", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=150)

        expiryDate = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=expiryDate,width=40, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=150)


        #CVV
        tk.Label(formWindow, text="CVV", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=200)
        CVV = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=CVV,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=200)


        tk.Button(formWindow, text="submit",
                        width=10, fg='black',
                        font=('Arial', 16, 'bold'), command=lambda:[submit_exposPayment(exhibitionID,C_Name, u, cardNumber, expiryDate, CVV),confirm(),formWindow.destroy()]).place(x=350, y=700)

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
        formWindow.geometry("1100x950")


        #artID
        tk.Label(formWindow, text="Art ID", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=0)
        artID = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=artID,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=0)

        #review
        tk.Label(formWindow, text="Review", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=50)
        review = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=review,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=50)



        tk.Button(formWindow, text="submit",
                        width=10, fg='black',
                        font=('Arial', 16, 'bold'), command=lambda:[submit_review(artID, u, review), confirm(), formWindow.destroy()]).place(x=350, y=700)

        def submit_review(artID, u, review):
            cur = db.cursor()

            i=artID.get()
            r=review.get()


            cur = db.cursor()
            cur.execute('insert into "reviews" ("username", "artID", "review") VALUES(:1, :2, :3)', (u, i, r))
            db.commit()


        formWindow.mainloop()

    def likes(u):
        formWindow = tk.Tk()
        formWindow.title("likes")
        formWindow.geometry("1100x950")


        #artID
        tk.Label(formWindow, text="Art ID", width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=0, y=0)
        artID = tk.StringVar(formWindow)
        tk.Entry(formWindow,textvariable=artID,width=20, fg='black',
                font=('Arial', 16, 'bold')).place(x=250, y=0)

        #like
        var = IntVar(formWindow)

        tk.Radiobutton(formWindow, text="like",indicatoron=0, variable=var, value=1).place(x=250, y=200)




        tk.Button(formWindow, text="submit",
                        width=10, fg='black',
                        font=('Arial', 16, 'bold'), command=lambda: [submit_like(artID, u, var), confirm(), formWindow.destroy()]).place(x=350, y=400)

        def submit_like(artID, u, var):

            i=artID.get()
            if(var.get() == 1):
                cur = db.cursor()
                cur.execute('insert into "likes" ("artID", "username", "likesNo.") VALUES(:1, :2, :3)', (i, u, l))
                db.commit()


        formWindow.mainloop()



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
            font=('Arial', 16, 'bold'), command=lambda: Register()).place(x=250, y=100)
    #view
    tk.Button(dataWindow, text="View",
             width=10, fg='black',
            font=('Arial', 16, 'bold'), command=lambda: view()).place(x=250, y=200)
    #delete
    tk.Button(dataWindow, text="Delete",
             width=10, fg='black',
            font=('Arial', 16, 'bold'), command=lambda: delete() ).place(x=250, y=300)

    dataWindow.mainloop()




openWindow = tk.Tk()
openWindow.title("Welcome to el 7ag FATHY w law7ato")
openWindow.geometry("500x300")
tk.Label(openWindow, text="Welcome to Artify Gallery", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=120, y=20)
tk.Label(openWindow, text="Enter User Name", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=100)
name = tk.StringVar()
tk.Entry(openWindow, textvariable=name, width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=240, y=100)
tk.Label(openWindow, text="Enter Password", width=20, fg='black',
            font=('Arial', 16, 'bold')).place(x=0, y=150)
passw = tk.StringVar()
tk.Entry(openWindow, textvariable=passw, show="*", width=20, fg='black',
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
