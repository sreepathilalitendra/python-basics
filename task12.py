# check largest  of three number
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
if a >= b and a >= c:
    print(a,"is a largest number")
elif b >= a and b >= c:
    print(b,"is a largest number")
else:
    print(c," is a largest number")
# Even + positive combo
a = int(input("Enter the value of a:"))
if a % 2 == 0 and a > 0:
        print("Even number and positive number")
elif a % 2 == 0 and a < 0:
    print("Even and Negative")
elif a % 2!= 0 and a > 0:
    print("odd and positive")
else:
    print("Odd  and Negative ")
# leap year 
year = int(input("Enter year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")
