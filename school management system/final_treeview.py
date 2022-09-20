import mysql.connector
from tkinter import *
      #tkinter created
from tkinter import ttk
mydb=mysql.connector.connect(host="localhost",user="root",password="jyothis@97",database='abc_school')
mycursor=mydb.cursor()
def link_student():
    window=Tk()
    window.title("STUDENT LOGIN")
    def fun1():
        Pd=Toplevel(window)
        Pd.title("PERSONAL DETAILS")
        Pd.geometry("1500x800")
        w1=Label(Pd,text="Enter your roll number",font=("times new roman",18),bg="light green",fg="white")
        w1.place(x=50,y=200)
        def fetch_value():
            n1=int(e.get())
            columns=("Roll no","Name","Class","dob","contact","email")
            tree=ttk.Treeview(Pd,columns=columns,show="headings")
            tree.heading("Roll no",text="Roll no")
            tree.heading("Name",text="Name")
            tree.heading("Class",text="Class")
            tree.heading("dob",text="D.O.B")
            tree.heading("contact",text="Contact")
            tree.heading("email",text="E-mail")
            mycursor.execute(f"select s_roll_no,s_name,s_class,s_dob,s_contact,s_email from student where s_roll_no={n1}")
            data=mycursor.fetchall()
            for i in data:
                    tree.insert('',END,values=i)
            tree.pack()
            mydb.commit()
        e=Entry(Pd)
        e.place(x=30,y=260,width=300)
        b=Button(Pd,text="Enter",command=fetch_value)
        b.place(x=150,y=300) 



    def fun2():
        Ue=Toplevel(window)
        Ue.title("UPCOMING EXAMS")
        Ue.geometry("1500x800")
        columns=("Slno","Date","Subject name")
        tree=ttk.Treeview(Ue,columns=columns,show="headings")
        tree.heading("Slno",text="Slno")
        tree.heading("Date",text="Date")
        tree.heading("Subject name",text="Subject Name")
        tree.insert("",END,values=("1","28-12-21","Science"))
        tree.insert("",END,values=("2","29-12-21","Maths"))
        tree.insert("",END,values=("3","30-12-21","English"))
        tree.insert("",END,values=("4","31-12-21","Malayalam"))
        tree.insert("",END,values=("5","2-1-22","History"))
        tree.insert("",END,values=("6","3-1-22","Geography"))
        tree.insert("",END,values=("7","4-1-22","Hindi"))
        tree.pack()

    def fun3():
        Er=Toplevel(window)
        Er.title("EXAM RESULTS")
        Er.geometry("1500x800")
        columns=("Subject name","Marks Awarded","Total Marks","Percantage")
        tree=ttk.Treeview(Er,columns=columns,show="headings")
        tree.heading("Subject name",text="Subject name")
        tree.heading("Marks Awarded",text="Marks Awarded")
        tree.heading("Total Marks",text="Total Marks")
        tree.heading("Percantage",text="Percantage")
        tree.insert("",END,values=("Science","95","100","0.95"))
        tree.insert("",END,values=("Maths","80","100","0.80"))
        tree.insert("",END,values=("Malayalam","75","100","0.75"))
        tree.insert("",END,values=("Hindi","72","100","0.72")) 
        tree.pack()            
    def fun4():
        Tt=Toplevel(window)
        Tt.title("TIME TABLE")
        Tt.geometry("1500x800")
        columns=("Week","Period 1","Period 2","Period 3","Period 4","Period 5","Period 6","Period 7")
        tree=ttk.Treeview(Tt,columns=columns,show="headings")
        tree.heading("Week",text="Week")
        tree.heading("Period 1",text="Period 1")
        tree.heading("Period 2",text="Period 2")
        tree.heading("Period 3",text="Period 3")
        tree.heading("Period 4",text="Period 4")
        tree.heading("Period 5",text="Period 5")
        tree.heading("Period 6",text="Period 6")
        tree.heading("Period 7",text="Period 7")
        tree.insert("",END,values=("Monday","Science","Maths","English","Malayalam","Geography","Hindi","History"))
        tree.insert("",END,values=("Tuesday","Malayalam","Science","Geography","History","Hindi","English","Maths"))
        tree.insert("",END,values=("Wednessday","History ","Science ","Maths ","Geography ","Malayalam ","Hindi ","English "))
        tree.insert("",END,values=("THursday","Science","Maths","English","Malayalam","Geography","Hindi","History"))
        tree.insert("",END,values=("Friday","Hindi","Science ","Maths ","Geography ","Malayalam ","History","English"))
        tree.pack()

    def fun5():
        Cr=Toplevel(window)
        Cr.title("COMPLAINT REGISTER")
        Cr.geometry("1500x800")
        w1=Label(Cr,text="Enter your complaint",font=("times new roman",18),bg="light green",fg="white")
        w1.place(x=50,y=200)
        b=Button(Cr,text="Enter",command=abort)
        e=Entry(Cr) 
        b.place(x=150,y=300) 
        e.place(x=30,y=260,width=300)



    l=Label(window,text="STUDENT LOGIN",font=("times new roman",30),bg="light blue",fg="white") #to label a text
    l.pack(side=TOP,fill=X) 

    l1=Label(window,text="Personal Details",font=("times new roman",18),bg="light green",fg="white")
    l1.place(x=10,y=200)
    e1=Button(window,text="Enter",command=fun1,font=("times new roman",14),bg="white",fg="black")
    e1.place(x=200,y=200)
    l2=Label(window,text="Upcoming Exams",font=("times new roman",18),bg="light green",fg="white")
    l2.place(x=10,y=250)
    e2=Button(window,text="Enter",command=fun2,font=("times new roman",14),bg="white",fg="black")
    e2.place(x=200,y=250)
    l3=Label(window,text="Exam results",font=("times new roman",18),bg="light green",fg="white")
    l3.place(x=10,y=300)
    e3=Button(window,text="Enter",command=fun3,font=("times new roman",14),bg="white",fg="black")
    e3.place(x=200,y=300)
    l4=Label(window,text="Time Table",font=("times new roman",18),bg="light green",fg="white")
    l4.place(x=10,y=350)
    e4=Button(window,text="Enter",command=fun4,font=("times new roman",14),bg="white",fg="black")
    e4.place(x=200,y=350)
    l5=Label(window,text="Complaint register",font=("times new roman",14),bg="black",fg="white")
    l5.place(x=10,y=400)
    e5=Button(window,text="Enter",command=fun5,font=("times new roman",14),bg="white",fg="black")
    e5.place(x=200,y=400)


    def abort():
        window.destroy()


    lo=Button(window,text="Log out",command=abort,font=("times new roman",18),bg="black",fg="white")
    lo.place(x=1400,y=70)




    window.geometry("1500x800") 
    window.mainloop()

