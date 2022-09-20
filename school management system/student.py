import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector



#mysqlconnect

mydb=mysql.connector.connect(host="localhost",user="root",password="jyothis@97",database='abc_school')
mycursor=mydb.cursor()



#tkinter
def link_students():
    mycursor.execute("create table if not exists student(s_id int primary key auto_increment,s_roll_no int,s_name varchar(30),s_class varchar(30),s_gender varchar(30),s_dob varchar(30),s_addr varchar(30),s_email varchar(30),s_contact varchar(30),s_blood_group varchar(30))")
    window=tkinter.Tk()
    window.geometry("600x600")
    window.title("STUDENT REGISTRATION")
    #ButtonFunctions
        
    def Add_Student():
        n2=int(e2.get())
        n3=str(e3.get())
        n4=str(e4.get())
        n5=str(e5.get())
        n6=str(e6.get())
        n7=str(e7.get())
        n8=str(e8.get())
        n9=str(e9.get())
        n10=str(e10.get())
        mycursor.execute(f"insert into student(s_roll_no,s_name,s_class,s_gender,s_dob,s_addr,s_email,s_contact,s_blood_group) values({n2},'{n3}','{n4}','{n5}','{n6}','{n7}','{n8}','{n9}','{n10}')")
        mydb.commit()
        
    def Delete_Student():
        n2=int(e2.get())
        mycursor.execute(f"delete from student where s_roll_no={n2}")
        mydb.commit()
        
    def Update_Student():
        n2=int(e2.get())
        n3=str(e3.get())
        n4=str(e4.get())
        n5=str(e5.get())
        n6=str(e6.get())
        n7=str(e7.get())
        n8=str(e8.get())
        n9=str(e9.get())
        n10=str(e10.get())

        mycursor.execute(f"update student set s_name='{n3}',s_class='{n4}',s_gender='{n5}',s_dob='{n6}',s_addr='{n7}',s_email='{n8}',s_contact='{n9}',s_blood_group='{n10}' where s_roll_no={n2}")
        mydb.commit()
        
    def Fetch():
        n1=int(e2.get())
        columns=('Roll No','Name','Class','Contact Number')
        tree=ttk.Treeview(window,columns=columns,show='headings')
        tree.heading('Roll No',text='Roll No')
        tree.heading('Name',text='Name')
        tree.heading('Class',text='Class')
        tree.heading('Contact Number',text='Contact Number')
        mycursor.execute(f"select s_roll_no,s_name,s_class,s_contact from student where s_roll_no={n1}")
        data=mycursor.fetchall()
        for i in data:
            tree.insert('',END,values=i)
        tree.pack()
        mydb.commit()

    def Clear():
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        
    #UI Design
        
    l=tkinter.Label(window,text="Student Details")
    l.place(x=30,y=20)

    #Label

    l2=tkinter.Label(window,text="Roll No")
    l2.place(x=50,y=90)
    l3=tkinter.Label(window,text="Name")
    l3.place(x=50,y=120)
    l4=tkinter.Label(window,text="Class")
    l4.place(x=50,y=150)
    l5=tkinter.Label(window,text="Gender")
    l5.place(x=50,y=180)
    l6=tkinter.Label(window,text="DOB")
    l6.place(x=50,y=210)
    l7=tkinter.Label(window,text="Address")
    l7.place(x=50,y=240)
    l8=tkinter.Label(window,text="email")
    l8.place(x=50,y=270)
    l9=tkinter.Label(window,text="Contact")
    l9.place(x=50,y=300)
    l10=tkinter.Label(window,text="Blood Group")
    l10.place(x=50,y=330)

    #Entry

    e2=tkinter.Entry(window)
    e2.place(x=150,y=90)
    e3=tkinter.Entry(window)
    e3.place(x=150,y=120)
    e4=tkinter.Entry(window)
    e4.place(x=150,y=150)
    e5=tkinter.Entry(window)
    e5.place(x=150,y=180)
    e6=tkinter.Entry(window)
    e6.place(x=150,y=210)
    e7=tkinter.Entry(window)
    e7.place(x=150,y=240)
    e8=tkinter.Entry(window)
    e8.place(x=150,y=270)
    e9=tkinter.Entry(window)
    e9.place(x=150,y=300)
    e10=tkinter.Entry(window)
    e10.place(x=150,y=330)

    #Button

    b=tkinter.Button(window,text="ADD",command=Add_Student)
    b.place(x=130,y=370)
    b1=tkinter.Button(window,text="DELETE",command=Delete_Student)
    b1.place(x=200,y=370)
    b2=tkinter.Button(window,text="UPDATE",command=Update_Student)
    b2.place(x=270,y=370)
    b3=tkinter.Button(window,text="FETCH",command=Fetch)
    b3.place(x=340,y=370)
    b4=tkinter.Button(window,text="Back",command=window.destroy)
    b4.place(x=500,y=10)
    b5=tkinter.Button(window,text="CLEAR",command=Clear)
    b5.place(x=410,y=370)


    window.mainloop()
