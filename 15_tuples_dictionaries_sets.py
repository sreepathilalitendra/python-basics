# Tuples

numbers = (1, 2, 3)
print(numbers)
print(type(numbers))


# Program 1 - Tuple indexing
data = (10, 20, 30)

print(data)
print(data[0])
print(data[-1])


# Program 2 - Tuple length
colors = ("red", "blue", "green")
print(len(colors))


# Dictionaries

# Program 3 - Dictionary
student = {
    "Name": "Lalitendra",
    "Age": 18,
    "Branch": "CSE"
}

print(student)
print(type(student))
print(len(student))


# Access values
print(student["Name"])
print(student["Age"])
print(student)


# Changing values
student["Age"] = 19
print(student)


# Add new value
student["college"] = "XYZ"
print(student)


# Sets

# Program 4 - Set
numbers = {1, 2, 3, 4}
print(numbers)


# Task - Tuple
num = (1, 2, 3, 4, 5)

print(num, type(num))
print(num[0])
print(num[-1])
print(len(num))


# Dictionary
student = {
    "Name": "Lalitendra",
    "Age": 18
}

print(student)
print(type(student))
print(student["Name"])

student["Age"] = 19
print(student)

student["city"] = "Hyderabad"
print(student)


# Set
number = {1, 2, 3, 4, 5, 6, 2, 4, 6, 1, 3, 2, 4, 5}
print(number)


# Challenge - Dictionary
favorite = {
    "colors": "black",
    "food": "Biryani"
}

print(favorite)