from tkinter import *
from tkinter import ttk
from types import NoneType
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from numpy import logical_not
from tkcalendar import DateEntry
from tkinter import simpledialog
from tkinter.simpledialog import SimpleDialog,askinteger
import re
from datetime import date

class EmpLeave:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee management system")
        self.root.config(bg="light blue")

        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='blue',bg='white')
        lbl_title.place(x=0,y=0,width=1500, height=50)


        btnback=Button(root,text="Back",font=("times new roman", 10, "bold"),relief=RIDGE,fg="white",bg="black",command=lambda:self.ExitFunction(root))
        btnback.place(x=5,y=5,width=70,height=40)

        img1=Image.open(r"Images\login.jpg ")
        img1=img1.resize((50, 50), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image = self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=210,y=0, width=100, height=50)

        img_frame=Frame(self.root,bg="blue")
        img_frame.place(x=0,y=55,width=1380,height=70)

         ####button apply###########
        btnapply=Button(img_frame,text="apply",command=self.apply,font=('times new roman',15,'bold'),width=13,bg='orange',fg='black')
        btnapply.place(relx=0.10,rely=0.10)

        ####button leave balance###########
        btnleave_balance=Button(img_frame,text="Leave Balance",command=self.LeaveBalance,font=('times new roman',15,'bold'),width=13,bg='orange',fg='black')
        btnleave_balance.place(relx=0.40,rely=0.10)

        ####button all leavestatus###########
        btnleave_status=Button(img_frame,text="Leave Status",command=self.EmployeeLeaveHistory,font=('times new roman',15,'bold'),width=13,bg='orange',fg='black')
        btnleave_status.place(relx=0.70,rely=0.10)


    def apply(self):
      leave_frame=Frame(self.root,bg="white")
      leave_frame.place(x=270,y=280,width=650,height=200)

      #empid
      lbl_EmpId=Label(leave_frame,text="Emp Id",font=('arial','11','bold',),bg='white' )
      lbl_EmpId.grid(row=0,column=0,padx=2,sticky=W,pady=5)

      self.txt_EmpId=ttk.Entry(leave_frame,width=22,font=('arial','11','bold'),)
      self.txt_EmpId.grid(row=0,column=1,sticky=W,padx=5,pady=5)

      #leave type
      lbl_leavetype=Label(leave_frame,text="Leavetype",font=('arial','11','bold',),bg='white' )
      lbl_leavetype.grid(row=1,column=0,padx=2,sticky=W,pady=5)

      self.combo_leavetype=ttk.Combobox(leave_frame,font=('arial','11','bold'),width=20,state="readonly")
      self.combo_leavetype[ 'value']=('Select','CL','Maternity_leave')
      self.combo_leavetype.current()
      self.combo_leavetype.grid(row=1, column=1, padx=2, pady=5, sticky=W)

      #no of days
      lbl_No_of_days=Label(leave_frame,text="No_Of_Days",font=('arial','11','bold',),bg='white' )
      lbl_No_of_days.grid(row=2,column=0,padx=2,sticky=W,pady=5)

      self.txt_No_of_days=ttk.Entry(leave_frame,width=22,font=('arial','11','bold'),)
      self.txt_No_of_days.grid(row=2,column=1,sticky=W,padx=5,pady=5)

      #callback and validation register
      validate_Days=self.root.register(self.checkDays)
      self.txt_No_of_days.config(validate='key',validatecommand=(validate_Days,'%P'))

      # #leave available
      # lbl_leaveavailable=Label(leave_frame,text="Leave Available",font=('arial','11','bold',),bg='white' )
      # lbl_leaveavailable.grid(row=3,column=0,padx=2,sticky=W,pady=5)

      # self.txt_leaveavailable=ttk.Entry(leave_frame,width=22,font=('arial','11','bold'),)
      # self.txt_leaveavailable.grid(row=3,column=1,sticky=W,padx=5,pady=5)

      # #callback and validation register
      # validate_leaveAvailabel=self.root.register(self.checkLeaveAvailable)
      # self.txt_leaveavailable.config(validate='key',validatecommand=(validate_leaveAvailabel,'%P'))

      #leave reason
      lbl_leavereason=Label(leave_frame,text="Leave Reason",font=('arial','11','bold',),bg='white' )
      lbl_leavereason.grid(row=3,column=0,padx=2,sticky=W,pady=5)

      self.combo_leavereason=ttk.Combobox(leave_frame,font=('arial','11','bold'),width=20,state="readonly")
      self.combo_leavereason[ 'value']=('Select','Relatives Wedding','not feeling well')
      self.combo_leavereason.current()
      self.combo_leavereason.grid(row=3, column=1, padx=2, pady=5, sticky=W)
       
      #available on
      lbl_applied_on=Label(leave_frame,text="Applied On",font=('arial','11','bold',),bg='white' )
      lbl_applied_on.grid(row=0,column=2,padx=2,sticky=W,pady=5)
        
       
      self.txt_applied_on=DateEntry(leave_frame,selectmode='day',width=22,font=('arial','11','bold'),date_pattern='d/m/yy')
      self.txt_applied_on.grid(row=0,column=3,sticky=W,padx=5,pady=5)

      #leave from
      lbl_leave_from=Label(leave_frame,text="Leave From",font=('arial','11','bold',),bg='white' )
      lbl_leave_from.grid(row=1,column=2,padx=2,sticky=W,pady=5)

      self.txt_leave_from=DateEntry(leave_frame,selectmode='day',width=22,font=('arial','11','bold'),date_pattern='d/m/yy')
      self.txt_leave_from.grid(row=1,column=3,sticky=W,padx=5,pady=5)

       #leave To
      lbl_leave_to=Label(leave_frame,text="Leave To",font=('arial','11','bold',),bg='white' )
      lbl_leave_to.grid(row=2,column=2,padx=2,sticky=W,pady=5)

      self.txt_leave_to=DateEntry(leave_frame,selectmode='day',width=22,font=('arial','11','bold'),date_pattern='d/m/yy')
      self.txt_leave_to.grid(row=2,column=3,sticky=W,padx=5,pady=5)

      ####button submit###########
      btnsubmit=Button(leave_frame,text="Submit",command=self.apply_leave_data,font=('times new roman',15,'bold'),width=13,bg='blue',fg='black')
      btnsubmit.grid(row=4,column=1,padx=10,pady=5)

      ''' ####button all leave###########
        btnallLeave=Button(leave_frame,text="Leave history",font=('times new roman',15,'bold'),command=self.EmployeeLeaveHistory,width=13,bg='blue',fg='black')
        btnallLeave.grid(row=4,column=3,padx=10,pady=5)'''

    def ExitFunction(self,root):
        root.withdraw()
        os.system("py .\EmployeeMenu.py")
        root.deiconify()

    ###############apply leave##################
    def apply_leave_data(self):

      global emp_id

      temp=re.findall(r'\d+', str(self.txt_leave_from))
      res= list(map(int,temp))

      temp1=re.findall(r'\d+', str(self.txt_leave_to))
      res1=list(map(int,temp1))

      date1,date2,date3=str(self.txt_leave_from.get_date()).split('-')
      year1=int(date1)
      month1=int(date2)
      day1=int(date3)

      date4,date5,date6=str(self.txt_leave_to.get_date()).split('-')
      year2=int(date4)
      month2=int(date5)
      day2=int(date6)

      date_from=date(year1,month1,day1)
      date_to=date(year2,month2,day2)

      date_calc=(date_to-date_from).days+1
      # date1=date(res[0], res[1], res[2])
      # date2=date(res1[0], res1[1], res1[2])
      # date3=(date2-date1).days+1

  
      if str(date_calc) == self.txt_No_of_days.get():
         today = date.today()
         global date_current
         date_current = today.strftime("%d/%m/%Y")

         con=mysql.connector.connect(host='localhost',database='employee management',user='pajju',password='1234')
         cur=con.cursor()
         cur.execute(f'select CL from tblleavestructure where emp_id="{self.txt_EmpId.get()}"')
         while True:
            row=cur.fetchone()
            print('///')
            row1=str(row[0])
            print('---')
            print(row1)
            print('***')
            balance1=row1

            break

         con=mysql.connector.connect(host='localhost',database='employee management',user='pajju',password='1234')
         cur=con.cursor()
         cur.execute(f'select Maternity_leave from tblleavestructure where emp_id= "{self.txt_EmpId.get()}"')
         while True:
            row=cur.fetchone()
            
            balance2=str(row[0])
            break
         
         
        
         if self.combo_leavetype.get() == "CL":
            if int(balance1) >= int(self.txt_No_of_days.get()):
               cur.execute('insert into tblleavedetails values(%s,%s,%s,%s,%s,%s,%s,"pending")',(
                          self.txt_EmpId.get(),
                          self.combo_leavetype.get(),
                          self.txt_No_of_days.get(),
                          #self.txt_leaveavailable.get(),
                          self.combo_leavereason.get(),
                          self.txt_applied_on.get(),
                          self.txt_leave_from.get(),
                          self.txt_leave_to.get()
                          
                ))
               con.commit()
               con.close()
               messagebox.showinfo("success","Employee has successfully applied leave")
            else:
               messagebox.showerror("CL Warning","No Sufficient Balance!!!!!!!!")

         if self.combo_leavetype.get() == "Maternity_leave":
            if int(balance2) >=int(self.txt_No_of_days.get()):
               cur.execute('insert into tblleavedetails values(%s,%s,%s,%s,%s,%s,%s,"pending")',(
                          self.txt_EmpId.get(),
                          self.combo_leavetype.get(),
                          self.txt_No_of_days.get(),
                          #self.txt_leaveavailable.get(),
                          self.combo_leavereason.get(),
                          self.txt_applied_on.get(),
                          self.txt_leave_from.get(),
                          self.txt_leave_to.get()
                          
                ))
               con.commit()
               con.close()
               messagebox.showinfo("success","Employee has successfully applied leave")
            else:
               messagebox.showerror("Maternity_leave Warning","No Sufficient Balance!!!!!!!!")

      else:
            messagebox.showerror("Error", "Total Number of Days Does not Match.....") 
    


      
      if self.txt_EmpId.get()=="":
         messagebox.showerror("Error","emp id is Required")
      elif self.combo_leavetype.get()=="":
          messagebox.showerror("Error","leavetype is Required")
      elif self.txt_No_of_days.get()=="":
        messagebox.showerror("Error","No.Of days is Required")
      elif self.combo_leavereason.get()=="":
         messagebox.showerror("Error","leave reason is Required")
      elif self.txt_applied_on.get()=="":
         messagebox.showerror("Error","applied_on is Required")
      elif self.txt_leave_from.get()=="":
         messagebox.showerror("Error","leave_from is Required")
      elif self.txt_leave_to.get()=="": 
        messagebox.showerror("Error","leave to Required")
     

    def EmployeeLeaveHistory(self):
       

        leave_status_frame=Frame(self.root,bg="white")
        leave_status_frame.place(x=10,y=240,width=1330,height=300)
        
        tree = ttk.Treeview(leave_status_frame)
        tree.pack(side = 'left')
        
        verscrlbar = ttk.Scrollbar(leave_status_frame, command = tree.yview)  
        verscrlbar.pack(side ='left', fill = "y") 
    
        tree.configure(yscrollcommand = verscrlbar.set)


        tree["columns"] = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight')

        tree.column("one", anchor = 'c', minwidth = 0, width = 150)
        tree.column("two", anchor = 'c', minwidth = 0, width = 150)
        tree.column("three", anchor = 'c', minwidth = 0, width = 150)
        tree.column("four", anchor = 'c', minwidth = 0, width = 150)
        tree.column("five", anchor = 'c', minwidth = 0, width = 150)
        tree.column("six", anchor = 'c', minwidth = 0, width = 150)
        tree.column("seven", anchor = 'c', minwidth = 0, width = 150)
        tree.column('eight', anchor = 'c', minwidth = 0, width = 140)
        
        tree['show'] = 'headings'

        tree.heading("one", text="Emp ID")
        tree.heading("two", text="Leave Type")
        tree.heading("three", text="no_of days")
        tree.heading("four", text="leave reason")
        tree.heading("five", text="applied on")
        tree.heading("six", text="leave from")
        tree.heading("seven", text="leave to")
        tree.heading("eight", text = "status")
        

        con=mysql.connector.connect(host='localhost',database='employee management',user='pajju',password='1234')
        cur=con.cursor()
        
        cur.execute(f'SELECT * FROM  tblleavedetails WHERE emp_id = "{self.txt_EmpId.get()}"')
        
        for row in cur:
            tree.insert('', 'end', values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        tree.pack()

    def checkDays(self,Days):
      if Days.isdigit():
         return True
      elif len(str(Days))==0:
         return True
      else:
         messagebox.showerror('invalid','invalid entry')
         return False

    def LeaveBalance(self):
      
      global balanced
      balanced=[]
      con=mysql.connector.connect(host='localhost',database='employee management',user='pajju',password='1234')
      cur=con.cursor()
      cur.execute(f'select * from tblleavestructure where emp_id="{self.txt_EmpId.get()}"')
      balanced = cur.fetchone()
      self.WindowBalance()

    def  WindowBalance(self):

      #   balanceWindow = Toplevel()
      #   balanceWindow.resizable(0, 0)
      leavebalance_frame=Frame(self.root,bg="white")
      leavebalance_frame.place(x=950,y=280,width=250,height=200)


      label_1 = Label(leavebalance_frame, text = "Employee ID=", fg="black", justify=LEFT, font=("Calibri", 16))
      label_2 = Label(leavebalance_frame, text = balanced[0], font=("Calibri", 16))
      label_3 = Label(leavebalance_frame, text ="Sick Leave=", fg="black", font=("Calibri", 16), justify=LEFT)
      label_4 = Label(leavebalance_frame, text = balanced[1], font=("Calibri", 16))
      label_5 = Label(leavebalance_frame, text = "Maternity Leave=", fg="black", font=("Calibri", 16), justify=LEFT)
      label_6 = Label(leavebalance_frame, text = balanced[2], font=("Calibri", 16))
       
      label_1.grid(row=0, column=0)
      label_2.grid(row=0, column=1)
      label_3.grid(row=1, column=0)
      label_4.grid(row=1, column=1)
      label_5.grid(row=2, column=0)
      label_6.grid(row=2, column=1)
        







        




















root=Tk()
obj=EmpLeave(root) 
root.mainloop()