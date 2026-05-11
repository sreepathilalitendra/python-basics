# Even or odd 
n = int(input("Enter number:"))
if n % 2 == 0:
    print("Even")
else:
    print("odd")
# Reverse a string 
name = input("Enter name:")
print(name[::-1])
# sum of the list
num = [10,20,30]
total = 0
for i in num:
    total += i
print(total)
numbers = [4,9,2,15,7]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print(largest)