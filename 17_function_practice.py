# Function with user input
def add():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print("Sum =", a + b)

add()


# Program 2 - Default parameters
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Lalitendra")


# Multiple return values
def calculate(a, b):
    return a + b, a * b

sum_value, product = calculate(5, 2)

print("Sum =", sum_value)
print("Product =", product)


# Program 4 - Largest number
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(10, 20))


# Program 5 - Factorial of a number
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

print(factorial(5))