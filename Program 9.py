# Program 9:

class Father:
    
    def height(self):
        print("Height = 6 feet")
    
class Mother:
        
    def colour(self):
        print("Colour = White")

class Son(Father, Mother):
    def __init__(self):
        pass
    
S = Son()
S.height()
S.colour()
