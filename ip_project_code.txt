from tkinter import *
import tkinter.messagebox
from typing import Tuple

import mysql.connector
window=Tk()
window.geometry("300x300")
window.title("Welcome")
us=StringVar()
pwd=StringVar()
var=StringVar()
fn=StringVar()
pn=StringVar()

def print1():
    user=us.get()
    pword1=pwd.get()
    desg1=var.get()
    print(f"your username is {user}")
    print(f"your password is {pword1}")
    print(f"your designation is {desg1}")


def print2():
    name=fn.get()
    phone=pn.get()
    print(f"your name is {name}")
    print(f"your phone no. is {phone}")
    tkinter.messagebox.showinfo("Welcome to Grocery Store", "successfully signed in!")

def reset_fields():
    us.set("")
    pwd.set("")
    var.set("Select Designation")
    fn.set("")
    pn.set("")

def exit1():
    exit()

def abt():
    tkinter.messagebox.showinfo("About:","Grocery Store login page")

def sql():
    desg1 = var.get()
    user=us.get()
    pword1=pwd.get()

    try:
        conn = mysql.connector.connect(
            host='localhost',
            user="root",
            password='@ntifr@gile',
            database='grocery_store'
        )

        cursor=conn.cursor()
        query="select* from user_info where username=%s and password=%s"
        cursor.execute(query,(user, pword1))
        result = cursor.fetchone()

        if result:
            tkinter.messagebox.showinfo("Login Successful","Welcome back")
            reset_fields()
            if desg1=='Store Manager':
                sales_page()
            elif desg1=='Employee':
                billpage()

        else:
            tkinter.messagebox.showinfo("Error", "Incorrect username or password")

        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        tkinter.messagebox.showerror("Error", f"Error: {err}")


def w3():
    root1=Toplevel(window)
    root1.title("sign in page")
    root1.geometry('500x500')
    lab_1=Label(root1, text="Sign in to Grocery Store",fg="white",bg="green",font=("arial",22,"bold")).pack()
    lab_2 = Label(root1, text="Username:", fg="black", bg='white', font=("arial", 18,))
    lab_2.place(x=80, y=130+30)
    entry2 = Entry(root1, textvariable=us)
    entry2.place(x=240+30, y=135+30)
    lab_3 = Label(root1, text="Password:", fg="black", bg='white', font=("arial", 18,))
    lab_3.place(x=80, y=180+30)
    entry3 = Entry(root1, textvariable=pwd)
    entry3.place(x=240+30, y=185+30)
    lab_4 = Label(root1, text="Designation:", fg="black", bg='white', font=("arial", 18,))
    lab_4.place(x=80, y=230+30)
    lab_5=Label(root1, text="Full Name:", fg="black", bg='white', font=("arial", 18,))
    lab_5.place(x=80, y=30+30)
    entry5 = Entry(root1, textvariable=fn)
    entry5.place(x=240+30, y=35+30)
    lab_6 = Label(root1, text="Phone Number:", fg="black", bg='white', font=("arial", 18,))
    lab_6.place(x=80, y=80+30)
    entry6=Entry(root1, textvariable=pn)
    entry6.place(x=240+30, y=85 + 30)

    list1 = ['Store Manager', 'Employee']
    droplist = OptionMenu(root1, var, *list1)
    var.set("Select Designation")
    droplist.place(x=240+60, y=230+30)



    def sql_add():
        name = fn.get()
        phone = pn.get() or "0000000000"
        user = us.get()
        pword1 = pwd.get()
        desg1 = var.get()
        try:
            conn1 = mysql.connector.connect(
                host='localhost',
                user="root",
                password='@ntifr@gile',
                database='grocery_store'
            )

            cursor1 = conn1.cursor()
            if len(phone)>10:
                tkinter.messagebox.showinfo("Phone number too long", "Phone number should not exceed 10 digits!")
            q1 = "insert into user_info (username, password, name, phone_no, designation) values(%s,%s,%s,%s,%s)"
            v1 = (user, pword1, name, phone, desg1)
            cursor1.execute(q1, v1)
            conn1.commit()
            tkinter.messagebox.showinfo("Sign Up Successful", "Welcome")
            reset_fields()
            sql()
            cursor1.close()
            conn1.close()
        except mysql.connector.Error as err:
            tkinter.messagebox.showerror("Error", f"Error: {err}")

    but1 = Button(root1, text="SIGN IN", fg="green", bg="white", font=("arial", 18), command=sql_add)
    but1.place(x=210, y=450)
    but2 = Button(root1, text="EXIT", fg="green", bg="white", font=("arial", 18), command=exit1)
    but2.place(x=510, y=450)


label1=Label(window, text="Welcome to Grocery Store!",fg="white",bg="green",font=("arial",22,"bold")).pack()
label2=Label(window, text="Username:", fg="black", bg='white', font=("arial",18,))

label2.place(x=80,y=130)
entry_2=Entry(window, textvariable=us)
entry_2.place(x=240,y=135)
label3=Label(window, text="Password:", fg="black", bg='white', font=("arial",18,))
label3.place(x=80,y=180)
entry_3=Entry(window, textvariable=pwd)
entry_3.place(x=240,y=185)
label4=Label(window, text="Designation:", fg="black", bg='white', font=("arial",18,))
label4.place(x=80,y=230)

menu=Menu(window)
window.config(menu=menu)
subm1=Menu(menu)
menu.add_cascade(label='File',menu=subm1)
subm1.add_command(label='Exit', command=exit1)

subm2=Menu(menu)
menu.add_cascade(label='Option',menu=subm2)
subm2.add_command(label='About', command=abt)

list1=['Store Manager','Employee']
droplist=OptionMenu(window, var, *list1)
var.set("Select Designation")
droplist.place(x=240, y=230)

button1=Button(window, text="LOGIN", fg="green", bg="white", font=("arial",18), command=sql)
button1.place(x=150,y=380)
button2=Button(window, text="EXIT", fg="green", bg="white", font=("arial",18), command=exit1)
button2.place(x=280,y=380)
button3=Button(window, text="SIGNUP", fg="green", bg="white", font=("arial",18), command=w3)
button3.place(x=210,y=450)

def billpage():
    import billpage

def sales_page():

    salesw=Toplevel(window)
    salesw.geometry("600x400")
    lab1 = Label(salesw, text='Sales Data', fg="black", bg='light blue', font=("arial", 18,)).place(x=30, y=5)
    try:
        conn2=mysql.connector.connect(
            host='localhost',
            user='root',
            password='@ntifr@gile',
            database='grocery_store'
        )
        cursor2=conn2.cursor()
        cursor2.execute("select* from sales")
        rows=cursor2.fetchall()
        header=['Sale ID', 'Total Quantity', 'Total Cost']
        for col, header in enumerate(header):
            header_label=Label(salesw, text=header, font=('Arial', 12, 'bold'))
            header_label.grid(row=0, column=col, padx=10, pady=40)
        for row_index, row in enumerate(rows, start=1):
            for col_index, value in enumerate(row):
                cell=Label(salesw, text=value, font=('Arial', 10))
                cell.grid(row=row_index, column=col_index, padx=10, pady=40)
        cursor2.close()
        conn2.close()
    except mysql.connector.Error as err:
        tkinter.messagebox.showerror("Error", f"Error: {err}")

window.mainloop()





