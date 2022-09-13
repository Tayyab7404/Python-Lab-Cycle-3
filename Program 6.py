# Program 6:

class Fraction:
    def hcf(self,n1,n2):
        x = min(n1,n2)
        y = max(n1,n2)

        if x == 0:
            return y
        
        return self.hcf(y%x,x)

    def __init__(self,numer,denom):
        h = self.hcf(abs(numer),abs(denom))

        self.numer = numer // h
        self.denom = denom // h

    def __str__(self):
        return f"{self.numer}/{self.denom}"

    def __add__(self,f2):
        n = self.numer*f2.denom + f2.numer*self.denom
        d = self.denom*f2.denom
        return Fraction(n,d)

    def __sub__(self,f2):
        n = self.numer*f2.denom - f2.numer*self.denom
        d = self.denom*f2.denom
        return Fraction(n,d)

    def float(self):
        return self.numer/self.denom

if __name__ == "__main__":
    n1, d1 = [int(x) for x in input("Enter the 1st Fractional number: ").split("/")]
    n2, d2 = [int(x) for x in input("Enter the 2nd Fractional number: ").split("/")]

    num1 = Fraction(n1, d1)
    num2 = Fraction(n2, d2)

    num3 = num1 + num2
    num4 = num1 - num2

    print(f"{num1} + {num2} = {num3} = {num3.float()}")

    print(f"{num1} - {num2} = {num4} = {num4.float()}")
