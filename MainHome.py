
from asyncio.windows_utils import Popen
from atexit import register
from cProfile import label
import email
import imghdr
from logging import root
from os import popen
from pickle import POP
from poplib import POP3
from   tkinter import *
from tkinter import font

from turtle import width
from unittest import result
from PIL import Image,ImageTk

from tkinter import messagebox
from tkinter import ttk
import os
import mysql.connector


def exit():
  status=messagebox.askyesno(title='Question',message='Do you want to exit the Login window?')
  if status == True:
    POP.destroy()
  else:
    POP.deiconify()






    

    

      
    

    


       
 









           


def show_password():
    if POP .txtpass.cget('show') == '*':
      POP  .txtpass.config(show='')
    else:
      POP  .txtpass.config(show='*')



def Login():
      window.withdraw()
      os.system("py ./LoginPage.py")
      window.deiconify()     
    

window=Tk()
window.geometry("1500x800")
window.title("Employee Management System")
window.config(bg="Black")#background color
label=Label(window,text="Employee management system",font=('times new roman',37,'bold'),fg='orange',bg='black')
#label.place(x=0,y=0,width=1500, height=50)
label.pack()
a=Button(text="LOGIN",command=Login,font=('times new roman',15,'bold'),bg='Orange',fg='blue')
a.place(relx=0.0, rely=0.06)

b=Button(text="LOGOUT",command=exit,font=('times new roman',15,'bold'),bg='Orange',fg='blue')
b.place(relx=0.92, rely=0.06)

'''button_frame = Frame( bd=2,relief=RIDGE, background='white')
button_frame.place(x=0, y=600,width=1500)'''

c=Button(text="Employee Management System \n It maintains the information about personal and official  details of the employees. It is developed to override the prevailing in the practicing manual system.\n Employment Management System is a distributed application ,developed to maintain the details of  employees working in any organization.\n This project will enhance the employee and the company to serve more quickly and efficiently. \nThis software is developed in order to computerize the activities which take more time, if  done  manually",font=('times new roman',15,'bold'),bg='orange',fg='blue',state=DISABLED)
c.place(x=0,y=700,width=1550)



image = Image.open('Images\image_2.jpg')
window.photo=ImageTk.PhotoImage(image)
        
window.title_image=Label(image=window.photo)
window.title_image.place(x=0,y=88,width=1550, height=600)

window.mainloop()