# Program 3:

class MoreAgeError(Exception):
    def __init__(self, m):
        self.msg = m
    
def check(age):
    try:
        if age>30:
            raise MoreAgeError("Ineligible due to more age!")
        else:
            print("The canditate is eligible")
        
    except MoreAgeError as e:
        print(e)
    
    finally:
        print("Exit")

if __name__ == "__main__":
    age = int(input("Enter age of the canditate: "))
    check(age)
