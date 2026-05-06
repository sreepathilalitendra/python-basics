# if statement 
a = 10
if a > 5:
    print("a is greater than 5")
# if - else 
a = 3
if a > 5:
    print("Greater")
else:
    print("Smaller")
#if-elif-else statement
a = 10
if a > 10:
    print("greater than 10")
elif a == 10:
    print("Equal to 10")
else:
    print("Less than 10")
#practice and task
# program 1 - even or odd 
n = int(input("Enter a number:"))
if n % 2 == 0:
    print("Even")
else:
    print("OSdd")
# program 2 - positive / neagtive 
num = int(input("Enter a number:"))
if num > 0:
    print("positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")
#program -3  - greater
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
if a > b:
    print(" a is greater")
else:
    print("b is greater")
# challenge
marks =int(input("Enter your total marks:"))
if marks >= 90:
    print("Grade A")
elif marks >=70:
    print("Grade B")
else:
    print("Grade C")    