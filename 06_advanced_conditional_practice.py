# Check Largest of Three Numbers

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a >= b and a >= c:
    print(a, "is the largest number")
elif b >= a and b >= c:
    print(b, "is the largest number")
else:
    print(c, "is the largest number")


# Even + Positive Combo

a = int(input("Enter the value of a: "))

if a % 2 == 0 and a > 0:
    print("Even number and positive number")
elif a == 0:
    print("Zero")
elif a % 2 == 0 and a < 0:
    print("Even and Negative")
elif a % 2 != 0 and a > 0:
    print("Odd and Positive")
else:
    print("Odd and Negative")


# Leap Year

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")