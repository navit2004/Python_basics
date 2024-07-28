# 6.Create an empty dictionary . Allow 4 friends to enter their favourite language as value and use key ass their names . Assume that the name are unique.
d={}

name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})

print(d)