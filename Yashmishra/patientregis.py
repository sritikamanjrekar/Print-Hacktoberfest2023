
from tkinter import *

root = Tk()
root.title("Registration Form")
root.iconbitmap('Logo1.ico')
root.configure(bg="#8080ff")
root.geometry("500x700")

import mysql.connector as s
c=s.connect(host='127.0.0.1',database='hospital',user='root',password='mayk2002',auth_plugin='mysql_native_password') 


lable1 = Label(root, text="REGISTRATION FORM",font=('Helvetica', 30, 'bold') ,bg="#8080ff",fg="darkblue")
lable1.place(x=40, y=0)


lable2 = Label(root, text="Patient ID",font=('Helvetica', 12) ,bg="#8080ff",fg="darkblue")
lable2.place(x=215, y=80)

entry1 = Entry(root)
entry1.place(x=190, y=110)

lable3 = Label(root, text="Patient Name",font=('Helvetica', 12) ,bg="#8080ff",fg="darkblue")
lable3.place(x=200, y=140)

entry2 = Entry(root)
entry2.place(x=190, y=170)

lable4 = Label(root, text="Sex",font=('Helvetica', 12) ,bg="#8080ff",fg="darkblue")
lable4.place(x=235, y=200)

entry3 = Entry(root)
entry3.place(x=190, y=230)

lable5 = Label(root, text="D.0.B (YYYY-MM-DD)",font=('Helvetica', 12) ,bg="#8080ff",fg="darkblue")
lable5.place(x=175, y=260)

entry4 = Entry(root)
entry4.place(x=190, y=290)

lable6 = Label(root, text="Blood Group",font=('Helvetica', 12) ,bg="#8080ff",fg="darkblue")
lable6.place(x=205, y=320)

entry5 = Entry(root)
entry5.place(x=190, y=350)

lable6 = Label(root, text="Contact Number",font=('Helvetica', 12) ,bg="#8080ff",fg="darkblue")
lable6.place(x=192, y=380)

entry6 = Entry(root)
entry6.place(x=190, y=410)

lable7 = Label(root, text="E-Mail",font=('Helvetica', 12) ,bg="#8080ff",fg="darkblue")
lable7.place(x=225, y=440)

entry7 = Entry(root)
entry7.place(x=190, y=470)

lable8 = Label(root, text="Address",font=('Helvetica', 12) ,bg="#8080ff",fg="darkblue")
lable8.place(x=220, y=500)

entry8 = Entry(root)
entry8.place(x=190, y=530)

Button0 = Button(root, text="SUBMIT",height=1, width=18,bg="#8080ff",fg="darkblue",command=lambda:sub())
Button0.place(x=182, y=610)

Button1 = Button(root, text="< <  BACK",height=1, width=18,bg="#8080ff",fg="darkblue",command=lambda:root.destroy())
Button1.place(x=32, y=650)

Button2 = Button(root, text="DELETE",height=1, width=18,bg="#8080ff",fg="darkblue",command=lambda:delete())
Button2.place(x=182, y=650)

Button3 = Button(root, text="SEARCH  > >",height=1, width=18,bg="#8080ff",fg="darkblue",command=lambda:search())
Button3.place(x=332, y=650)

def sub():
    global u
    cur=c.cursor()
    u=entry1.get()
    t=(u,entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),)
    cur.execute("insert into patient values (%s,%s,%s,%s,%s,%s,%s,%s);",t)
    c.commit()
    cur.close()
    q=Label(root,text="The patient have been registered.....")
    q.place(y=550)
    root.after(3000,lambda:q.place_forget())
def search():
    global d,rtp
    rtp=Tk()
    rtp.iconbitmap("logo1.ico")
    rtp.configure(bg="#8080ff")
    rtp.geometry("300x350")
    Label(rtp,text="Enter id to search: ",bg="#8080ff",fg="darkblue").pack()
    d=Entry(rtp)
    d.place(y=30,x=90)
    Button(rtp,text="GET DETAILS",command=lambda:ddd(),bg="#8080ff",fg="darkblue").place(y=60,x=110)
    rtp.mainloop()
