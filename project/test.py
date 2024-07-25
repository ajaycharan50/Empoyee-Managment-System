from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class employee:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System-By Ajay Charan")
          #bg image
        img=Image.open(r"C:\Users\Dell\Downloads\20230607171839_IMG_3110-01.jpeg")
        img=img.resize((1400,800),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1400,height=700) 
          
  #============variables========
        self.var_dep=StringVar()
        self.var_class=StringVar()
        self.var_sec=StringVar()
        self.var_StuID=StringVar()
        self.var_StuName=StringVar()
        self.var_AdmnNum=StringVar()
        self.var_rollNum=StringVar()
        self.var_Gender=StringVar()
        self.var_DOB=StringVar()
        self.var_contnum=StringVar()
        self.var_contnum2=StringVar()
        self.var_Father=StringVar()
        self.var_Mother=StringVar()
        self.var_EMAIL=StringVar()
        self.var_Adress=StringVar()
        self.var_photo=StringVar()
        self.var_radio1=StringVar()
         
         
        
        title_lbl=Label(text="EMPLOYEE MANAGEMENT SYSTEM-By Ajay Charan",font=("Dancing Script",35 ,"bold"),bg="black",fg="white") 
        title_lbl.place(x=-120,y=0,width=1530,height=55)
        
        main_frame=Frame(bd=2,bg="black")
        main_frame.place(x=15,y=55,width=1400,height=620)
        
         #left label framedent Details",
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee details",font=("times new roman",20,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=580)
        
        #current class
        Current_Course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Role Details",font=("times new roman",15,"bold"))
        Current_Course_frame.place(x=20,y=50,width=620,height=120)
         
         
        dep_label=Label(Current_Course_frame,text="ROLE",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
         
        dep_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Role","Engineering Project Manage","Chief Digital Officer.","Software Architect.")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
         
         #typeofemployee
      
        class_label=Label(Current_Course_frame,text="Type of Employee",font=("times new roman",15,"bold"),bg="white")
        class_label.grid(row=0,column=2,padx=10,sticky=W)
         
        class_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_class,font=("times new roman",10,"bold"),width=17,state="read only")
        class_combo["values"]=("select Type","Full-Time Employees.","Part-Time Employees.","Seasonal Employees.")
        class_combo.current(0)
        class_combo.grid(row=0,column=3,padx=2,pady=1,sticky=W)
         
         #department
        sec_label=Label(Current_Course_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        sec_label.grid(row=1,column=0,padx=10,sticky=W)
         
        sec_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_sec,font=("times new roman",10,"bold"),width=17,state="read only")
        sec_combo["values"]=("select Department","General Management","Marketing Department","Operations Department","Human Resource Department.",)
        sec_combo.current(0)
        sec_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
         
         #Employee details
        Current_Course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("times new roman",15,"bold"))
        Current_Course_frame.place(x=20,y=220,width=630,height=350)
         
         #Employeetid
        student_label=Label(Current_Course_frame,text=" EmpID:",font=("times new roman",10,"bold"),bg="white")
        student_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
         
        student_entry=Entry(Current_Course_frame,textvariable=self.var_StuID,width=20,font=("times new roman",10,"bold"),bg="white")
        student_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
         
         #employee name
        name_label=Label(Current_Course_frame,text="Emp Name:",font=("times new roman",10,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
         
        name_entry=Entry(Current_Course_frame,textvariable=self.var_StuName,width=20,font=("times new roman",10,"bold"),bg="white")
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
         
         #Salary
        admission_label=Label(Current_Course_frame,text="Salary:",font=("times new roman",10,"bold"),bg="white")
        admission_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
         
        admission_entry=Entry(Current_Course_frame,width=20,textvariable=self.var_AdmnNum,font=("times new roman",10,"bold"),bg="white")
        admission_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
         
         #Acc number
        roll_label=Label(Current_Course_frame,text="Acc Number:",font=("times new roman",10,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_entry=Entry(Current_Course_frame,width=20,textvariable=self.var_rollNum,font=("times new roman",10,"bold"),bg="white")
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
         
         #gender
        gender_label=Label(Current_Course_frame,text="Gender:",font=("times new roman",10,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
         
        gender_entry=Entry(Current_Course_frame,width=20,font=("times new roman",10,"bold"),bg="white")
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
         
        gender_label=ttk.Combobox(Current_Course_frame,textvariable=self.var_Gender,font=("times new roman",10,"bold"),width=17,state="read only")
        gender_label["values"]=("select","male","female")
        gender_label.current(0)
        gender_label.grid(row=2,column=1,padx=10,pady=8,sticky=W)
         
         #DOB
        dob_label=Label(Current_Course_frame,text="Date of Birth:",font=("times new roman",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
         
        dob_entry=Entry(Current_Course_frame,width=20,textvariable=self.var_DOB,font=("times new roman",10,"bold"),bg="white")
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
          
 
          
         #contact number   
        phone_label=Label(Current_Course_frame,text="Contact Number:",font=("times new roman",10,"bold"),bg="white")
        phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
         
        phone_entry=Entry(Current_Course_frame,width=20,textvariable=self.var_contnum,font=("times new roman",10,"bold"),bg="white")
        phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
         
         
         #contact number 2
        phone_label=Label(Current_Course_frame,text="Contact Number 2:",font=("times new roman",10,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
         
        phone__entry=Entry(Current_Course_frame,width=20,textvariable=self.var_contnum2,font=("times new roman",10,"bold"),bg="white")
        phone__entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
         
         #father name
        father_label=Label(Current_Course_frame,text="Father Name:",font=("times new roman",10,"bold"),bg="white")
        father_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
         
        father_entry=Entry(Current_Course_frame,width=20,textvariable=self.var_Father,font=("times new roman",10,"bold"),bg="white")
        father_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
         
         #mother name
        mother_label=Label(Current_Course_frame,text="Mother Name:",font=("times new roman",10,"bold"),bg="white")
        mother_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
         
        mother_entry=Entry(Current_Course_frame,width=20,textvariable=self.var_Mother,font=("times new roman",10,"bold"),bg="white")
        mother_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
         
         #email
        email_label=Label(Current_Course_frame,text="EMAIL ID:",font=("times new roman",10,"bold"),bg="white")
        email_label.grid(row=5,column=0,padx=10,pady=5,sticky=W)
         
        email_entry=Entry(Current_Course_frame,width=20,textvariable=self.var_EMAIL,font=("times new roman",10,"bold"),bg="white")
        email_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)
         
         #adress
        adress_label=Label(Current_Course_frame,text="Residential Adress:",font=("times new roman",10,"bold"),bg="white")
        adress_label.grid(row=5,column=2,padx=10,pady=5,sticky=W)
         
        adress_entry=Entry(Current_Course_frame,width=20,textvariable=self.var_Adress,font=("times new roman",10,"bold"),bg="white")
        adress_entry.grid(row=5,column=3,padx=10,pady=5,sticky=W)
         
         #buttons frame
        btn_frame=Frame(Current_Course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=250,width=600,height=30)
         
        save_btn=Button(btn_frame,width=20,command=self.add_details,text="Save",font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=1)
         
        update_btn=Button(btn_frame,width=20,text="Update",command=self.update_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)
         
        delete_btn=Button(btn_frame,width=20,text="Delete",command=self.delete_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=3)
         
        reset_btn=Button(btn_frame,width=20,command=self.reset_data,text="Reset",font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=4)
         
        btn_frame1=Frame(Current_Course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=10,y=280,width=600,height=30)

         #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="WHITE",relief=RIDGE,text="Employee Details",font=("times new roman",20,"bold"))
        Right_frame.place(x=680,y=10,width=650,height=580)
         
         #==============SEARCH SYSTEM=============
         
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",20,"bold"))
        Search_frame.place(x=10,y=20,width=630,height=100)
         
        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="white",fg="red")
        Search_label.grid(row=0,column=1,padx=10,pady=5,sticky=W)
         
         
         
        dep_label=ttk.Combobox(Search_frame,font=("times new roman",10,"bold"),width=17,state="read only")
        dep_label["values"]=("select","Empid","Contact Number")
        dep_label.current(0)
        dep_label.grid(row=0,column=2,padx=10,pady=8,sticky=W)
         
        search_entry=Entry(Search_frame,width=20,font=("times new roman",10,"bold"),bg="white")
        search_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W) 
         
        search_btn=Button(Search_frame,width=12,command=self.fetch_data, text="Search",font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=4,padx=4)
         
        showall_btn=Button(Search_frame,width=12,command=self.fetch_data,text="Show All",font=("times new roman",10,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=5,padx=4)
         
         #==========label============
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=150,width=630,height=350)
         
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
         
        self.student_table=ttk.Treeview(table_frame,column=("dep","class","sec","StuID","StuName","AdmnNum","rollNum","Gender","DOB","contnum","contnum2","Father","Mother","EMAIL","Adress","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
         
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
         
        self.student_table.heading("dep",text="Role")
        self.student_table.heading("class",text="Type of employee")
        self.student_table.heading("sec",text="Department")
        self.student_table.heading("StuID",text="EmpID")
        self.student_table.heading("StuName",text="emp name")
        self.student_table.heading("AdmnNum",text="Salary")
        self.student_table.heading("rollNum",text="Acc Number")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="Date of Birth")
        self.student_table.heading("contnum",text="Contact Number")
        self.student_table.heading("contnum2",text="Contact Number 2")
        self.student_table.heading("Father",text="Father Name")
        self.student_table.heading("Mother",text="Mother Name")
        self.student_table.heading("EMAIL",text="EMAIL")
        self.student_table.heading("Adress",text="Residential Adress")
        self.student_table.heading("photo",text="PhotoSampleStatus")
         
        #self.student_table.column["Show"]=("headings")
         
        
         
        self.student_table.pack(fill=BOTH,expand=1)  
        self.student_table.column("dep",width=100)
        self.student_table.column("class",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("StuID",width=100)
        self.student_table.column("StuName",width=100)
        self.student_table.column("AdmnNum",width=100)
        self.student_table.column("rollNum",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("contnum",width=100)
        self.student_table.column("contnum2",width=100)
        self.student_table.column("Father",width=100)
        self.student_table.column("Mother",width=100)
        self.student_table.column("EMAIL",width=100)
        self.student_table.column("Adress",width=150)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
  #  ================add details ==================     
         
    def add_details(self):
        if self.var_dep.get()=="Select Department" or self.var_StuName.get()=="" or self.var_StuID.get()=="": 
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root', password='Ajay@123', database='world')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_dep.get(),
                                                                                            self.var_class.get(),
                                                                 
                                                                                            self.var_sec.get(),
                                                                                            self.var_StuID.get(),
                                                                                            self.var_StuName.get(),
                                                                                            self.var_AdmnNum.get(),
                                                                                            self.var_rollNum.get(),
                                                                                            self.var_Gender.get(),
                                                                                            self.var_DOB.get(),
                                                                                            self.var_contnum.get(),
                                                                                            self.var_contnum2.get(),
                                                                                            self.var_Father.get(),
                                                                                            self.var_Mother.get(),
                                                                                            self.var_EMAIL.get(),
                                                                                            self.var_Adress.get()
                                                                                            
                                                                                            ))  
                conn.commit() 
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee has been added Successfully",parent=self.root)
            except Exception as es:
                 messagebox.showerror("ERROR",f"Due To :{str(es)}",parent=self.root)
                     
                
    #============fetch data=======
    def fetch_data(self): 
        conn=mysql.connector.connect(host='localhost', username='root', password='Ajay@123', database='world')
        my_cursor=conn.cursor()
        my_cursor.execute("select *from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("" ,END,values=i)
            conn.commit()
        conn.close()
        
        
     #=============get cursor=========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),    
        self.var_class.set(data[1]),       
        self.var_sec.set(data[2]),               
        self.var_StuID.set(data[3]),          
        self.var_StuName.set(data[4]),      
        self.var_AdmnNum.set(data[5]),          
        self.var_rollNum.set(data[6]),           
        self.var_Gender.set(data[7]),  
        self.var_DOB.set(data[8]),
        self.var_contnum.set(data[9]),  
        self.var_contnum2.set(data[10]),  
        self.var_Father.set(data[11]),  
        self.var_Mother.set(data[12]),  
        self.var_EMAIL.set(data[13]),  
        self.var_Adress.set(data[14]),  
    #===============update function=======
    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_StuName.get()=="" or self.var_StuID.get()=="": 
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this Employee details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost', username='root', password='Ajay@123', database='world')
                    my_cursor=conn.cursor()    
                    my_cursor.execute("update student set deo=%s,class=%s,sec=%s,StuName=%s,AdmnNum=%s,rollNum=%s,Gender=%s,DOB=%s,contnum=%s,contnum2=%s,Father=%s,Mother=%s,EMAIL=%s,Adress=%s where StuID=%s",(
                
                                                                                                                                                                                                                           self.var_dep.get(),
                                                                                                                                                                                                                          self.var_class.get(),
                                                                                                                                                                                                                          self.var_sec.get(),
                                                                                                                                                                                                                          
                                                                                                                                                                                                                          self.var_StuName.get(),
                                                                                                                                                                                                                          self.var_AdmnNum.get(),
                                                                                                                                                                                                                          self.var_rollNum.get(),
                                                                                                                                                                                                                          self.var_Gender.get(),
                                                                                                                                                                                                                          self.var_DOB.get(),
                                                                                                                                                                                                                          self.var_contnum.get(),
                                                                                                                                                                                                                          self.var_contnum2.get(),
                                                                                                                                                                                                                          self.var_Father.get(),
                                                                                                                                                                                                                          self.var_Mother.get(),
                                                                                                                                                                                                                          self.var_EMAIL.get(),
                                                                                                                                                                                                                          self.var_Adress.get(),
                                                                                                                                                                                                                          self.var_StuID.get()
                                                                                                                                                                                                                          
                                                                                                                                                                                                                          
                                                                                                                                                                                                                         ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Employee Details Successfully Updated",parent=self.root)   
                conn.commit()  
                
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
                
    #=======delete function
    def delete_data(self):
        if self.var_StuID.get()=="":
           messagebox.showerror("Error","EmptID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno(" Delete Page","Do you want to delete tmysqlhis student",parent=self.root)  
                if delete>0:
                   conn=mysql.connector.connect(host='localhost', username='root', password='Ajay@123', database='world')
                   my_cursor=conn.cursor()                          
                   sql="delete from student where StuID=%s"
                   val=(self.var_StuID.get(),)
                   my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit() 
                self.fetch_data()
                conn.close()          
                messagebox.showinfo("Delete","Successfully deleted Employee details",parent=self.root)      
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)},parent=self.root") 
     #=====reset====
    def reset_data(self):
        self.var_dep.set("Select Department")  
        self.var_class.set("select class"),       
        self.var_sec.set("select section"),               
        self.var_StuID.set(""),          
        self.var_StuName.set(""),      
        self.var_AdmnNum.set(""),          
        self.var_rollNum.set(""),           
        self.var_Gender.set("select"),  
        self.var_DOB.set(""),
        self.var_contnum.set(""),  
        self.var_contnum2.set(""),  
        self.var_Father.set(""),  
        self.var_Mother.set(""),  
        self.var_EMAIL.set(""),  
        self.var_Adress.set(""),
        self.var_photo.set("") 
        self.var_radio1.set("")   
                                           
if __name__ == "__main__":
    root=Tk()
    obj=employee(root)
    root.mainloop() 