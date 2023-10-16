import random as r
import tkinter
import mysql.connector as s
conn = s.connect(user='root', password='mayk2002', host='localhost',database='hospital')
rootR=tkinter.Tk()
rootR.title("ROOM ALLOCATION")
rootR.geometry("600x360")
rootR.config(bg="#8080ff")
rootR.iconbitmap('Logo1.ico')
r_head=tkinter.Label(rootR,text="ROOM ALLOCATION",font='Airal 15 bold',bg="#8080ff",fg="darkblue")
r_head.place(x=75,y=10)
id=tkinter.Label(rootR,text="PATIENT ID",bg="#8080ff",fg="darkblue")
id.place(x=30,y=60)
P_id=tkinter.Entry(rootR)
P_id.place(x=100,y=60)
room_tl=tkinter.Label(rootR,text="ROOM TYPE",bg="#8080ff",fg="darkblue")
room_tl.place(x=30, y=100)
z=tkinter.StringVar()
room_t=tkinter.Radiobutton(rootR,text='GENERAL ROOM',value='GENERAL ROOM',variable=z,bg="#8080ff",fg="darkblue",indicator = 0)
room_t.place(x=105,y=100)
room_t=tkinter.Radiobutton(rootR,text='DELUX ROOM',value='DELUX ROOM',variable=z,bg="#8080ff",fg="darkblue",indicator = 0)
room_t.place(x=250,y=100)
room_t=tkinter.Radiobutton(rootR,text='SUPER DELUX ROOM',value='SUPER DELUX ROOM',variable=z,bg="#8080ff",fg="darkblue",indicator = 0)
room_t.place(x=380,y=100)
room_nol=tkinter.Label(rootR,text="ROOM NUMBER",bg="#8080ff",fg="darkblue")
room_nol.place(x=30,y=140)
l1=['101','102-AA','102-BB','103','104-AA','104-BB','105','206-AAA','206-BBB','206-CCC','207','208-AAA','208-BBB','208-CCC','210','211','302','304-AA','304-BB']
cur=conn.cursor()
cur.execute("select room_no from roomallo;")
b=cur.fetchall()
a=r.choice(l1)
while(a in b):
    continue
else:
    v=a
    cur.close()
room_no=tkinter.Label(rootR,bg="#8080ff",fg="darkblue",text=v)
room_no.place(x=135,y=140)
ratel=tkinter.Label(rootR, text="ROOM CHARGES",bg="#8080ff",fg="darkblue")
ratel.place(x=30, y=220)
get1=tkinter.Button(rootR,text="GET",command=lambda:get(),bg="#8080ff",fg="darkblue").place(x=200, y=220)
def up():
    global u,d2,d1,rootDE
    rootDE=tkinter.Tk()
    rootDE.geometry("250x250")
    rootDE.title("EMPLOYEE DELETION")
    rootDE.config(bg="#8080ff")
    h1=tkinter.Label(rootDE,text="ENTER PATIENT ID TO UPDATE :",bg="#8080ff",fg="darkblue")
    h1.place(x=20,y=10)
    d1=tkinter.Entry(rootDE)
    d1.place(x=20,y=35)
    h2=tkinter.Label(rootDE,text="ENTER DATE DISCHARGE TO UPDATE :",bg="#8080ff",fg="darkblue")
    h2.place(x=20,y=65)
    d2=tkinter.Entry(rootDE)
    d2.place(x=20,y=90)
    B1=tkinter.Button(rootDE,text="UPDATE",command=lambda:delling(),bg="#8080ff",fg="darkblue")
    B1.place(x=20,y=130)
    rootDE.mainloop()
def delling():
    try:
        global conn
        cur=conn.cursor()
        u=d1.get()
        cur.execute("update roomallo set Datedischarged=%s where P_id=%s;",(d2.get(),u,))
        conn.commit()
        tkinter.Label(rootDE,text="Date discharge has been updated").pack()
        cur.close()
    except:
        print("error")
