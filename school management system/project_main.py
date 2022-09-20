from tkinter import*
import tkinter.messagebox
import student
import teacher_mysql_tkinter
import tkinter_non_staff
import parent_window
import final_treeview
import teacher_students
import mysql.connector



##localhost connection

mydb= mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        password= 'jyothis@97',
        database='abc_school')
mycursor=mydb.cursor()

##UI Creation

window=Tk()
window.title("SCHOOL MANAGEMENT SYSEM")
window.title("IT SOURCECODE")
window.geometry("1600x1000+0+0")
label=Label(text="ABC SCHOOL MANAGEMENT SYSTEM",font=("times new roman",35),bg="light blue",fg="white")
label.pack(side=TOP,fill=X)

##Menu Option
options = ['Admin','Teacher','Student','Parent']
clicked=StringVar()
clicked.set('Select your role')
menu=OptionMenu(window,clicked,*options)
menu.place(x=630,y=70)

## UserName and Password(Label & Entry)

user1=Label(text="USERNAME",font=("arial",23))
user1.place(x=610,y=120)
user=Entry(width=17,bd=5,font=("arial",20))
user.place(x=570,y=200)
label.pack(side=TOP ,fill=X)
user2=Label(text="PASSWORD",font=("arial",23))
user2.place(x=610,y=280)
user3=Entry(width=17,show="*",bd=5,font=("arial",20))
user3.place(x=570,y=360)

def second():
# window2
    window2=Tk()
    window2.title("IT SOURCECODE")
    window2.geometry("1600x1000+0+0")
    def distroy5():
        window2.destroy()
    def students():
        student.link_students()   
    def teachers():
        teacher_mysql_tkinter.teaching()
    def non_teaching():
        tkinter_non_staff.non_teaching()
    
        
    mainlabel= Label(window2,text="SCHOOL MANAGEMENT SYSTEM", font=("times new roman", 35), bg="light blue",fg="white")
    mainlabel.pack(side=TOP, fill=X)
    button = Button(window2,width=15, font=("arial", 20), text="STUDENTS", bg="light blue",fg="white", command=students)
    button.place(x=10, y=480)
    teachers= Button(window2, width=15, font=("arial", 20), text="TEACHERS", bg="light blue",fg="white",command=teachers)
    teachers.place(x=350, y=480)
    non_staff = Button(window2, width=20, font=("arial", 20), text="NON TEACHING STAFF", bg="light blue",fg="white",command=non_teaching)
    non_staff.place(x=680, y=480)
    link= Button(window2, width=15, font=("arial", 20), text="EXIT", bg="light blue",fg="white",command=distroy5)
    link.place(x=1080, y=480)
    window2.mainloop()
   
def distroy():
    window.destroy()
def login():
    if user.get()=="abc@admin" and user3.get()=="admin123":
        second()
        distroy()
    elif user.get()=="abc@teachers" and user3.get()=="teachers123":
        teacher_students.link_teacher_student()
        distroy()
    elif user.get()=="abc@officestaff" and user3.get()=="officestaff123":
        tkinter_non_staff.non_teaching()
        distroy()
    elif user.get()=="abc@students" and user3.get()=="students123":
        final_treeview.link_student()
        distroy()
    elif user.get()=="abc@parents" and user3.get()=="parents123":
        parent_window.link_parent()
        distroy()
    
    else:
        t=tkinter.messagebox.showinfo(title='INVALID USERNAME OR PASSWORD ',message='YOU HAVE ENTERED INVALID USERNAME OR PASSWORD')
        user.delete(0,END)
        user3.delete(0,END)

INQUIRY=Button(text="LOGIN",width=17,font=("arial",20),bg="light blue",fg="white",command=login )
INQUIRY.place(x=560 , y=480)


window.mainloop()
mydb.close()
