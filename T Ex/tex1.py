from tkinter import * 

def res():
    data = e1.get()+e2.get()
    label_text.set(data)

parent = Tk()  
label_text = StringVar()
name_label = Label(parent, text="Name")
name_label.grid(row=0, column=0)  
e1 = Entry(parent)
e1.grid(row=0, column=1)  
password_label = Label(parent, text="Password")
password_label.grid(row=1, column=0)  
e2 = Entry(parent)
e2.grid(row=1, column=1)  
submit = Button(parent, text="Submit", command=res)
submit.grid(row=4, column=0) 
result_label = Label(parent, textvariable=label_text)
result_label.grid(row=5, column=1) 
parent.mainloop()
