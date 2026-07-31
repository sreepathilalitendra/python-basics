# Functions

def greet():
    print("Hello")


# Program 1
def greet():
    print("Welcome to Python")

greet()


# Program 2 - Function with parameter
def greet(name):
    print("Hello", name)

greet("Lalitendra")


# Program 3 - Function with two parameters
def add(a, b):
    print("Sum =", a + b)

add(10, 20)


# Program 4 - Function with return value
def square(n):
    return n * n

result = square(5)
print(result)


# Check Even or Odd
def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check(10))