def ddd():
    global a
    cur=c.cursor()
    cur.execute("select * from patient where p_id=%s",(d.get(),))
    a=cur.fetchall()
    print(a)
    dfg()
    cur.close()
def dfg():
    if a!=[]:
        for jj in a:
            break
        qq=Label(rtp,text="Patient Id",bg="#8080ff",fg="darkblue")
        qq.place(x=30,y=90)
        pid1=Label(rtp,text=jj[0],bg="white",fg="darkblue")
        pid1.place(x=140,y=90)
        ww=Label(rtp,text="Patient Name",bg="#8080ff",fg="darkblue")
        ww.place(x=30,y=120)
        qw1=Label(rtp,text=jj[1],bg="white",fg="darkblue")
        qw1.place(x=140,y=120)
        vv=Label(rtp,text="sex",bg="#8080ff",fg="darkblue")
        vv.place(x=30,y=150)
        qw2=Label(rtp,text=jj[2],bg="white",fg="darkblue")
        qw2.place(x=140,y=150)
        gg=Label(rtp,text="Dob",bg="#8080ff",fg="darkblue")
        gg.place(x=30,y=180)
        qw3=Label(rtp,text=jj[3],bg="white",fg="darkblue")
        qw3.place(x=140,y=180)
        hh=Label(rtp,text="Blood group",bg="#8080ff",fg="darkblue")
        hh.place(x=30,y=210)
        qw4=Label(rtp,text=jj[4],bg="white",fg="darkblue")
        qw4.place(x=140,y=210)
        hh1=Label(rtp,text="Contact Number",bg="#8080ff",fg="darkblue")
        hh1.place(x=30,y=240)
        qw41=Label(rtp,text=jj[5],bg="white",fg="darkblue")
        qw41.place(x=140,y=240)
        hh12=Label(rtp,text="E-Mail",bg="#8080ff",fg="darkblue")
        hh12.place(x=30,y=270)
        qw412=Label(rtp,text=jj[6],bg="white",fg="darkblue")
        qw412.place(x=140,y=270)
        hh123=Label(rtp,text="Address",bg="#8080ff",fg="darkblue")
        hh123.place(x=30,y=300)
        qw4123=Label(rtp,text=jj[7],bg="white",fg="darkblue")
        qw4123.place(x=140,y=300)
    else:
        qq1=Label(rtp,text="Patient details not found or patient not registered...",bg="#8080ff",fg="darkblue")
        qq1.place(x=30,y=90)
        rtp.after(3000,lambda:qq1.place_forget())
def delete():
    global d1,rt
    rt=Tk()
    rt.iconbitmap("logo1.ico")
    rt.configure(bg="#8080ff")
    rt.geometry("300x350")
    Label(rt,text="Enter id to delete: ",bg="#8080ff",fg="darkblue").pack()
    d1=Entry(rt)
    d1.place(y=30,x=90)
    Button(rt,text="DELETE",command=lambda:ddd1(),bg="#8080ff",fg="darkblue").place(y=60,x=127)
    rt.mainloop()

def ddd1():
    cur=c.cursor()
    cur.execute("select * from patient where p_id=%s",(d1.get(),))
    a1=cur.fetchall()
    cur.close()
    if a1!=[]:
        cur=c.cursor()
        cur.execute("delete from patient where p_id=%s",(d1.get(),))
        c.commit()
        q1=Label(rt,text="Patient deleted....",bg="#8080ff",fg="darkblue")
        q1.place(x=30,y=90)
        rt.after(3000,lambda:q1.place_forget())
        cur.close()
    else:
        g=Label(rt,text="no patient found......",bg="#8080ff",fg="darkblue")
        g.place(x=30,y=90)
        rt.after(3000,lambda:g.place_forget())
root.mainloop()


                 