def get():
    global q,m
    q=z.get()
    if q=="GENERAL ROOM":
        rate=tkinter.Label(rootR,text="6000",bg="#8080ff",fg="darkblue")
        rate.place(x=130, y=220)
        m=6000
    if q=="DELUX ROOM":
        rate=tkinter.Label(rootR,text="7000",bg="#8080ff",fg="darkblue")
        rate.place(x=130, y=220)
        m=7000
    if q=="SUPER DELUX ROOM":
        rate=tkinter.Label(rootR,text="10000",bg="#8080ff",fg="darkblue")
        rate.place(x=130, y=220)
        m=10000
def sub():
      global conn
      cur=conn.cursor()
      t=(P_id.get(),v,m,da.get(),)
      cur.execute("insert into roomallo values (%s,%s,%s,%s,null);",t)
      conn.commit()
      cur.close()
      tkinter.Label(rootR,text="Room has been alloted is"+v).pack(side=tkinter.BOTTOM)
def ROOMDETAILS():
    global n,root
    root=tkinter.Tk()
    root.geometry("250x500")
    root.title("ROOM DETAILS")
    root.config(bg="#8080ff")
    tkinter.Label(root,text="Enter the room no to know details",bg="#8080ff",fg="darkblue").pack()
    n=tkinter.Entry(root)
    n.pack()
    tkinter.Button(root,text="GET DETAILS",command=lambda:qwe(),bg="#8080ff",fg="darkblue").place(x=80,y=60)
    root.mainloop()
def qwe():
    global j,i,conn
    cur=conn.cursor()
    print(n.get())
    
    cur.execute("select * from roomallo where room_no=%s;",(n.get(),))
    j=cur.fetchall()
    print (j)
    cur.close()
    for i in j:
        print(i)
        dfg()
        
def dfg():
    cur=conn.cursor()
    cur.execute("select * from patient where p_id=%s;",(i[0],))
    tt=cur.fetchall()
    cur.close()
    if tt!=[]:
        for jj in tt:
            break
        qq=tkinter.Label(root,text="Patient Id",bg="#8080ff",fg="darkblue")
        qq.place(x=30,y=90)
        pid1=tkinter.Label(root,text=i[0],bg="white",fg="darkblue")
        pid1.place(x=140,y=90)
        ww=tkinter.Label(root,text="Patient Name",bg="#8080ff",fg="darkblue")
        ww.place(x=30,y=120)
        qw1=tkinter.Label(root,text=jj[1],bg="white",fg="darkblue")
        qw1.place(x=140,y=120)
        vv=tkinter.Label(root,text="Total Room Charge",bg="#8080ff",fg="darkblue")
        vv.place(x=30,y=150)
        qw2=tkinter.Label(root,text=i[2],bg="white",fg="darkblue")
        qw2.place(x=140,y=150)
        gg=tkinter.Label(root,text="Date Admittes",bg="#8080ff",fg="darkblue")
        gg.place(x=30,y=180)
        qw3=tkinter.Label(root,text=i[3],bg="white",fg="darkblue")
        qw3.place(x=140,y=180)
        hh=tkinter.Label(root,text="Date Discharged",bg="#8080ff",fg="darkblue")
        hh.place(x=30,y=210)
        qw4=tkinter.Label(root,text=i[4],bg="white",fg="darkblue")
        qw4.place(x=140,y=210)
da_l = tkinter.Label(rootR, text="DATE ADMITTED",bg="#8080ff",fg="darkblue")
da_l.place(x=30,y=260)
da=tkinter.Entry(rootR)
da.place(x=140,y=260)
Submit=tkinter.Button(rootR,text="SUBMIT",bg="#8080ff",fg="darkblue",command=lambda:sub())
Submit.place(x=30,y=310)
Update=tkinter.Button(rootR,text="UPDATE",command=lambda:up(),bg="#8080ff",fg="darkblue")
Update.place(x=130,y=310)
cr=tkinter.Button(rootR,text='ROOM DETAILS',bg="#8080ff",fg="darkblue",command=lambda:ROOMDETAILS())
cr.place(x=220,y=310)
ee=tkinter.Button(rootR,text="EXIT",command=lambda:rootR.destroy(),bg="#8080ff",fg="darkblue")
ee.place(x=350,y=310)
rootR.mainloop()
