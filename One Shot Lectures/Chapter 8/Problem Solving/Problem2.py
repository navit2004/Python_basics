# 2.Write a program using functions to convert celsius to farenheit.
def f_to_c(f):
    return 5*(f-32)/9

f=int(input("Enter temperature in farenheit: "))
c= f_to_c(f)
print(f"{round(c,2)} °C")