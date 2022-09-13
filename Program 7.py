# Program 7:

class Vehicle:
    def __init__(self, Type=None, Colour=None, Speed=0, Price=0, Gears=0):
        self.Type = Type
        self.Colour = Colour
        self.Speed = Speed
        self.Price = Price
        self.Gears = Gears
    
    def show(self):
        print(f"Type of vehicle: {self.Type}")
        print(f"Color of {self.Type}: {self.Colour}")
        print(f"Price of {self.Type}: {self.Price}")
        
    def speed(self):
        print(f"Maximum speed of {self.Type}: {self.Speed}")
        
    def change_gear(self):
        print(f"Number of gears of {self.Type}: {self.Gears}")
        
class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

if __name__ == "__main__":
    c = Car("car", "silver", 140, 400000, 5)
    t = Truck("truck", "red", 110, 800000, 5)
    
    c.show()
    c.speed()
    c.change_gear()
    
    print()
    
    t.show()
    t.speed()
    t.change_gear()
