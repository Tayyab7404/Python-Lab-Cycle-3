# Program 2:

class Number:
    def __init__(self, num=0):
        self.num = num

    def __str__(self):
        return str(self.num)

    def isPrime(self):
        for i in range(2,self.num//2 + 1):
            if i%2 == 0:
                return False
        return True

    def isEven(self):
        return self.num % 2 == 0

    def isOdd(self):
        return self.num % 2 == 1

if __name__ == "__main__":
    n = Number(int(input("Enter a number: ")))

    if n.isPrime():
        print(f"{n} is a Prime number")
    else:
        print(f"{n} is not a Prime number")

    if n.isEven():
        print(f"{n} is an Even number")
    elif n.isOdd():
        print(f"{n} is an Odd number")