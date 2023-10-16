
import tkinter as tk
from subprocess import call
root = tk.Tk()
root.geometry("300x200")
root.title("HOSPITAL MANAGEMENT SYSTEM")
heading = tk.Label(root, text="WELCOME TO THE HOSPITAL",bg='white',fg='orange',font='Times 16 bold italic')
heading.pack()
def loga():
    global u,p
    u=userbox.get()
    p=passbox.get()
    if u=="admin" and p=="admin":
        call(["python","ADMIN.py"])
    elif u=="" and p=="":
        ww=tk.Label(root,text="PLEASE ENTER ID AND PASSWORD")
        ww.place(x=10,y=160)
        root.after(3000,lambda:ww.place_forget())
    else:
        L=tk.Label(root,text="WROUNG ID OR PASSWORD CAN BE OF EMPLOYEE")
        L.place(x=10,y=160)
        root.after(3000,lambda:L.place_forget())
def loge():
    global u,p
    u=userbox.get()
    p=passbox.get()
    import mysql.connector as s
    c=s.connect(host='127.0.0.1',database='hospital',user='root',password='mayk2002',auth_plugin='mysql_native_password')
    cur=c.cursor()
    cur.execute("select * from userpass where E_id=%s and password=%s;",(u,p,))
    a=cur.fetchall()
    if [(u,p,'N')]==a:
        call(["python","EMPLOYEE.py"])
    elif u=="" and p=="":
        qq=tk.Label(root,text="PLEASE ENTER ID AND PASSWORD")
        qq.place(x=10,y=160)
        root.after(3000,lambda:qq.place_forget())
    else:
        L1=tk.Label(root,text="WRONG ID OR PASSWORD CAN BE OF ADMIN")
        L1.place(x=10,y=160)
        root.after(3000,lambda:L1.place_forget())
    c.close()
L1=tk.Label(root,text="").pack()
username=tk.Label(root,text="USERNAME",justify="left")
username.place(x=0,y=50)
userbox = tk.Entry(root)
userbox.pack()
L1=tk.Label(root,text="").pack()
password=tk.Label(root,text="PASSWORD",justify="left") 
password.place(x=0,y=90)
passbox = tk.Entry(root,show="*")
passbox.pack()
L1=tk.Label(root,text="").pack()
u=userbox.get()
p=passbox.get()
login = tk.Button(root, text="LOGIN ADMIN",command=lambda:loga(),font="arial 8 bold")
login.place(x=30,y=130)
login = tk.Button(root, text="LOGIN EMPLOYEE",command=lambda:loge(),font="arial 8 bold")
login.place(x=120,y=130)
root.mainloop()
