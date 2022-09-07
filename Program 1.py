# Program 1:

a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    c = a/b
    print(d)
    
except ZeroDivisionError:
    print("Division by '0' is not possible!\nPlease enter a valid number")

except ValueError:
    print("Only integers are allowed!\nPlease enter a valid number")

except NameError:
    print("d is not defined")
    print("c = ",c)

finally:
    print("Exit")