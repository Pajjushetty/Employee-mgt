from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
import os
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox


class AdminManageLeave:
     def __init__(self,root):
         self.root=root
         self.root.geometry("1530x790+0+0")
     
         self.root.title("Employee management system")
         self.root.config(bg="light blue")


         lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='blue',bg='white')
         lbl_title.place(x=0,y=0,width=1500, height=50)

         btnback=Button(root,text="Back",font=("times new roman", 10, "bold"),relief=RIDGE,fg="white",bg="black",    command=lambda:self.BackFunction(root))
         btnback.place(x=5,y=5,width=70,height=40)

         img1=Image.open(r"Images\login.jpg ")
         img1=img1.resize((50, 50), Image.ANTIALIAS)
         self.photoimage1=ImageTk.PhotoImage(img1)
         lblimg1=Label(image = self.photoimage1, bg="white", borderwidth=0)
         lblimg1.place(x=210,y=0, width=100, height=50)

         

         self.var_emp_id=StringVar()
         self.var_leave_type=StringVar()
         self.var_no_of_days=StringVar()
         #self.var_leave_available=StringVar()
         self.var_leave_reason=StringVar()
         self.var_applied_on=StringVar()
         self.var_leave_from=StringVar()
         self.var_leave_to=StringVar()
         
        
          
         leave_frame=Frame(self.root,bg="orange")
         leave_frame.place(x=70,y=60,width=1000,height=300)

        #empid
         lbl_EmpId=Label(leave_frame,text="Emp Id",font=('arial','11','bold',),bg='white' )
         lbl_EmpId.grid(row=0,column=0,padx=2,sticky=W,pady=5)

         self.txt_EmpId=ttk.Entry(leave_frame,textvariable=self.var_emp_id,width=22,font=('arial','11','bold'),state='readonly')
         self.txt_EmpId.grid(row=0,column=1,sticky=W,padx=5,pady=5)
         
        #leave type
         lbl_leavetype=Label(leave_frame,text="Leavetype",font=('arial','11','bold',),bg='white' )
         lbl_leavetype.grid(row=1,column=0,padx=2,sticky=W,pady=5)

         self.combo_leavetype=ttk.Combobox(leave_frame,textvariable=self.var_leave_type,font=('arial','11','bold'),width=20,state="readonly")
         self.combo_leavetype[ 'value']=('Select','CL')
         self.combo_leavetype.current()
         self.combo_leavetype.grid(row=1, column=1, padx=2, pady=5, sticky=W)

         #no of days
         lbl_No_of_days=Label(leave_frame,text="No_Of_Days",font=('arial','11','bold',),bg='white' )
         lbl_No_of_days.grid(row=2,column=0,padx=2,sticky=W,pady=5)

         self.txt_No_of_days=ttk.Entry(leave_frame,textvariable=self.var_no_of_days,width=22,font=('arial','11','bold'),state='readonly')
         self.txt_No_of_days.grid(row=2,column=1,sticky=W,padx=5,pady=5)
          
        #  #leave available
        #  lbl_leaveavailable=Label(leave_frame,text="Leave Available",font=('arial','11','bold',),bg='white' )
        #  lbl_leaveavailable.grid(row=3,column=0,padx=2,sticky=W,pady=5)

        #  self.txt_leaveavailable=ttk.Entry(leave_frame,textvariable=self.var_leave_available,width=22,font=('arial','11','bold'),state='readonly')
        #  self.txt_leaveavailable.grid(row=3,column=1,sticky=W,padx=5,pady=5)

         #leave reason
         lbl_leavereason=Label(leave_frame,text="Leave Reason",font=('arial','11','bold',),bg='white' )
         lbl_leavereason.grid(row=3,column=0,padx=2,sticky=W,pady=5)

         self.combo_leavereason=ttk.Combobox(leave_frame,textvariable=self.var_leave_reason,font=('arial','11','bold'),width=20,state="readonly")
         self.combo_leavereason[ 'value']=('Select','Relatives Wedding','not feeling well')
         self.combo_leavereason.current()
         self.combo_leavereason.grid(row=3, column=1, padx=2, pady=5, sticky=W)

         #available on
         lbl_applied_on=Label(leave_frame,text="Applied On",font=('arial','11','bold',),bg='white' )
         lbl_applied_on.grid(row=0,column=2,padx=2,sticky=W,pady=5)

         self.txt_applied_on=ttk.Entry(leave_frame,textvariable=self.var_applied_on,width=22,font=('arial','11','bold'),state='readonly')
         self.txt_applied_on.grid(row=0,column=3,sticky=W,padx=5,pady=5)

        #leave from
         lbl_leave_from=Label(leave_frame,text="Leave From",font=('arial','11','bold',),bg='white' )
         lbl_leave_from.grid(row=1,column=2,padx=2,sticky=W,pady=5)

         self.txt_leave_from=ttk.Entry(leave_frame,textvariable=self.var_leave_from,width=22,font=('arial','11','bold'),state='readonly')
         self.txt_leave_from.grid(row=1,column=3,sticky=W,padx=5,pady=5)
 
          #leave To
         lbl_leave_to=Label(leave_frame,text="Leave To",font=('arial','11','bold',),bg='white' )
         lbl_leave_to.grid(row=2,column=2,padx=2,sticky=W,pady=5)

         self.txt_leave_to=ttk.Entry(leave_frame,textvariable=self.var_leave_to,width=22,font=('arial','11','bold'),state='readonly')
         self.txt_leave_to.grid(row=2,column=3,sticky=W,padx=5,pady=5)

        # accept or reject leave
         self.var_radio=IntVar()
         radio_accept=Radiobutton(leave_frame,value=1,text='accept',variable=self.var_radio,font=('arial','11','bold'))
         radio_accept.grid(row=4,column=0,sticky=W,padx=5,pady=5)

         radio_reject=Radiobutton(leave_frame,value=2,text='reject',variable=self.var_radio,font=('arial','11','bold'))
         radio_reject.grid(row=4,column=1,sticky=W,padx=5,pady=5)

          ####button ok###########
         btnok=Button(leave_frame,text="Ok",font=('times new roman',15,'bold'),command=self.acceptreject,width=13,bg='blue',fg='black')
         btnok.grid(row=5,column=0,padx=10,pady=5)

          ####button cancel###########
         #btncancel=Button(leave_frame,text="Cancel",font=('times new roman',15,'bold'),width=13,bg='blue',fg='black')
         #btncancel.grid(row=5,column=1,padx=10,pady=5)


         
         
         
         
         
         
         
         
         
         
         
         
         
          #table frame
         table_frame = Frame(root, bd=3, relief=RIDGE)
         table_frame.place(x=10, y=400,width=1350,height=300)

          # Scrool bar

         axis_x_scrollbar = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
         axis_y_scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL)

         axis_x_scrollbar.pack(side=BOTTOM,fill=X)
         axis_y_scrollbar.pack(side=RIGHT,fill=Y)



          # Table Content

        ##  Heading to be represented in each column
         self.emp_leave_table=ttk.Treeview(table_frame,columns=("emp_id", "leave_type","no_of_days_request",  "leave_reason", "applied_on", "leave_from", "leave_to"), xscrollcommand=axis_x_scrollbar.set,yscrollcommand=axis_y_scrollbar.set)

         self.emp_leave_table.heading("emp_id", text='Emp_ID')
         self.emp_leave_table.heading("leave_type", text='Leave_Type')
         self.emp_leave_table.heading("no_of_days_request", text='No_Of_Days_Request')
         #self.emp_leave_table.heading("leave_available", text='Leave_Available')
         self.emp_leave_table.heading("leave_reason", text='Leave_Reason')
         self.emp_leave_table.heading("applied_on", text='Applied_On')
         self.emp_leave_table.heading("leave_from", text='Leave_From')
         self.emp_leave_table.heading("leave_to", text='Leave_To')
         

        ## To give proper spacing among columns in database area.
         self.emp_leave_table['show']='headings'

         self.emp_leave_table.column("emp_id",width=50)
         self.emp_leave_table.column("leave_type",width=50)
         self.emp_leave_table.column("no_of_days_request",width=50)
         #self.emp_leave_table.column("leave_available",width=50)
         self.emp_leave_table.column("leave_reason",width=50)
         self.emp_leave_table.column("applied_on",width=100)
         self.emp_leave_table.column("leave_from",width=100)
         self.emp_leave_table.column("leave_to",width=100)

         self.emp_leave_table.pack(fill=BOTH, expand=1)
         self.emp_leave_table.bind("<ButtonRelease>",self.get_cursor)

         self.fetch_data()

     def fetch_data(self):
       con=mysql.connector.connect(
          host='localhost',
          database='employee management',
          user='pajju',
          password='1234'
          )
       cur=con.cursor()
       cur.execute('select * from tblleavedetails where status="pending"')
       data=cur.fetchall()
       con.close()
       if len(data)!=0:
          self.emp_leave_table.delete(*self.emp_leave_table.get_children())
          for i in data:
             self.emp_leave_table.insert("",END,values=i)     
         
     def get_cursor(self,event=""):
       cursor_row=self.emp_leave_table.focus()
       content=self.emp_leave_table.item(cursor_row)
       data=content['values']

       self.var_emp_id.set(data[0])
       self.var_leave_type.set(data[1])
       self.var_no_of_days.set(data[2])
       #self.var_leave_available.set(data[3])
       self.var_leave_reason.set(data[4])
       self.var_applied_on.set(data[5])
       self.var_leave_from.set(data[6])
       self.var_leave_to.set(data[7])
      
     def acceptreject(self):
        try:
             update=messagebox.askyesno('leave','Are you sure want to accept or reject the  leave')
             if update>0:
               if self.var_radio.get() ==1:
                 con=mysql.connector.connect(host='localhost',database='employee management',user='pajju',password='1234')
                 cur=con.cursor()
                 cur.execute(f'update tblleavedetails set status="accept" where emp_id="{self.txt_EmpId.get()}"')
                 
                 cur.execute(f'select * from tblleavestructure where emp_id="{self.txt_EmpId.get()}"')
                 exampleData = cur.fetchone()
                 exCasual=int(exampleData[1])
                 exMaternity=int(exampleData[2])
                 
                 date1=exCasual
                 date2=exMaternity
                 date3=int(self.var_no_of_days.get())
                 print(date1,date2,date3)
                 if ( self.var_leave_type.get() == ('CL')):
                  cur.execute(f'update tblleavestructure set CL="{(date1-date3)}" where emp_id="{self.txt_EmpId.get()}"')
                 elif ( self.var_leave_type.get() == ('Maternity_leave')): 
                   cur.execute(f'update tblleavestructure set Maternity_leave="{(date1-date3)}" where emp_id="{self.txt_EmpId.get()}"')
                
               else:                
                con=mysql.connector.connect(host='localhost',database='employee management',user='pajju',password='1234')
                cur=con.cursor()
                cur.execute(f'update tblleavedetails set status="reject" where emp_id="{self.txt_EmpId.get()}"')
             else:
               if not update:
                  return
               
             con.commit()
             self.fetch_data()
             con.close()
             messagebox.showinfo('success','employee leave successfully approved')
        except Exception as es:
            messagebox.showerror("Error",f"due to :{str(es)}")

     def BackFunction(self,root):
        root.withdraw()
        os.system("py .\AdminMenu.py")
        root.deiconify()

     
                                                                                       




root=Tk()
obj=AdminManageLeave(root) 
root.mainloop()
