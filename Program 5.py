# Program 5:

class Mycomplex:
    
    def __init__(self, r, i):
        self.real = r
        self.img = i
        
    def __str__(self):
        if self.img < 0:
            out = ''
        else:
            out = '+'
        return str(self.real) + out + str(self.img) + 'j'
    
    def __add__(self, c):
        r = self.real + c.real
        i = self.img + c.img
        return Mycomplex(r, i)
        
if __name__ == "__main__":
    print("Enter first complex number: ")
    r = int(input("\tReal part:"))
    i = int(input("\tImaginary part: "))
    c1 = Mycomplex(r, i)

    print("Enter second complex number: ")
    r = int(input("\tReal part: "))
    i = int(input("\tImaginary part: "))
    c2 = Mycomplex(r, i)

    print(f"{c1} + {c2} =", c1+c2)
