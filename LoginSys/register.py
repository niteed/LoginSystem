from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class Register :
	#constructor
	def __init__(self,root):
		self.root=root
		self.root.title("Register")
		self.root.geometry("1920x1080")

		#========background image=======
		self.bg=ImageTk.PhotoImage(file=r"C:\Users\kishor\Desktop\AttendanceSys\Images\Register_bg_image.jpg ")
		#showing image on window with the help of label
		bg_lbl=Label(self.root,image=self.bg)
		bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


		#========left image=======
		leftbg1=Image.open(r"C:\Users\kishor\Desktop\AttendanceSys\Images\register_quote.jpg ")
		#showing image on window with the help of label
		leftbg1=leftbg1.resize((850,500),Image.ANTIALIAS)
		self.bg1=ImageTk.PhotoImage(leftbg1)
		left_lbl=Label(self.root,image=self.bg1)
		left_lbl.place(x=50,y=80,width=550,height=590)

		#========Registration main frame=======
		frame=Frame(self.root,bg="white")
		frame.place(x=600,y=80,width=720,height=590)
		
		register_lbl=Label(frame,text="Register Here",font=("times new roman",30,"bold"),fg="darkblue",bg="white")
		register_lbl.place(x=50,y=60)

		#========Label and entry=======
		#==ROW 1==
		fname=Label(frame,text="First name",font=("times new roman",15,"bold"),bg="white")
		fname.place(x=50,y=160)
		fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
		fname_entry.place(x=50,y=190,width=250)

		lname=Label(frame,text="Last name",font=("times new roman",15,"bold"),bg="white")
		lname.place(x=370,y=160)
		self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
		self.txt_lname.place(x=370,y=190,width=250)

		#==ROW 2==
		contact=Label(frame,text="Contact no",font=("times new roman",15,"bold"),bg="white")
		contact.place(x=50,y=230)
		self.txt_contact=ttk.Entry(frame,font=("times new roman",15,"bold"))
		self.txt_contact.place(x=50,y=260,width=250)


		email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
		email.place(x=370,y=230)
		self.txt_email=ttk.Entry(frame,font=("times new roman",15))
		self.txt_email.place(x=370,y=260,width=250)

		#==ROW 3==
		security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
		security_Q.place(x=50,y=300)

		self.combo_security_Q=ttk.Combobox(frame,font=("times new roman",15),state="readonly")
		self.combo_security_Q["values"]=("Select","Your Birth Place","Your Grandparents Name","Your Favourite Flower")
		self.combo_security_Q.place(x=50,y=330,width=250)
		self.combo_security_Q.current(0)


		security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
		security_A.place(x=370,y=300)

		self.txt_security=ttk.Entry(frame,font=("times new roman",15,"bold"))
		self.txt_security.place(x=370,y=330,width=250)


		#==ROW 4==
		pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
		pswd.place(x=50,y=370)
		self.txt_pswd=ttk.Entry(frame,font=("times new roman",15,"bold"))
		self.txt_pswd.place(x=50,y=400,width=250)

		confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
		confirm_pswd.place(x=370,y=370)
		self.txt_confirm_pswd=ttk.Entry(frame,font=("times new roman",15,"bold"))
		self.txt_confirm_pswd.place(x=370,y=400,width=250)
		
		#==check button==
		checkbtn=Checkbutton(frame,text="I agree The Terms & Conditions",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
		checkbtn.place(x=50,y=450)

		#==buttons===
		regbtn=Button(frame,text="Register Now",font=("times new roman",16,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="black")
		regbtn.place(x=50,y=500,width=160)

		logbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="black")
		logbtn.place(x=250,y=500,width=160)

	
		

#object
if __name__ == "__main__" :
	#calling object of class
	root=Tk()
	app=Register(root)
	root.mainloop()