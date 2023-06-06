from tkinter import*
import sqlite3
from tkinter.messagebox import *
from datetime import date
con=sqlite3.connect('new_db')
cur=con.cursor()


if len(mobile)==10 and mobile.isdigit():
    cur.execute('select * from booking_history where phone=?',[mobile])
    res_tkt=cur.fetchall()

for i in res_tkt:
     name=i[0]
     gen=i[1]
     seat=i[2]
     phone=i[3]
     age=i[4]
     ref=i[5]
     phone=i[3]
     age=i[4]
     ref=i[5]
     book_date=i[6]
     travel_date=i[7]
     b_i_d=i[8]
     
cur.execute('select fair,route_id from bus where bus_id=?',[b_i_d])
res_bus=cur.fetchall()
fare=res_bus[0][0]
route_id=res_bus[0][1]
cur.execute('select s_name,e_name from route where r_id=?',[route_id])
res_route=cur.fetchall()
s_name=res_route[0][0]
route_id=res_bus[0][1]
cur.execute('select s_name,e_name from route where r_id=?',[route_id])
res_ref=cur.fetchall()
s_name=res_route[0][0]
e_name=res_route[0][1]
cur.execute('select booking_ref from booking_history where phone=?',[phone])
res_ref=cur.fetchall()
b_ref=res_ref[0][0]

Label(text="YOUR TICKET", font='Arial 12 bold', bg='blue',fg='white').grid(row=16,columnspan=12 )
Label(text="booking ref = "+b_ref,font='Arial 12 bold', fg='blue').grid(row=17,column=4)
Label(text="name = " + name, font='Arial 12 bold', fg='blue').grid(row=17, column=5)
Label(text="gender = " + gen, font='Arial 12 bold', fg='blue').grid(row=17, column=6)
Label(text="no of seats = " + str(seat), font='Arial 12 bold', fg='blue').grid(row=17, column=7)
Label(text="age = " + str(age), font='Arial 12 bold', fg='blue').grid(row=17, column=8)
Label(text="booked on = " + book_date, font='Arial 12 bold', fg='blue').grid(row=18, column=4)
Label(text="travel date = " + travel_date, font='Arial 12 bold', fg='blue').grid(row=18, column=5)
Label(text="fare = " + str(fare), font='Arial 12 bold', fg='blue').grid(row=18, column=6)
Label(text="total fare = " + str(fare*seat), font='Arial 12 bold', fg='blue').grid(row=18, column=7)
                                                           
