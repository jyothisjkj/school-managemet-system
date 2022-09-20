from tkinter import*
from tkinter import ttk
import mysql.connector
mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'jyothis@97',
    database='abc_school')
mycursor=mydb.cursor()

def non_teaching():
    mycursor.execute("create table if not exists non_teaching_staff1(n_id int auto_increment primary key,n_emply_id int,n_name varchar(30),n_addr varchar(30),n_gender varchar(30),n_contact_no varchar(30),n_attendance varchar(30),n_leave varchar(30),n_salary varchar(30))")
    window=Tk()
    window.title("EMPLOYEE DETAILS")
    window.geometry("1600x1000")


    def add_value():
        
        n1=int(e1.get())
        n2=str(e2.get())
        n3=str(e3.get())
        n4=str(e4.get())
        n5=str(e5.get())
        n6=str(e6.get())
        n7=str(e7.get())
        n8=str(e8.get())
        
        mycursor.execute(f"insert into non_teaching_staff1(n_emply_id,n_name,n_addr,n_gender,n_contact_no,n_attendance,n_leave,n_salary)values({n1},'{n2}','{n3}','{n4}','{n5}','{n6}','{n7}','{n8}')")
        mydb.commit()

    def del_value():
        
        n1=int(e1.get())
        
        mycursor.execute(f"delete from non_teaching_staff1 where n_emply_id={n1}")
        mydb.commit()

    def update_value():
        
        n2=str(e2.get())
        n1=int(e1.get())
        n3=str(e3.get())
        n4=str(e4.get())
        n5=str(e5.get())
        n6=str(e6.get())
        n7=str(e7.get())
        n8=str(e8.get())
      
        mycursor.execute(f"update non_teaching_staff1 set n_name='{n2}',n_addr='{n3}',n_gender='{n4}',n_contact_no='{n5}',n_attendance='{n6}',n_leave='{n7}',n_salary='{n8}' where n_emply_id={n1}")
        mydb.commit()
        
    def fetch_value():
        
        n1=int(e1.get())
        columns=('Employee Id','Name','Address','Contact Number')
        tree=ttk.Treeview(window,columns=columns,show='headings')
        tree.heading('Employee Id',text='Employee Id')
        tree.heading('Name',text='Name')
        tree.heading('Address',text='Address')
        tree.heading('Contact Number',text='Contact Number')
        mycursor.execute(f"select n_emply_id,n_name,n_addr,n_contact_no from non_teaching_staff1 where n_emply_id={n1}")
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
        
        

        
        
    mainlabel= Label(window,text="NON TEACHING STAFF", font=("times new roman", 28), bg="light blue",fg="white")
    mainlabel.pack(side=TOP, fill=X)
    l1=Label(window,text="Employee ID",font=("arial",15))
    l2=Label(window,text="Name",font=("arial",15))
    l3=Label(window,text="Address",font=("arial",15))
    l4=Label(window,text="Gender",font=("arial",15))
    l5=Label(window,text="Contact Number",font=("arial",15))
    l6=Label(window,text="Attendance",font=("arial",15))
    l7=Label(window,text="Leave",font=("arial",15))
    l8=Label(window,text="Salary",font=("arial",15))
    l1.place(x=100,y=100)
    l2.place(x=100,y=170)
    l3.place(x=100,y=240)
    l4.place(x=100,y=310)
    l5.place(x=100,y=380)
    l6.place(x=100,y=450)
    l7.place(x=100,y=520)
    l8.place(x=100,y=590)
    
    e1=Entry(window,width=20,bd=5,font=("arial",10))
    e2=Entry(window,width=20,bd=5,font=("arial",10))
    e3=Entry(window,width=20,bd=5,font=("arial",10))
    e4=Entry(window,width=20,bd=5,font=("arial",10))
    e5=Entry(window,width=20,bd=5,font=("arial",10))
    e6=Entry(window,width=20,bd=5,font=("arial",10))
    e7=Entry(window,width=20,bd=5,font=("arial",10))
    e8=Entry(window,width=20,bd=5,font=("arial",10))
    e1.place(x=400,y=100)
    e2.place(x=400,y=170)
    e3.place(x=400,y=240)
    e4.place(x=400,y=310)
    e5.place(x=400,y=380)
    e6.place(x=400,y=450)
    e7.place(x=400,y=520)
    e8.place(x=400,y=590)
    
    b1=Button(window,width=15, font=("arial", 15),text="Add",command=add_value)
    b2=Button(window,width=15, font=("arial", 15),text="Remove",command=del_value)
    b3=Button(window,width=15, font=("arial", 15),text="Update",command=update_value)
    b4=Button(window,width=15, font=("arial", 15),text="Fetch",command=fetch_value)
    b5=Button(window,width=15,font=("arial", 15),text="CLEAR",command=Clear)
    b6= Button(window, text='Logout',fg='blue',font=('calibri 25 underline'),command=window.destroy)
    b1.place(x=10,y=650)
    b2.place(x=250,y=650)
    b3.place(x=490,y=650)
    b4.place(x=730,y=650)
    b5.place(x=950,y=650)
    b6.place(x=1100,y=100)

    window.mainloop()
    mydb.close()
