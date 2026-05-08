# largest number 
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
if a >= b and a >= c:
    print(a," is the largest number")
elif b >= a and b >=c:
    print(b," is the largest number")
else:
    print(c," is the largest number")
# even or Odd and positive and Negative 
a = int(input("Enter a number:"))
if a % 2 == 0 and a > 0:
    print("Even and Positive number")
elif a == 0:
    print("Zero")
elif a % 2 == 0 and a < 0:
    print("Even and Negative number")
elif a % 2!= 0 and a > 0:
    print("Odd and Positive number")
else: 
    print("Odd and Negative number")
# calculator program 
a = int(input("Enter the value of a:"))
a = 10
b = 20
if a > b :
    print("A")
elif b > a:
    print("B")
else:
    print("Equal") # output B        

