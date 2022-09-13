# Program 10:

class GrandFather:
    def __init__(self, Property1=0):
        self.Property1 = Property1

class Father(GrandFather):
    def __init__(self, Property1=0, Property2=0):
        self.Property2 = Property2
        super().__init__(Property1)

class Son(Father):
    def __init__(self, Property1=0, Property2=0, Property3=0):
        self.Property3 = Property3
        super().__init__(Property1, Property2)
    
    def display(self):
        print(f"GrandFather's Property = {self.Property1}")
        print(f"Father's Property = {self.Property2}")
        print(f"Son's Property = {self.Property3}")
    
if __name__ == "__main__":
    S = Son(10000000, 1000000, 100000)
    S.display()
