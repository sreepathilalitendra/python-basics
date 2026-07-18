# Add an integer and a float
a = int(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

print("Total =", a + b)

# Take a number and double it
a = int(input("Enter the value of a: "))
print("Double =", a * 2)

# Take three numbers and print their average
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

average = (a + b + c) / 3
print("Average =", average)

# Find the square and cube of a number
a = int(input("Enter the value of a: "))

square = a ** 2
cube = a ** 3

print("Square =", square)
print("Cube =", cube)

# Age type conversion
age = input("Enter your age: ")

print("Before conversion:", type(age))

age = int(age)

print("After conversion:", type(age))
print("Next year age =", age + 1)

# Sum, product, and average of two numbers
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Sum =", a + b)
print("Product =", a * b)

average = (a + b) / 2
print("Average =", average)