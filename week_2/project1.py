name1 = (input("Enter the first name:"))
age1 = int(input("Enter age1:"))
name2 = (input("Enter the second name:"))
age2 = int(input("Enter the name of your choice:"))

#swap ages
age1, age2 = age2 , age1
print(name1, "is now", age1, "years old")
print(name2, "is now", age2, "years old")