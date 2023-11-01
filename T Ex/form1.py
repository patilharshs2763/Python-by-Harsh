from tkinter import *
parent=Tk()
parent.geometry('500x600')
parent.title("Registration Form")

# label1=Label(parent,text="Register Here",width=30).place(x=20,y=50)
label1=Label(parent,text="Register Here",width=30).grid(row=1,column=1)

parent.mainloop()