from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import PIL
import os


class Employlee_Menu:
    def __init__(self,root):
        self.root=root
        root.geometry("1550x800")
        root.title("Employee Management System")
        root.configure(bg="cyan")
        
        # img=Image.open("/images/OIP.jpg")
        # img=img.resize((1550,800),Image.ANTIALIAS)
        # self.bg=ImageTk.PhotoImage(img)

        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="#ccff33")
        frame.place(x=350,y=120,width=750,height=500)

        str=Label(frame, text="Employee Menu", font=("times new roman", 20, "bold"),fg="white", bg="black")
        str.place(x=280,y=20)

      
        

        self.Photo_Update=PhotoImage(file=r"images/clean.png")
        self.Photo_Update=self.Photo_Update.subsample(10,10)

        self.Update_btn=Button(frame,text="Update",bd=0, bg='#e7feff', image=self.Photo_Update,compound=TOP,command=lambda:self.EmployeeFunction(root))
        self.Update_btn.place(width= 150, height=120, x= 120, y=100)
        
         


        # self.photo_View = PhotoImage(file=r"images/view.png")
        # self.photo_View = self.photo_View.subsample(9, 9)

        # self.View_btn = Button(frame, text='View', bd=0, bg='#e7feff', image=self.photo_View,
        #                        compound=TOP) 
        # self.View_btn.place(width= 150, height=120, x= 420, y=100)



        self.photo_Leave = PhotoImage(file=r"images/marksheet.png")
        self.photo_Leave = self.photo_Leave.subsample(5, 5)

        self.Leave_btn = Button(frame, text='Apply Leave', bd=0, bg='#e7feff', image=self.photo_Leave,
                               compound=TOP) 
        self.Leave_btn.place(width= 150, height=120, x= 420, y=100)




        self.photo_exit = PhotoImage(file=r"Images/exiticon.png")
        self.photo_exit = self.photo_exit.subsample(3, 3)

        self.Exit_btn = Button(frame, text='Exit', bd=0, bg='#e7feff', image=self.photo_exit,
                               compound=TOP,command=lambda:self.ExitFunction(root)) 
        self.Exit_btn.place(width= 150, height=120, x= 270, y=280)

    def ExitFunction(self,root):
        root.withdraw()
        os.system("py .\Homepage.py")
        root.deiconify()

    def EmployeeFunction(self,root):
        root.withdraw()
        os.system("py .\EmployeeDesign.py")
        root.deiconify()










root=Tk()
menu=Employlee_Menu(root)
root.mainloop()

  
