from tkinter import *
import mysql.connector as s
import random as r
from subprocess import call
c=s.connect(host='127.0.0.1',database='hospital',user='root',password='mayk2002',auth_plugin='mysql_native_password')
root = Tk()
root.title("Appointment")
root.iconbitmap('Logo1.ico')
root.configure(bg="#f0c2e0")
root.geometry("500x500")
 
l1=['101','102-AA','102-BB','103','104-AA','104-BB','105','206-AAA','206-BBB','206-CCC','207','208-AAA','208-BBB','208-CCC','210','211','302','304-AA','304-BB']
cur=c.cursor()
cur.execute("select room_no from roomallo;")
b=cur.fetchall()
a=r.choice(l1)
while(a in b):
    continue
else:
    v1=a
    cur.close()
def qqq():
   global v1
   cur=c.cursor()
   cur.execute("insert into pappo values(%s,%s,%s,%s,%s)",(entry1.get(),entry2.get(),v1,entry5.get(),entry4.get(),))
   c.commit()
   s=Label(root,text="Appointment fixed....")
   s.pack(side=BOTTOM)
   root.after(3000,lambda:s.pack_forget())
   cur.close()
lable1 = Label(root, text="APPOINTMENT",font=('Helvetica', 45, 'bold') ,bg="#f0c2e0", fg="purple")
lable1.place(x=40, y=10)

  
lable2 = Label(root, text="Patient ID",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable2.place(x=50, y=160)

entry1 = Entry(root, width=46)
entry1.place(x=160, y=160)

lable3 = Label(root, text="Doctor ID",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable3.place(x=50, y=190)

entry2 = Entry(root, width=46)
entry2.place(x=160, y=190)

lable4 = Label(root, text="Appt.nt No.",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable4.place(x=50, y=220)

entry3 = Label(root,text=v1,bg="white", fg="purple")
entry3.place(x=160, y=220)

lable5 = Label(root, text="Appt.nt Time",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable5.place(x=50, y=250)

entry4 = Entry(root, width=46)
entry4.place(x=160, y=250)

lable6 = Label(root, text="Appt.nt Date",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable6.place(x=50, y=280)

entry5 = Entry(root, width=46)
entry5.place(x=160, y=280)

lable6 = Label(root, text="Sickness",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable6.place(x=50, y=310)

entry6 = Entry(root, width=46)
entry6.place(x=160, y=310, height=75)

Button1 = Button(root, text="Fix Appointment",height=2, width=18, bg="#f0c2e0", fg="purple",command=lambda:qqq())
Button1.place(x=30, y=430)


Button3 = Button(root, text="Search Appointments",height=2, width=18, bg="#f0c2e0", fg="purple",command=lambda:call(["python","apposeaE.py"]))
Button3.place(x=330, y=430)




root.mainloop()
