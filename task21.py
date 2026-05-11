# functions 
def greet():
    print("Hello")
#program 1
def greet():
    print("Welcome to python")
greet()
#program -2 
def greet(name):
    print("Hello",name)
greet("Lalitendra")
# program -3
def add(a,b):
    print("sum =",a+b)
add(10,20)
# program -4 
def square(n):
    return n * n
result = square(5)
print(result)
def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check(10))

