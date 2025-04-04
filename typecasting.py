name = "Dream"
age = "18"
isStudent = True
weight = 60.5

print(f"Name : {name}")
print("The type of name is", type(name))
print(f"Age : {age}")
print("The type of age is", type(age))
print(f"Is a student : {isStudent}")
print("The type of isStudent is", type(isStudent))
print(f"Weight : {weight}")
print("The type of weight is", type(weight))

print("\nAfter typecasting...")
age = str(age)
print(age)
print("The type of age is", type(age))
weight = int(weight)
print(weight)
print("The type of weight is", type(weight))
