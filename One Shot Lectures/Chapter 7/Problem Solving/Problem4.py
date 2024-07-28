# 4.Write a program to find whether a given number is prime or not.
n = int(input("Enter a number: "))

for i in range(2,n):
    if(n%i==0):
        print("number is composite.")
        break
else:
     print("this is a prime number")
    