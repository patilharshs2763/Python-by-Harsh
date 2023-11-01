class Vehical:
    def disp(self):
        print("I'm Vehical")
class Bike(Vehical):
    def dispBike(self):
        print("I'm Bike")
ob=Bike()
ob.disp()
ob.dispBike()