# Mixed data types in a list
data = [1, "Python", 3.5]
print(data)


# Add 2 values using extend() method
numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)


# Printing using loop
numbers = [10, 20, 30]

for i in numbers:
    print(i)


# Program 1 - insert() method
numbers = [1, 2, 3]
numbers.insert(1, 99)
print(numbers)


# Program 2 - remove() method
fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)


# Program 3 - pop() method
numbers = [10, 20, 30]
numbers.pop(1)
print(numbers)


# Program 4 - Printing list items using loop
numbers = [1, 2, 3, 4, 5]

for i in numbers:
    print(i)


# Program 5 - Sum of list items
numbers = [10, 20, 30]
total = 0

for i in numbers:
    total += i

print("Sum =", total)


# Task - Create list of colors
colors = ["red", "green", "orange"]
print(colors)
print(len(colors))


# Insert new color
colors.insert(1, "pink")
print(colors)


# Remove color
colors.remove("green")
print(colors)


# Pop color
colors.pop(-1)
print(colors)


# Printing all items using loop
for i in colors:
    print(i)