s = {1,2,3,22,"navit",4,4}

e= set() #don't use s = {}, as it will create an empty dictionary.

print(type(e))
print(s)

s.add(444)
print(s ,type(s))

print(len(s))

s.remove(1)
print(s ,type(s))