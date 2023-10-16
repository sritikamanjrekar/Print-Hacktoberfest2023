
def qwe():
    global j,i,conn
    import mysql.connector as s
    conn=s.connect(user='root', password='mayk2002', host='localhost',database='hospital')
    cur=conn.cursor()
    cur.execute("select * from roomallo;")
    j=cur.fetchall()
    cur.close()
    

from tkinter import *

def show():

    listBox.insert(END, "P_id  | Roomno           | charges      | Dateadmitted | Datedischargd")
    listBox.insert(END,"")
    listBox.insert(END,"\n")
    qwe()
    for i in range(len(j)):
        listBox.insert(END,j[i][0])
        listBox.insert(END,"  |")
        listBox.insert(END,j[i][1])
        listBox.insert(END," \t\t\t |")
        listBox.insert(END,j[i][2])
        listBox.insert(END," \t\t|")
        listBox.insert(END,j[i][3])
        listBox.insert(END," \t  |")
        listBox.insert(END,j[i][3])
        listBox.insert(END,"\n")
scores = Tk()
scores.config(bg="#8080ff")
label = Label(scores, text="Room details", font = ("Arial",30),bg="#8080ff",fg="darkblue").grid(row = 0, columnspan = 3)
listBox= Text(scores,width =73,bg="#8080ff",fg="darkblue")
listBox.grid(row = 1,column= 0, columnspan =2)
showScores = Button(scores, text = "Show all details",width = 15, command = show,bg="#8080ff",fg="darkblue").grid(row = 4, column = 0)
closeButton = Button(scores, text = "Close",width = 15, command = lambda:scores.destroy(),bg="#8080ff",fg="darkblue").grid(row = 4, column = 1)

scores.mainloop()
