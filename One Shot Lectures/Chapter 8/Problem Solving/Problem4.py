# 4.Write a recursive function to calculate the sum of first n natural numbers.
'''
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+4
sum(5)=1+2+3+4+5

sum(n)=sum(n-1)+sum(n)
'''
n=int(input("Enter your number: "))
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
print(sum(n))