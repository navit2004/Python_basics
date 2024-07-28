# 7.Write a program to print the following star pattern .
#   *  
#  *** 
# ***** for n=3
# p1
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(" " * (n-i),end="") #end tag does not allow to give a new line.
    print("*" * (2*i-1))