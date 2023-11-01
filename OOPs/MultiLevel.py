class Vehical:
    def disp(self):
        print("I'm Vehical")
class Car(Vehical):
    def dispCar(self):
        print("I'm Car")
class Lexus(Car):
    def dispLexus(self):
        print("I'm Lexus car")
ob=Lexus()
ob.disp()
ob.dispCar()
ob.dispLexus()