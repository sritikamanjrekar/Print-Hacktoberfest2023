# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:28:42 2020

@author: asha_
"""

from tkinter import *
from subprocess import call
rt=Tk()
rt.geometry("300x250")
rt.title("Employee page")
rt.iconbitmap('Logo1.ico')
rt.configure(bg="#f0c2e0")
m=Label(rt,text="MENU",font='Times 16 bold italic',fg='purple',bg="#f0c2e0")
button1=Button(rt,text="PATIENT REGISTRATION",fg='black',bg="#f0c2e0",command=lambda:call(["python","Regis.py"]))
button2 = Button(rt, text="ROOM ALLOCATION",fg='black',bg="#f0c2e0",command=lambda:call(["python","roomalloE.py"]))
button4 = Button(rt, text="BOOK APPOINTMENT",fg='black',bg="#f0c2e0",command=lambda:call(["python","AppointmentsE.py"]))
button6 = Button(rt, text="LOGOUT",fg='black',bg="#f0c2e0",command=lambda:rt.destroy())
m.place(x=75,y=5)
button1.pack(side=TOP)
button1.place(x=80,y=50)
button2.pack(side=TOP)
button2.place(x=80,y=100)
button4.pack(side=TOP)
button4.place(x=80, y=150)
button6.pack(side=TOP)
button6.place(x=80,y=200)
rt.mainloop()

