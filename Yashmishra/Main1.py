from tkinter import *
from subprocess import call
root = Tk()
root.geometry("700x400")
root.title("Login")
root.iconbitmap('Logo1.ico')
root.configure(background="#f0c2e0")

img = PhotoImage(file = "bg.png")
background= Label(root,image=img).place(x=0, y=0)

userbox = Entry(root)
userbox.place(x=370, y=236, height=15)

passbox = Entry(root,show="*")
passbox.place(x=370, y=255, height=15)
def log():
    global u,p
    u=userbox.get()
    p=passbox.get()
    import mysql.connector as s
    c=s.connect(host='127.0.0.1',database='hospital',user='root',password='mayk2002',auth_plugin='mysql_native_password')
    cur=c.cursor()
    cur.execute("select * from userpass where E_id=%s and password=%s;",(u,p,))
    a=cur.fetchall()
    if a!=[]:
        if a==[("admin","admin","N")]:
            call(["python","ADMIN.py"])
        else:
            call(["python","EMPLOYEE.py"])
    elif u=="" and p=="":
        ww=Label(root,text="PLEASE ENTER ID AND PASSWORD", bg="#f0c2e0", fg="purple")
        ww.place(x=260,y=340)
        root.after(3000,lambda:ww.place_forget())
    else:
        print(u,p)
        L1=Label(root,text=":(....WRONG ID OR PASSWORD ENTERED(REGISTER IF NOT THROUGH ADMIN)....:(", bg="#f0c2e0", fg="purple")
        L1.place(x=180,y=340)
        root.after(3000,lambda:L1.place_forget())
    c.close()

Button0 = Button(root, text="Login",height=1, width=18, bg="#f0c2e0", fg="purple",command=lambda:log())
Button0.place(x=290, y=300)

root.mainloop()
