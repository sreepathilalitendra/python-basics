data =[1,"Python",3.5]
print(data)
# add 2 values using extend( ) method 
numbers = [1,2,3]
numbers.extend([4,5])
print(numbers)
# priniting using loop
numbers = [10,20,30]
for i in numbers:
    print(i)
#program 1
#insert() method
numbers = [1,2,3]
numbers.insert(1,99)
print(numbers)
#program -2 
# remove() method 
fruits =["apple","banana","mango"]
fruits.remove("banana")
print(fruits)
# program -3 
#pop() method
numbers = [10,20,30]
numbers.pop(1)
print(numbers)
# program-4
numbers = [1,2,3,4,5]
for i in numbers:
    print(i)
#program -5
numbers = [10,20,30]
total = 0
for i in numbers:
    total += i
print("Sum = ",total)
# task 
#create list of color
colors = ["red","green","orange"]
print(colors)
print(len(colors))
# insert new color
colors.insert( 1,"pink")
print(colors)
#remove 
colors.remove("green")
print(colors)
#pop
colors.pop(-1)
print(colors)
#primting all items using loop
for i in colors:
    print(i)

