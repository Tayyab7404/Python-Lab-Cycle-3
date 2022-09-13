# Program 4:

def add(p, q):
    return p+q

p = input("Enter 1st value: ")
q = input("Enter 2nd value: ")

if p.isdigit():
    p = int(p)

if q.isdigit():
    q = int(q)

if type(p) == type(q):
    print(add(p,q))

else:
    print("Invalid Operation!")
