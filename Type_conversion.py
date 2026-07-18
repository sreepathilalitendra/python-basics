# Type Conversion

a = input("Enter a number: ")
a = int(a)
print(a, type(a))

b = input("Enter a decimal number: ")
b = float(b)
print(b, type(b))

c = input("Enter the value of c: ")
c = int(c)

d = 6
print(c + d)

a = 56
print("Number is: " + str(a))

a = input("Enter a number: ")
b = input("Enter a number: ")

print("Before conversion:", type(a))

total = int(a) + int(b)
print("Sum =", total)

a = input("Enter the value of a: ")
print("Before conversion:", type(a))

a = int(a)
print("After conversion:", type(a))

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Sum =", a + b)