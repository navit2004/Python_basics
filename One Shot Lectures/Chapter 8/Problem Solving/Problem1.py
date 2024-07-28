# 1.Write a program using functions to find greatest of three numbers.

def greatest():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    c=int(input("Enter a number: "))
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
print(f"{greatest()}, is greatest number")