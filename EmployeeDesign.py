from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from tkcalendar import DateEntry
from datetime import date
import re
import customtkinter



class EmpDesign:
   def __init__(self,root):
     self.root=root
     self.root.geometry("1530x790+0+0")
     
     self.root.title("Employee management system")

     lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='blue',bg='#FF7434')
     lbl_title.place(x=0,y=0,width=1530, height=50)


     btnback=Button(root,text="Back",font=("times new roman", 10, "bold"),relief=RIDGE,fg="white",bg="black",command=lambda:self.BackFunction(root))
     btnback.place(x=5,y=5,width=70,height=40)

      #Variable
     self.var_emp_id=StringVar()
     self.var_name=StringVar()
     self.var_dept=StringVar()
     self.var_design=StringVar()
     self.var_address=StringVar()
     self.var_email_id=StringVar()
     self.var_dob=StringVar()
     self.var_phone_no=StringVar()
     self.var_gender=StringVar()
     self.var_total_leave=StringVar()
     self.var_salary=StringVar()
     self.var_age=StringVar()
     self.var_doj=StringVar()

     
    




     # Frame for Image below title

     Main_frame=Frame(self.root, bd=2, relief=RIDGE)
     Main_frame.place(x=0,y=50, width=1580, height=800) 

     img=Image.open(r"./images/Main.jpg")
     img= img.resize((1550,800),Image.ANTIALIAS)
     self.bg=ImageTk.PhotoImage(img)
    
     lbl_bg=Label(Main_frame,image=self.bg)
     lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)  
     
    
     

     upper_frame=LabelFrame(Main_frame, bd=2, relief=RIDGE,text="EmployeeInformation",font=('times new roman',15,'bold'),fg='red')
     upper_frame.place(x=10,y=10, width=1530,height=205)
     #empid
     lbl_EmpId=Label(upper_frame,text="Emp Id",font=('calibri','11','bold',),bg='white' )
     lbl_EmpId.grid(row=0,column=0,padx=2,sticky=W,pady=5)
     
     self.txt_EmpId=ttk.Entry(upper_frame,textvariable=self.var_emp_id,width=22,font=('calibri','11','bold'),state=DISABLED)
     self.txt_EmpId.grid(row=0,column=1,sticky=W,padx=5,pady=5)
     self.old_value  = ''
     self.var_emp_id.trace('w',lambda *args,type='empid' :self.check(type,*args))
   

     validate_EmpId = self.root.register(self.checkEmpId)
     self.txt_EmpId.config(validate='key',validatecommand=(validate_EmpId,'%P'))

     #empname
     lbl_Empname=Label(upper_frame,text="Empname",font=('calibri','11','bold',),bg='white')
     lbl_Empname.grid(row=1,column=0,padx=2,sticky=W,pady=5)

     self.txt_Empname=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('calibri','11','bold'))
     self.txt_Empname.grid(row=1,column=1,sticky=W,padx=5,pady=5)

     validate_Empname = self.root.register(self.checkEmpname)
     self.txt_Empname.config(validate='key',validatecommand=(validate_Empname,'%P'))
     
    
     #empdepartment
     lbl_Department=Label(upper_frame,text="Department",font=('calibri','11','bold',),bg='white' )
     lbl_Department.grid(row=2,column=0,padx=2,sticky=W,pady=5)

     self.combo_Department=ttk.Combobox(upper_frame,font=('calibri','11','bold'),textvariable=self.var_dept,width=20,state='readonly')
     self.combo_Department[ 'value']=('Select Department','HR','Software Engineer', 'Manager')
     self.combo_Department.current()
     self.combo_Department.grid(row=2, column=1, padx=2, pady=5, sticky=W)

     #empdesignation
     lbl_Designation=Label(upper_frame,text="Designation",font=('calibri','10','bold',),bg='white' )
     lbl_Designation.grid(row=3,column=0,padx=2,sticky=W,pady=5)
     
     self.combo_Designation=ttk.Combobox(upper_frame,font=('calibri','10','bold'),textvariable=self.var_design,width=23,state='readonly')
     self.combo_Designation[ 'value']=('Chief Executive officer','Chief Operating Officers','Chief Financial Officer', 'Chief Legal Officer')
     self.combo_Designation.current()
     self.combo_Designation.grid(row=3, column=1, padx=2, pady=5, sticky=W)

     #empaddress
     lbl_Address=Label(upper_frame,text="Address",font=('calibri','11','bold',),bg='white' )
     lbl_Address.grid(row=4,column=0,padx=3,sticky=W,pady=5)

     self.txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('calibri','11','bold'))
     self.txt_Address.grid(row=4,column=1,sticky=W,padx=2,pady=5)

     validate_Address = self.root.register(self.checkAddress)
     self.txt_Address.config(validate='key',validatecommand=(validate_Address,'%P'))


     #empEmail
     lbl_EmailId=Label(upper_frame,text="Email ID",font=('calibri','11','bold',),bg='white' )
     lbl_EmailId.grid(row=0,column=3,padx=3,sticky=W,pady=5)

     self.txt_EmailId=ttk.Entry(upper_frame,textvariable=self.var_email_id,width=22,font=('calibri','11','bold'))
     self.txt_EmailId.grid(row=0,column=4,sticky=W,padx=2,pady=5)

     
      #empDOb
     lbl_dob=Label(upper_frame,text="DOB",font=('calibri','11','bold',),bg='white' )
     lbl_dob.grid(row=1,column=3,padx=3,sticky=W,pady=5)

     self.txt_dob=DateEntry(upper_frame,textvariable=self.var_dob,width=20,font=('calibri','11','bold'),selectmode='day')
     self.txt_dob.grid(row=1,column=4,sticky=W,padx=2,pady=5)
     dt=date(2021,7,26)
     self.txt_dob.set_date(dt)

     
   #   validate_dob = self.root.register(self.checkdob)
   #   self.txt_dob.config(validate='key',validatecommand=(validate_dob,'%P'))



     #empphoneno
     lbl_Phone_no=Label(upper_frame,text="Phone no",font=('calibri','11','bold',),bg='white' )
     lbl_Phone_no.grid(row=2,column=3,padx=3,sticky=W,pady=5)

     self.txt_Phone_no=ttk.Entry(upper_frame,textvariable=self.var_phone_no,width=22,font=('calibri','11','bold'))
     self.txt_Phone_no.grid(row=2,column=4,sticky=W,padx=2,pady=5)

     validate_phoneno = self.root.register(self.checkPhoneno)
     self.txt_Phone_no.config(validate='key',validatecommand=(validate_phoneno,'%P'))

     self.old_value  = ''
     self.var_phone_no.trace('w',lambda *args,type='phone' :self.check(type,*args))

     #empdgender
     lbl_Gender=Label(upper_frame,text="Gender",font=('calibri','11','bold',),bg='white' )
     lbl_Gender.grid(row=3,column=3,padx=2,sticky=W,pady=5)

     self.combo_Gender=ttk.Combobox(upper_frame,font=('calibri','11','bold'),textvariable=self.var_gender,width=20,state='readonly')
     self.combo_Gender[ 'value']=('Male','Female','Other')
     self.combo_Gender.current()
     self.combo_Gender.grid(row=3, column=4, padx=2, pady=5, sticky=W)

     #empTotalLeave
     lbl_Total_leave=Label(upper_frame,text="Total Leave",font=('calibri','11','bold',),bg='white' )
     lbl_Total_leave.grid(row=4,column=3,padx=3,sticky=W,pady=5)

     self.txt_Total_leave=ttk.Entry(upper_frame,textvariable=self.var_total_leave,width=22,font=('calibri','11','bold'))
     self.txt_Total_leave.grid(row=4,column=4,sticky=W,padx=2,pady=5)

     #empSalary
     lbl_Salary=Label(upper_frame,text="Salary",font=('calibri','11','bold',),bg='white' )
     lbl_Salary.grid(row=0,column=5,padx=3,sticky=W,pady=5)

     self.txt_Salary=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('calibri','11','bold'))
     self.txt_Salary.grid(row=0,column=6,sticky=W,padx=2,pady=5)
     validate_salary = self.root.register(self.checksalary)
     self.txt_Salary.config(validate='key',validatecommand=(validate_salary,'%P'))


      #empAge
     lbl_Age=Label(upper_frame,text="Age",font=('calibri','11','bold',),bg='white' )
     lbl_Age.grid(row=1,column=5,padx=3,sticky=W,pady=5)

     self.txt_Age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('calibri','11','bold'))
     self.txt_Age.grid(row=1,column=6,sticky=W,padx=2,pady=5)
     validate_age = self.root.register(self.checkAge)
     self.txt_Age.config(validate='key',validatecommand=(validate_age,'%P'))
     self.old_value  = ''
     self.var_age.trace('w',lambda *args,type='age' :self.check(type,*args))


      #empDOJ
     lbl_doj=Label(upper_frame,text="DOJ",font=('calibri','11','bold',),bg='white' )
     lbl_doj.grid(row=2,column=5,padx=3,sticky=W,pady=5)

     self.txt_doj=DateEntry(upper_frame,width=22,textvariable=self.var_doj,font=('calibri','11','bold'),selectmode='day')
     self.txt_doj.grid(row=2,column=6,sticky=W,padx=2,pady=5)
     dt=date(2020,7,20)
     self.txt_doj.set_date(dt)
     
     #to display all the button in a frame
     btn_frame=Frame(upper_frame,relief=RIDGE)
     btn_frame.place(x=1100,y=15,width=200,height=100)   

     b=Button(btn_frame,text="Update",command=self.update_data,borderwidth=5,font=('times new roman',15,'bold'),width=13,bg='blue',fg='black')
     b.grid(row=0,column=0,padx=10,pady=5)

   #   c=Button(btn_frame,text="View",font=('times new roman',15,'bold'),width=13,bg='blue',fg='black')
   #   c.grid(row=1,column=0,padx=10,pady=10)

    
     
     
   

     #lower frame
     lower_frame=LabelFrame(Main_frame, bd=2, relief=RIDGE, text="Employee Information Table",font=('times new roman',15,'bold'),fg='red')
     lower_frame.place(x=10,y=320, width=1530,height=420)
     #search frame
     search_frame = LabelFrame(lower_frame, bd=2, relief=RIDGE, text='Search Employee Information', font=('times new roman', 14,'bold'),foreground='black')
     search_frame.place(x=10, y=10,width=1530,height=70)


     lbl_search_by=Label(search_frame, font=("calibri", 12, "bold"), text="Search By", foreground="white",bg='blue' )
     lbl_search_by.grid(row=0,column=0,padx=10,pady=10,sticky=W)

     #giving the options for searching
     self.var_com_search=StringVar()
     combo_search_by=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('calibri', 12,'bold'),width=18,state='readonly')
     combo_search_by['value']=('Select','emp_id','phone_no','email')
     combo_search_by.current(0)
     combo_search_by.grid(row=0, column=1, padx=10, pady=10, sticky=W)

     self.var_search=StringVar()
     txt_Search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=('calibri', 11,'bold'))
     txt_Search.grid(row=0, column=2, padx=10, pady=10)

     ## Button for searching a single row
     
     button_Search = Button(search_frame, text = 'Search',command=self.search_data,font=('calibri', 11,'bold'),width=18,foreground='white',bg='blue')       
     button_Search.grid(row=0, column=3, padx=10,pady=10)

     ## Button for searching all rows.
     
     button_Search_all= Button(search_frame, text = 'Search All',command=self.fetch_data,font=('calibri', 11,'bold'),width=18,foreground='white',bg='blue')
     button_Search_all.grid(row=0, column=4, padx=10,pady=10)

    #table frame
     table_frame = Frame(lower_frame, bd=3, relief=RIDGE)
     table_frame.place(x=10, y=80,width=1500,height=330)

      # Scrool bar

     axis_x_scrollbar = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
     axis_y_scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL)

     axis_x_scrollbar.pack(side=BOTTOM,fill=X)
     axis_y_scrollbar.pack(side=RIGHT,fill=Y)


     # Table Content

        ##  Heading to be represented in each column
     self.emp_info_table=ttk.Treeview(table_frame,columns=("empid", "name","department", "designition", "address", "email", "dob", "phone", "gender","leave", "salary", "age", "doj"), xscrollcommand=axis_x_scrollbar.set,yscrollcommand=axis_y_scrollbar.set)

     self.emp_info_table.heading("empid", text='Emp_ID')
     self.emp_info_table.heading("name", text='EmpName')
     self.emp_info_table.heading("department", text='Department')
     self.emp_info_table.heading("designition", text='Designition')
     self.emp_info_table.heading("address", text='Address')
     self.emp_info_table.heading("email", text='Email_ID')
     self.emp_info_table.heading("dob", text='DOB')
     self.emp_info_table.heading("phone", text='Phone_no')
     self.emp_info_table.heading("gender", text='Gender')
     self.emp_info_table.heading("leave", text='Total_Leave')
     self.emp_info_table.heading("salary", text='Salary')
     self.emp_info_table.heading("age", text='Age')
     self.emp_info_table.heading("doj", text='DOJ')

    ## To give proper spacing among columns in database area.
     self.emp_info_table['show']='headings'

     self.emp_info_table.column("empid",width=50)
     self.emp_info_table.column("name",width=50)
     self.emp_info_table.column("department",width=50)
     self.emp_info_table.column("designition",width=50)
     self.emp_info_table.column("address",width=50)
     self.emp_info_table.column("email",width=100)
     self.emp_info_table.column("dob",width=100)
     self.emp_info_table.column("phone",width=100)
     self.emp_info_table.column("gender",width=100)
     self.emp_info_table.column("leave",width=100)
     self.emp_info_table.column("salary",width=100)
     self.emp_info_table.column("age",width=100)
     self.emp_info_table.column("doj",width=100)

     self.emp_info_table.pack(fill=BOTH, expand=1)
     self.emp_info_table.bind("<ButtonRelease>",self.get_cursor)

     self.fetch_data()

     axis_x_scrollbar.config(command=self.emp_info_table.xview)
     axis_y_scrollbar.config(command=self.emp_info_table.yview)

   def BackFunction(self,root):
     root.withdraw()
     os.system("py .\EmployeeMenu.py")
     root.deiconify()

   ############display the details of employee###########

   def fetch_data(self):
       con=mysql.connector.connect(
          host='localhost',
          database='employee management',
          user='pajju',
          password='1234'
          )
       cur=con.cursor()
       cur.execute('select * from tblpersonaldetails')
       data=cur.fetchall()
       con.close()
       if len(data)!=0:
          self.emp_info_table.delete(*self.emp_info_table.get_children())
          for i in data:
             self.emp_info_table.insert("",END,values=i)

   #######get cursor#####

   def get_cursor(self,event=""):
      cursor_row=self.emp_info_table.focus()
      content=self.emp_info_table.item(cursor_row)
      data=content['values']

      self.var_emp_id.set(data[0])
      self.var_name.set(data[1])
      self.var_dept.set(data[2])
      self.var_design.set(data[3])
      self.var_address.set(data[4])
      self.var_email_id.set(data[5])
      self.var_dob.set(data[6])
      self.var_phone_no.set(data[7])
      self.var_gender.set(data[8])
      self.var_total_leave.set(data[9])
      self.var_salary.set(data[10])
      self.var_age.set(data[11])
      self.var_doj.set(data[12])

   ############# update method ##################
   def update_data(self):
      if self.txt_EmpId.get()=="" or self.txt_Empname.get()=="" or self.combo_Department.get()=="" or self.combo_Designation.get()=="" or self.txt_Address.get()=="" or self.txt_EmailId.get()=="" or self.txt_dob.get()=="" or self.txt_Phone_no.get()=="" or self.combo_Gender.get()=="" or self.txt_Total_leave.get()=="" or self.txt_Salary.get()=="" or self.txt_Age.get()=="" or self.txt_doj.get()=="":
         messagebox.showerror("Error","All Field Are Required")
      else:
         try:
            update=messagebox.askyesno('update','Are you sure want to update the employee details')
            if update>0:
               con=mysql.connector.connect(host='localhost',database='employee management',user='pajju',password='1234')
               cur=con.cursor()
               cur.execute('update tblpersonaldetails set emp_name=%s,department=%s,designation=%s,address=%s,email_id=%s,dob=%s,phone_no=%s,gender=%s,total_leave=%s,salary=%s,age=%s,doj=%s where emp_id=%s',(
                                                                                                     self.txt_Empname.get(),
                                                                                                     self.combo_Department.get(),
                                                                                                     self.combo_Designation.get(),
                                                                                                     self.txt_Address.get(),
                                                                                                     self.txt_EmailId.get(),
                                                                                                     self.txt_dob.get(),
                                                                                                     self.txt_Phone_no.get(),
                                                                                                     self.combo_Gender.get(),
                                                                                                     self.txt_Total_leave.get(),
                                                                                                     self.txt_Salary.get(),
                                                                                                     self.txt_Age.get(),
                                                                                                     self.txt_doj.get(),
                                                                                                     self.txt_EmpId.get()
                                                                                                   ))
            else:
               if not update:
                  return
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo('success','employee details successfully updated')
         except Exception as es:
            messagebox.showerror("Error",f"due to :{str(es)}")

    ############### search details ############
   def search_data(self):
      if  self.var_com_search.get()=="" or self.var_search.get()=="":
         messagebox.showerror("Error","Please select option")
      else:
         try:
             con=mysql.connector.connect(host='localhost',database='employee management',user='pajju',password='1234')
             cur=con.cursor()
             cur.execute('select * from tblpersonaldetails where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
             rows=cur.fetchall()
             if len(rows)!=0:
                 self.emp_info_table.delete(*self.emp_info_table.get_children())
                 for i in rows:
                    self.emp_info_table.insert("",END,values=i)
             con.commit()
             con.close()
         except Exception as es:
            messagebox.showerror("Error",f"due to :{str(es)}")
              
   def checkEmpId(self,EmpId):
         if EmpId.isdigit():
            return True
         if len(str(EmpId))==0:
            return True
         else:
            messagebox.showerror("Invalid",'Invalid Entry')
            return False 

   def check(self,type,*args):
      if type == 'phone':
         # for emp mob
         if len(self.txt_Phone_no.get()) <= 10:
            self.old_value = self.txt_Phone_no.get()
         else:
            self.var_phone_no.set(self.old_value)
      elif type=='empid':
         # for emp id
         if len(self.txt_EmpId.get()) <= 3:
            self.old_value = self.txt_EmpId.get()
         else:
            self.var_emp_id.set(self.old_value)
      elif type=='age':
         # for emp age
         if len(self.txt_Age.get()) <= 3:
            self.old_value = self.txt_Age.get()
         else:
            self.var_age.set(self.old_value)      
         


   def checkEmpname(self,Empname):
         if Empname.isalpha():
            return True
         else:
            messagebox.showerror("Invalid",'Invalid Entry')
            return False   


   def checkAddress(self,Address):
         if Address.isalphanum():
            return True
         else:
            messagebox.showerror("Invalid",'Invalid Entry')
            return False  


   def checkdob(self,dob):
         if dob.isnumeric():
            return True
         else:
            messagebox.showerror("Invalid",'Invalid Entry')
            return False 

   def checkdoj(self,doj):
         if doj.isnumeric():
            return True
         else:
            messagebox.showerror("Invalid",'Invalid Entry')
            return False

   def checkPhoneno(self,Phoneno):
         if Phoneno.isdigit():
            return True
         if len(str(Phoneno))==10:
            return True
         else:
            messagebox.showerror("Invalid",'Invalid Entry')
            return False
   def checkAge(self,age):
         if age.isnumeric():
            return True
         elif len(str(age))==0:
            return True 
         elif age < 18:
            messagebox.showerror("Age must be greater than 18")
            return False

         else:
            messagebox.showerror("Invalid",'Invalid Entry')
            return False           

   def checksalary(self,salary):
         if salary.isnumeric():
            return True
         elif len(str(salary))==0:
            return True   
         else:
            messagebox.showerror("Invalid",'Invalid Entry')
            return False           

   def checkemail(self,email):
         if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
               return True
            else:
               messagebox.showwarning('Alert','Invalid email enter the valid email user') 
               return False
         else:        
            messagebox.showerror("Invalid",'Email length is to small')

root=Tk()
obj=EmpDesign(root) 
root.mainloop()
