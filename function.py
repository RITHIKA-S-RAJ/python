def add(x,y):
    return x + y 
def sub(x,y):
    return x - y
a = int(input("Enter a X:"))
b = int(input("Enter a Y:"))
if input("Enter operation :") == "+":
    print(add(a,b))
else:
    print(sub(a,b))