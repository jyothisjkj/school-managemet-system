from tkinter import*
from tkinter import ttk
import mysql.connector
mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'jyothis@97',
    database='abc_school')
mycursor=mydb.cursor()

def teaching():
    mycursor.execute("create table if not exists teacher(n_id int auto_increment primary key ,n_teacher_id int,n_name varchar(30),n_addr varchar(30) ,n_gender varchar(30),n_contact_no varchar(30),n_class int,n_subject varchar(30),n_attendance varchar(30),n_leave varchar(30),n_salary varchar(30))")
    window=Tk()
    window.title("TEACHER DETAILS")
    window.geometry("1600x1000")


    def add_value():
        n1=int(e1.get())
        n2=str(e2.get())
        n3=str(e3.get())
        n4=str(e4.get())
        n5=str(e5.get())
        n6=int(e6.get())
        n7=str(e7.get())
        n8=str(e8.get())
        n9=str(e9.get())
        n10=str(e10.get())
        
        mycursor.execute(f"insert into teacher(n_teacher_id,n_name,n_addr,n_gender,n_contact_no,n_class,n_subject,n_attendance,n_leave,n_salary)values({n1},'{n2}','{n3}','{n4}','{n5}',{n6},'{n7}','{n8}','{n9}','{n10}')")
        mydb.commit()
    def del_value():
        n1=int(e1.get())
        mycursor.execute(f"delete from teacher where n_teacher_id={n1}")
        mydb.commit()
    def update_value():
        n1=int(e1.get())
        n2=str(e2.get())
        n3=str(e3.get())
        n4=str(e4.get())
        n5=str(e5.get())
        n6=int(e6.get())
        n7=str(e7.get())
        n8=str(e8.get())
        n9=str(e9.get())
        n10=str(e10.get())
        
      
        mycursor.execute(f"update teacher set n_name='{n2}',n_addr='{n3}',n_gender='{n4}',n_contact_no='{n5}',n_class={n6},n_subject='{n7}',n_attendance='{n8}',n_leave='{n9}',n_salary='{n10}' where n_teacher_id={n1}")
        mydb.commit()
    def fetch_value():
        n1=int(e1.get())
        columns=('Name','Address','Contact Number','Class','Subject',)
        tree=ttk.Treeview(window,columns=columns,show='headings')
        tree.heading('Name',text='Name')
        tree.heading('Address',text='Address')
        tree.heading('Contact Number',text='Contact Number')
        tree.heading('Class',text='Class') 
        tree.heading('Subject',text='Subject')
        
        mycursor.execute(f"select n_name,n_addr,n_contact_no,n_class,n_subject from teacher where n_teacher_id={n1}")
        data=mycursor.fetchall()
        for i in data:
            tree.insert('',END,values=i)
        tree.pack()
        mydb.commit()
    def Clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        

        
        
    mainlabel= Label(window,text="TEACHER", font=("times new roman", 28), bg="light blue",fg="white")
    mainlabel.pack(side=TOP, fill=X)
    l1=Label(window,text="Teacher ID",font=("arial",15))
    l2=Label(window,text="Name",font=("arial",15))
    l3=Label(window,text="Address",font=("arial",15))
    l4=Label(window,text="Gender",font=("arial",15))
    l5=Label(window,text="Contact Number",font=("arial",15))
    l6=Label(window,text="Class",font=("arial",15))
    l7=Label(window,text="Subject",font=("arial",15))
    l8=Label(window,text="Attendance",font=("arial",15))
    l9=Label(window,text="Leave",font=("arial",15))
    l0=Label(window,text="Salary",font=("arial",15))
    l1.place(x=100,y=80)
    l2.place(x=100,y=130)
    l3.place(x=100,y=180)
    l4.place(x=100,y=230)
    l5.place(x=100,y=280)
    l6.place(x=100,y=330)
    l7.place(x=100,y=380)
    l8.place(x=100,y=430)
    l9.place(x=100,y=480)
    l0.place(x=100,y=530)

    e1=Entry(window,width=20,bd=5,font=("arial",10))
    e2=Entry(window,width=20,bd=5,font=("arial",10))
    e3=Entry(window,width=20,bd=5,font=("arial",10))
    e4=Entry(window,width=20,bd=5,font=("arial",10))
    e5=Entry(window,width=20,bd=5,font=("arial",10))
    e6=Entry(window,width=20,bd=5,font=("arial",10))
    e7=Entry(window,width=20,bd=5,font=("arial",10))
    e8=Entry(window,width=20,bd=5,font=("arial",10))
    e9=Entry(window,width=20,bd=5,font=("arial",10))
    e10=Entry(window,width=20,bd=5,font=("arial",10))

    e1.place(x=400,y=80)
    e2.place(x=400,y=130)
    e3.place(x=400,y=180)
    e4.place(x=400,y=230)
    e5.place(x=400,y=280)
    e6.place(x=400,y=330)
    e7.place(x=400,y=380)
    e8.place(x=400,y=430)
    e9.place(x=400,y=480)
    e10.place(x=400,y=530)

    b1=Button(window,width=15, font=("arial", 15),text="ADD",command=add_value)
    b2=Button(window,width=15, font=("arial", 15),text="REMOVE",command=del_value)
    b3=Button(window,width=15, font=("arial", 15),text="UPDATE",command=update_value)
    b4=Button(window,width=15, font=("arial", 15),text="FETCH",command=fetch_value)
    b5=Button(window,width=15,font=("arial", 15),text="CLEAR",command=Clear)
    b6= Button(window, text='Logout',fg='blue',font=('calibri 25 underline'),command=window.destroy)
        
    b1.place(x=10,y=620)
    b2.place(x=250,y=620)
    b3.place(x=490,y=620)
    b4.place(x=730,y=620)
    b5.place(x=950,y=620)
    b6.place(x=1100,y=100)

    window.mainloop()
    mydb.close()
