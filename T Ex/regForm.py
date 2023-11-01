from tkinter import *

def display_data():
    full_name = entry_1.get()
    email = entry_2.get()
    gender = "Male" if var.get() == 1 else "Female"
    age = entry_3.get()

    data_label.config(text=f"Full Name: {full_name}\nEmail: {email}\nGender: {gender}\nAge: {age}")
    # data_label.set(full_name,email,gender,age)

root = Tk()
root.geometry('500x500')
root.title("Registration Form")
data_label=StringVar()
label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)
var = IntVar()
Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

label_4 = Label(root, text="Age:", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

entry_3 = Entry(root)
entry_3.place(x=240, y=280)

submit_button = Button(root, text='Submit', width=20, fg='blue', command=display_data)
submit_button.place(x=180, y=380)

data_label = Label(root, text="", font=("bold", 10))
# data_label = Label(root, font=("bold", 10))
data_label.place(x=180, y=420)

root.mainloop()
