####Teachers school management

from tkinter import*
from tkinter import ttk
#------------**SQL**------------#
import mysql.connector
mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'jyothis@97',
    database='abc_school')
mycursor=mydb.cursor()

#-------------------------------#
def link_teacher_student():
    window=Tk()
    window.title("Teachers Page")
    window.geometry("1200x700")
    t_name="Mrs. qwerty"
    t_address=("""xyz house
        near palarivattom

                               """)
    #---------------------------------------#
    def fetch_value():
        n1=int(e2.get())
        mycursor.execute(f"select s_roll_no,s_name,s_class,s_dob,s_contact,s_email from student where s_roll_no={n1}")
        data=mycursor.fetchall()

        for i in data:
                tree.insert('',END,values=i)

            
            
        mydb.commit()
    #-----------***---------------------------#

    def log_out():  ###LOG OUT COMMAND
        window.destroy()
    def complaint(): ### complaint box
        pass
    def clear_out():  ### clear out 
        pass

    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

    #name adress
    Tname=Label(window,text=f"WELCOME {t_name}...")         
    Taddress=Label(window,text=(f"{t_address}"))
    Tname.place(x=5,y=5)
    Taddress.place(x=5,y=20)

    #********************************************************#

    ## Frame Box

    list_frame=LabelFrame(window)
    list_frame.place(x=7,y=90,width=1180,height=500)

    l2=Label(window,text="Roll No")
    l2.place(x=400,y=350)
    e2=Entry(window)
    e2.place(x=600,y=350)
    fbutton=Button(window,text="show",command=fetch_value)
    fbutton.place(x=500,y=450)


    columns=("Roll no","Name","Class","dob","contact","email")
    tree=ttk.Treeview(list_frame,columns=columns,show="headings")
    tree.heading("Roll no",text="Roll no")
    tree.heading("Name",text="Name")
    tree.heading("Class",text="Class")
    tree.heading("dob",text="D.O.B")
    tree.heading("contact",text="Contact")
    tree.heading("email",text="E-mail")

    s_list=Label(list_frame,text="Student List",font=("Arial ",10),fg="black",bg="light grey")
    s_list.pack()

    tree.pack()
                

    #==================================================================#

    ## NAME OF SCHOOL

    school_N=Label(window,text="ABC INTERNATIONAL SCHOOL",font=("Arial Rounded MT Bold",25),fg="black",bg="light grey")
    school_N.place(x=180,y=6,width=900,height=70)

    #==================================================================# 

    ######NOTIFICATIONS
    '''####
    ####n1=Entry(window)
    ####n1.place(x=330,y=330,width=150,height=25)
    ####n2=Label(window,text="Notifications")
    ####n2.place(x=250,y=330)'''

    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

    ##complaint box
    options=["Complaint","Notifications"]
    clicked=StringVar()
    clicked.set("options")
    menu=OptionMenu(window,clicked,*options)
    menu.place(x=825,y=630)

    ##comp_label=Label(window,text="Raise a complaint..")
    comp=Entry(window)
    ##comp_label.place(x=350,y=400)
    comp.place(x=950,y=620,width=170,height=50)
    comp_button=Button(window,text="SUBMIT",command=complaint)
    comp_button.place(x=1125,y=630)

    #============================================================================#

    ##Log out
    lg_out=Button(window,text="LogOut",command=log_out) 
    lg_out.place(x=1130,y=10)



    window.mainloop()
