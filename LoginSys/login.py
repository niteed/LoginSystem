from tkinter import*
from tkinter import ttk
#to insert img for bg we will use pillow library
from PIL import Image,ImageTk
#importing msg box for errors
from tkinter import messagebox

class Login_Window:
    #constructor for login class
    def __init__(self,root):
        self.root=root
        #window title,size
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0") 
        #(size,xpoint start,ypoint start)
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\kishor\Desktop\AttendanceSys\Images\Login_bg_image.jpg")
        #displaying bg image by using label
        lbl_bg=Label(self.root,image=self.bg)
        #placing the image using relative width and height so that whenever window chnges it can place itself properly
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        #frame for login
        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=170,width=340,height=450)

        #inserting image on frame
        img1=Image.open(r"C:\Users\kishor\Desktop\AttendanceSys\Images\icon_login.png")
        img1=img1.resize((105,90),Image.ANTIALIAS)
        #resizing(width,height)
        #antialias converts high level img to low level
        #img1 saved to photoimage1
        self.photoimage1=ImageTk.PhotoImage(img1)
        #images can be inserted via frames
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=620,y=170,width=105,height=90)
        #we need label inside frame
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=85)

        #label for username 
        username=lbl=Label(frame,text="Username",font=("times new roman",16,"bold"),fg="black",bg="white")
        username.place(x=70,y=140)
        #entry for username
        self.txtuser=ttk.Entry(frame,font=("times new roman",16,"bold"))
        self.txtuser.place(x=35,y=170,width=270)

        #label for password 
        password =lbl=Label(frame,text="Password",font=("times new roman",16,"bold"),fg="black",bg="white")
        password .place(x=70,y=210)
        #entry for password
        self.txtpass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        self.txtpass.place(x=35,y=240,width=270)

        #icon images
        #inserting image on frame
        img2=Image.open(r"C:\Users\kishor\Desktop\AttendanceSys\Images\icon_user.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblimg2.place(x=540,y=313,width=25,height=25)

        img3=Image.open(r"C:\Users\kishor\Desktop\AttendanceSys\Images\icon_pass.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lblimg3.place(x=540,y=383,width=25,height=25)

        #Login Button 
        #border=bd #border style=relief
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",16,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="black")
        loginbtn.place(x=110,y=290,width=120,height=35)

        #Signup button
        signupbtn=Button(frame,text="New User? Sign Up",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="blue",activebackground="white")
        signupbtn.place(x=9,y=340,width=160)

        #forgotpass button
        forgotpassbtn=Button(frame,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="blue",activebackground="white")
        forgotpassbtn.place(x=3,y=370,width=160)

    #function for validation which will be called inside login button
    #by using command=self.funcname

    def login(self) : 
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error:","all fields required")

        elif self.txtuser.get()=="nitee" and self.txtpass.get()=="123456":
             messagebox.showinfo("Login Successful","Welcome")
        
        else :
            messagebox.showerror("Invalid","Invalid Username or Password")



    





    
#object creation
if __name__=="__main__":
    #object calling
    root=Tk()
    #passing object through class
    app=Login_Window(root)
    #closing window with root
    root.mainloop()

    
