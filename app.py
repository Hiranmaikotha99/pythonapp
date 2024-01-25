from tkinter import *
import tkinter as tk
from tkinter import messagebox
from db import Database

db=Database('studentmanagement.db')

def populate_list():
    students_list.delete(0, END)
    for row in db.fetch():
        students_list.insert(END, row)


def add_info():
    if StudentID_text.get()==''or First_name_text.get()== '' or Last_name_text.get()=='' or Courses_text.get()=='' or Grade_text.get()== '':
              messagebox.showerror('Required Fields','Please include all fields')
              return
    db.insert(StudentID_text.get(), First_name_text.get(),
              Last_name_text.get(), Courses_text.get(), Grade_text.get())
    students_list.delete(0, END)
    students_list.insert(END, (StudentID_text.get(), First_name_text.get(),
                            Last_name_text.get(), Courses_text.get(), Grade_text.get()))
    clear_text
    populate_list()

def select_info(event):
    try:
      global selected_info
      index = students_list.curselection()[0]
      selected_info = students_list.get(index)
      
      StudentID_entry.delete(0, END)
      StudentID_entry.insert(END, selected_info[1])
      First_name_entry.delete(0, END)
      First_name_entry.insert(END, selected_info[2])
      Last_name_entry.delete(0, END)
      Last_name_entry.insert(END, selected_info[3])
      Courses_entry.delete(0, END)
      Courses_entry.insert(END, selected_info[4])
      Grade_entry.delete(0, END)
      Grade_entry.insert(END, selected_info[5])
    except IndexError:
      pass


def delete_info():
    db.remove(selected_info[0])
    clear_text()
    populate_list()

def update_info():
    db.update(selected_info[0], StudentID_text.get(), First_name_text.get(), Last_name_text.get(), Courses_text.get(), Grade_text.get())
    populate_list()

def clear_text():
    StudentID_entry.delete(0, END)
    First_name_entry.delete(0, END)
    Last_name_entry.delete(0, END)
    Courses_entry.delete(0 ,END)
    Grade_entry.delete(0, END)
 
#craeating window object
app = Tk()
# Student ID
StudentID_text = StringVar()
StudentID_label = Label(app, text='Student ID', font=('bold', 12))
StudentID_label.grid(row=0, column=0, sticky=W)
StudentID_entry = Entry(app, textvariable=StudentID_text)
StudentID_entry.grid(row=0, column=1)

#Courses Registered": "Data Networks, Mobile Technologies, Next generation",
#Student Name
First_name_text = StringVar()
First_name_label = Label(app, text='First_Name', font=('bold',12), pady=20)
First_name_label.grid(row=0, column=2, sticky=W)
First_name_entry = Entry(app, textvariable=First_name_text)
First_name_entry.grid(row=0, column=3)
app.title('student management')
app.geometry('750x350')
#student last Name
Last_name_text = StringVar()
Last_name_label = Label(app, text='Last_Name', font=('bold',12), pady=20)
Last_name_label.grid(row=0, column=4, sticky=W)
Last_name_entry = Entry(app, textvariable=Last_name_text)
Last_name_entry.grid(row=0, column=5)
app.title('student management')
app.geometry('750x350')

#courses
Courses_text = StringVar()
Courses_label = Label(app, text='Courses Registered', font=('bold', 12))
Courses_label.grid(row=1, column=0, sticky=W)
Courses_entry = Entry(app, textvariable=Courses_text)
Courses_entry.grid(row=1, column=1)
#gardes
Grade_text = StringVar()
Grade_label = Label(app, text='Overall Grade', font=('bold', 12))
Grade_label.grid(row=1, column=2, sticky=W)
Grade_entry = Entry(app, textvariable=Grade_text)
Grade_entry.grid(row=1, column=3)

# Parts List (Listbox)
students_list = Listbox(app, height=8, width=50, border=0)
students_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=4)

# Set scroll to listbox
students_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=students_list.yview)
#bind select
students_list.bind('<<ListboxSelect>>', select_info)

#buttons-add
add_btn = Button(app, text='Add Info',width=12, command=add_info)
add_btn.grid(row =3 , column=0, pady=20)
#button-delete
delete_btn = Button(app, text='Delete Info',width=12, command=delete_info)
delete_btn.grid(row =3 , column=1)
#button-update
Update_btn = Button(app, text='Update Info',width=12, command=update_info)
Update_btn.grid(row =3 , column=2)
#clear input
Clear_btn = Button(app, text='Clear Input Info',width=12, command=clear_text)
Clear_btn.grid(row =3 , column=3)

app.title('Student Management')
app.geometry('750x350')

#Populate data
populate_list()

#start program
app.mainloop()