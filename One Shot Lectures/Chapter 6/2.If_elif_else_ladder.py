a = int(input("Enter your age: "))
# if elif else ladder.
if(a>18):
    print("you are above the age of consent")
elif(a<0):
    print("you are entering invalid age")    

elif(a==0):
    print("you entered 0 which is invalid age")

else:
    print("you are below the age of consent")

print("end of program.")