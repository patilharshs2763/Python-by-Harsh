class Vehical:
    def disp(self):
        print("I have Vehicals")
class Car:
    def dispCar(self):
        print("Car")
class Lexus(Car):
    def dispLexus(self):
        print("Lexus")
class MyGarrage(Vehical,Lexus):
    def dispMyG(self):
        print("My Garrage")
ob=MyGarrage()0
ob.dispMyG()
ob.disp()
ob.dispCar()
ob.dispLexus()