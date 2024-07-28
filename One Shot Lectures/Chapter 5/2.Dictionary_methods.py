marks={
    "Navit":100,
    "harry":99,
    "chankit":40,
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"harry":98,"renuka":53})
print(marks)

print(marks.get("Navit"))
print(marks.get("Navita")) #prints none
# print(marks.get["Navita"]) #prints error