class Student:
    def __init__(self,clg):
        self.clg=clg
    
    def getData(self):
        self.name=input("Enter your name:")
        self.rollno=int(input("Enter Roll No:"))
        self.batch=input("Enter Batch:")
    def dispData(self):
        print("\nName:",self.name)
        print("Roll No:",self.rollno)
        print("Batch:",self.batch)
        print("College:",self.clg)

for ob in range(0,4):
    ob=Student("DYP")
    ob.getData()
    ob.dispData()
