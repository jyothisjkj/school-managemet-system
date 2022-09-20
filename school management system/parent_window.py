from tkinter import *
from tkinter import ttk

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="jyothis@97",database='abc_school')
mycursor=mydb.cursor()
def link_parent():
    parwindow=Tk()
    parwindow.title('Parents')
    parwindow.geometry('900x500')
    parwindow.resizable('False','False')


    bgframe=Frame(parwindow,bg='yellow',height=5,width=30)
    bgframe.grid(column=0,row=0)
    labelgreet=Label(parwindow,text='Welcome back',font=('calibri 14'))
    labelgreet.grid(column=0,row=0)

    def newwin1():
        newwindow=Toplevel(parwindow)
        newwindow.title('Student details')
        newwindow.geometry('1000x1000')
        newwindow.resizable('False','False')
        L1=Label(newwindow,text='Student Details',font=('Arial 20 underline'))
        L1.pack()
        def fetch_value():
            n1=int(e4.get())
            columns=("Roll no","Name","Class","dob","contact","email")
            tree=ttk.Treeview(newwindow,columns=columns,show="headings")
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
        #enter class
        L2=Label(newwindow,text='Enter Roll no.',font=('Arial 10'))
        L2.place(x=110,y=50)
        #class entry
        e4=Entry(newwindow)
        e4.place(x=200,y=50)
        # Confirm button
        buttonc=Button(newwindow,text='Confirm',command=fetch_value )
        buttonc.place(x=160,y=150)
        closebutton=Button(newwindow,text='close',command=newwindow.destroy)
        closebutton.pack(side='bottom')

        
    def newwin2():
        newwindow=Toplevel(parwindow)
        newwindow.title('Student details')
        newwindow.geometry('500x190')
        L1=Label(newwindow,text='Fee Details',font=('Arial 20 underline'))
        L1.pack()
        columns = ('Category','Fee')
        tree=ttk.Treeview(newwindow,height=30,columns=columns,show='headings')
        tree.heading('Category',text='Category')
        tree.heading('Fee',text='Fee')
        tree.insert('',END,values=("Tuition",'2,500'))
        tree.insert('',END,values=("Bus",'500'))
        tree.insert('',END,values=("Exam",'300'))
        tree.insert('',END,values=("Programme",'100'))
        tree.pack()
        closebutton=Button(newwindow,text='close',command=newwindow.destroy)
        closebutton.place(x=200,y=160)
    def newwin3():
        newwindow=Toplevel(parwindow)
        newwindow.title('Student details')
        newwindow.geometry('300x300')
        L1=Label(newwindow,text='Bus routes',font=('Arial 20 underline'))
        L1.pack()
        L2=Label(newwindow,text='Attingal\nAlamcode \nChirayinkeezhu \nKallambalam \nVanchiyoor \nVarkkala \nKorani \nValiakunnu ',font=('calibri 15'))
        L2.pack()
        closebutton=Button(newwindow,text='close',command=newwindow.destroy)
        closebutton.pack(side='bottom')
    def newwin4():
        newwindow=Toplevel(parwindow)
        newwindow.title('Contact details')
        newwindow.geometry('300x300')
        L1=Label(newwindow,text='Contact Details',font=('Arial 20 underline'))
        L1.pack()
        L2=Label(newwindow,text='Email : abc_admin@gmail.com\nTele no.: 9765897321\nBus : ABC School Bus\nClass Teacher : Laya\nMob. No.:9877224419',font=('calibri 15'))
        L2.pack()
        closebutton=Button(newwindow,text='close',command=newwindow.destroy)
        closebutton.pack(side='bottom')
    #Button tabs
    studentlabel=Button(parwindow,text='Student details',fg='blue',font=('calibri 25 underline'),command=newwin1)
    Feelabel = Button(parwindow,text='Fee details',fg='blue', font=('calibri 25 underline'),command=newwin2)
    Buslabel=Button(parwindow, text='Bus route',fg='blue', font=('calibri 25 underline'),command=newwin3)
    logout= Button(parwindow, text='Logout',fg='blue',font=('calibri 25 underline'),command=parwindow.destroy)
    contact= Button(parwindow, text='Contact details',fg='blue',font=('calibri 25 underline'),command=newwin4)
    #button place
    studentlabel.place(x=60,y=50)
    Feelabel.place(x=60,y=250)
    Buslabel.place(x=330,y=50)
    contact.place(x=300,y=250)
    logout.place(x=650,y=50)
    #label
    ##printing=Label(parwindow,text=database_)
    ##printing.place(x=40,y=170)


    #button configure
    parwindow.mainloop()
