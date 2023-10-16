
import tkinter
import random as r
import mysql.connector as s
c=s.connect(host='127.0.0.1',database='hospital',user='root',password='mayk2002',auth_plugin='mysql_native_password')
rootAA=tkinter.Tk()
rootAA.geometry("500x400")
rootAA.title("APPOINTMENTS")
rootAA.config(bg="#8080ff")
rootAA.iconbitmap('Logo1.ico')
H=tkinter.Label(rootAA,text="APOINTMENTS",font="Arial 12 bold",bg="#8080ff",fg="darkblue")
H.place(x=55,y=5)
l1=tkinter.Label(rootAA,text="PATIENT ID",bg="#8080ff",fg="darkblue")
l1.place(x=20,y=30)
e1=tkinter.Entry(rootAA)
e1.place(x=100,y=30)
l2 = tkinter.Label(rootAA,text="DOCTOR ID",bg="#8080ff",fg="darkblue")
l2.place(x=20,y=60)
e2 = tkinter.Entry(rootAA)
e2.place(x=110, y=60)
l3 = tkinter.Label(rootAA,text="APPOINTMENT NO",bg="#8080ff",fg="darkblue")
l3.place(x=20,y=90)
def ww():
    global b,a,v1
    L=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10']
    cur=c.cursor()
    cur.execute("select appono from pappo;")
    b=cur.fetchall()
    a=r.choice(L)
    while(a in b):
        continue
    else:
        v1=a
    cur.close()
ww()
def setap():
    global v1,c
    t=(e1.get(),e2.get(),v1,e5.get(),e4.get(),)
    cur=c.cursor()
    cur.execute("insert into pappo values(%s,%s,%s,%s,%s);",t)
    c.commit()
    tkinter.Label(rootAA,text="Apointment set",bg="#8080ff",fg="darkblue").place(x=320,y=350)
    cur.close()

e3=tkinter.Label(rootAA,text=v1,bg="#8080ff",fg="darkblue")
e3.place(x=140,y=90)
l4 = tkinter.Label(rootAA,text="APPOINTMENT TIME(HH:MM)",bg="#8080ff",fg="darkblue")
l4.place(x=20,y=120)
e4=tkinter.Entry(rootAA)
e4.place(x=20,y=150)
l5 = tkinter.Label(rootAA,text="APPOINTMENT DATE(YYYY-MM-DD)",bg="#8080ff",fg="darkblue")
l5.place(x=20,y=180)
e5=tkinter.Entry(rootAA)
e5.place(x=20,y=210)
l6=tkinter.Label(rootAA,text="DESCRIPTION",bg="#8080ff",fg="darkblue")
l6.place(x=20,y=240)
e6=tkinter.Text(rootAA,width=20,height=3)
e6.place(x=20,y=270)
b1=tkinter.Button(rootAA,text="SET APPOINTMENT",command=lambda:setap(),bg="#8080ff",fg="darkblue")
b1.place(x=20,y=330)
b4=tkinter.Button(rootAA,text="EXIT",command=lambda:rootAA.destroy(),bg="#8080ff",fg="darkblue")
b4.place(x=200,y=330)
rootAA.mainloop()
