# 4.Write a program to find whether a given username contains less than 10 characters or not 
username = input("Enter your username: ")
if(len(username)<10):
    print("Given username contains less than 10 characters.")
else:
    print("Given username contains 10 or more characters.")
