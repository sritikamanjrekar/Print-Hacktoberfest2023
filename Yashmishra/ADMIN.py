# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:46:10 2020

@author: asha_
"""
from subprocess import call
from tkinter import *
rt=Tk()
rt.geometry("300x350")
rt.title("Admin page")
rt.configure(bg="#8080ff")
rt.iconbitmap('Logo1.ico')
m=Label(rt,text="MENU",font='Times 16 bold italic',bg="#8080ff",fg="darkblue")
button1=Button(rt,text="PATIENT REGISTRATION",bg="#8080ff",fg="darkblue",command=lambda:call(["python","patientregis.py"]))
button2 = Button(rt, text="ROOM ALLOCATION",bg="#8080ff",fg="darkblue",command=lambda:call(["python","roomallo.py"]))
button3 = Button(rt, text="EMPLOYEE REGISTRATION",bg="#8080ff",fg="darkblue",command=lambda:call(["python","empregA.py"]))
button4 = Button(rt, text="BOOK APPOINTMENT",bg="#8080ff",fg="darkblue",command=lambda:call(["python","bookappoA.py"]))
button5 = Button(rt, text="SHOW ROOM DETAILS",bg="#8080ff",fg="darkblue",command=lambda:call(["python","detailsrommallo.py"]))
button6 = Button(rt, text="LOGOUT",bg="#8080ff",fg="darkblue",command=lambda:rt.destroy())
m.place(x=75,y=5)
button1.pack(side=TOP)
button1.place(x=80,y=50)
button2.pack(side=TOP)
button2.place(x=80,y=100)
button3.pack(side=TOP)
button3.place(x=80,y=150)
button4.pack(side=TOP)
button4.place(x=80, y=200)
button5.pack(side=TOP)
button5.place(x=80,y=250)
button6.pack(side=TOP)
button6.place(x=80,y=300)
rt.mainloop()
