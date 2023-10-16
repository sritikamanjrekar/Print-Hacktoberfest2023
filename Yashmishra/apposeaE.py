from tkinter import *
import mysql.connector as s
c=s.connect(host='127.0.0.1',database='hospital',user='root',password='mayk2002',auth_plugin='mysql_native_password')
rootDE=Tk()
rootDE.geometry("300x250")
rootDE.title("APPOINTMENT SEARCH")
rootDE.config(bg="#f0c2e0")
rootDE.iconbitmap('Logo1.ico')  
d1=Entry(rootDE)
d1.place(x=50,y=35)

def ggg():
    cur=c.cursor()
    cur.execute("select * from pappo where appono=%s",(d1.get(),))
    ab=cur.fetchall()
    print(ab)
    cur.close()
    for aa1 in ab:
        cur=c.cursor()
        cur.execute("select * from patient where p_id=%s",(aa1[0],))
        abc=cur.fetchall()
        print(abc)
        cur.close()
        for aac in abc:
            qq=Label(rootDE,text="Patient Id",bg='#f0c2e0',fg="purple")
            qq.place(x=30,y=90)
            pid1=Label(rootDE,text=aa1[0],bg='white',fg="purple")
            pid1.place(x=140,y=90)
            ww=Label(rootDE,text="Pateint Name",bg='#f0c2e0',fg="purple")
            ww.place(x=30,y=120)
            qw1=Label(rootDE,text=aac[1],bg='white',fg="purple")
            qw1.place(x=140,y=120)
            vv=Label(rootDE,text="Doctor id",bg='#f0c2e0',fg="purple")
            vv.place(x=30,y=150)
            qw2=Label(rootDE,text=aa1[1],bg='white',fg="purple")
            qw2.place(x=140,y=150)
            gg=Label(rootDE,text="Appointment date",bg='#f0c2e0',fg="purple")
            gg.place(x=30,y=180)
            qw3=Label(rootDE,text=aa1[3],bg='white',fg="purple")
            qw3.place(x=140,y=180)
            hh=Label(rootDE,text="Appointment time",bg='#f0c2e0',fg="purple")
            hh.place(x=30,y=210)
            qw4=Label(rootDE,text=aa1[4],bg='white',fg="purple")
            qw4.place(x=140,y=210)



  
h1=Label(rootDE,text="ENTER APPOINTMENT NUMBER TO SEARCH: ",bg='#f0c2e0',fg="purple")
h1.place(x=20,y=10)

Button(rootDE,text="GET DETAILS",command=lambda:ggg(),bg='#f0c2e0',fg="purple").place(x=80,y=60)
rootDE.mainloop()



