a = int(input("Enter your age: "))
#  IF statement no 1
if(a%2 ==0):
    print("a is even.")
    
# end of if statement no 1

# if statement no 2
if(a>=18):
        print("you are adult.")
elif(a<0):
    print("you are entering invalid age")    

elif(a==0):
    print("you entered 0 which is invalid age")

else:
    print("you are below the age of consent ")

print("end of program.")