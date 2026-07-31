# String slicing

name = "Python"
print(name[0:3])  # Pyt
print(name[2:5])  # tho

a = "Lalitendra"
print(a[:5])
print(a[5:])

x = "Doctor"
print(x[-3:])


# Task

# 1. Take your name
c = "Lalitendra"
print(c[0:3])
print(c[-4:])
print(c[4:6])


# Challenge
k = input("Enter your name: ")
print(k[0])
print(k[-1])
print(k[0:4])


c = input("Enter your name: ")
mid = len(c) // 2

if len(c) >= 3:
    print(c[mid - 1:mid + 2])


name = "Lalitendra"
half = len(name) // 2
print(name[:half])

if name:
    print(name[0], name[1])


# Reverse a string
k = "python"
print(k[::-1])

print(k[::2])  # Print every second character


Name = input("Enter name: ")
half = len(Name) // 2
print("First half:", Name[:half])
print("Second half:", Name[half:])


j = input("Enter Your name: ")
print("Last 3 letters:", j[-3:])


w = "Lalitendra"
print(w[1::2])


# Palindrome
word = input("Enter word: ").lower()

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")