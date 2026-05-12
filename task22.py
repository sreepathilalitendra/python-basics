# function with user input 
def add():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    print("Sum =",a+b)
add()
# program 2 - Default parameters 
def greet(name='Guest'):
    print("Hello",name)
greet()
greet("Lalitendra")
#multiple return values 
def calculate(a,b):
    return a + b , a * b
sum_value,product = calculate(5,2)
print("Sum =" ,sum_value)
print("Product=",product)
#program -4 largest number
def largest(a, b):
    if a > b:
        return a
    else:
        return b
print(largest(10,20))
#program -5 factorial of a function 
def factorial(n):
    fact = 1
    for i in range(1,n+1):
       fact *=i
    return fact
print(factorial(5))
