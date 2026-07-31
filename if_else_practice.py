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


# if-elif-else statement
a = 10

if a > 10:
    print("Greater than 10")
elif a == 10:
    print("Equal to 10")
else:
    print("Less than 10")


# Practice and Task

# Program 1 - Even or Odd
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# Program 2 - Positive / Negative
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


# Program 3 - Greater
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

if a > b:
    print("a is greater")
else:
    print("b is greater")


# Challenge - Grade
marks = int(input("Enter your total marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")


# Ticket Price
age = int(input("Enter your age: "))

if age < 5:
    print("Ticket is free for Kids!")
elif age >= 5 and age <= 18:
    print("Ticket price is 150 (Student Discount)")
elif age > 18 and age < 60:
    print("Ticket Price is 250 (Adult)")
else:
    print("Ticket price is 100 (Senior Citizen Discount)")


# ATM Logic
pin = int(input("Enter your 4-digit PIN: "))

if pin == 1234:
    print("PIN is correct.")

    # Nested if
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 5000:
        print("Withdrawal Successful! Collect Your Cash.")
    else:
        print("Insufficient balance in your account!")
else:
    print("Wrong PIN! Access Denied.")