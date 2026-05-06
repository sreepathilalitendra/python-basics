c = input("Enter your name:")
mid = len(c)//2
if len(c) >=3:
 print(c[mid-1:mid+2])
name = "Lalitendra"
half = len(name)//2
print(name[:half])
if name:
    print(name[0],  name[1])
# reverse a string 
k = "python"
print(k[::-1])
print(k[::2])#print second character
Name = input("Enter name:")
half = len(Name)//2
print("First half:",Name[:half])
print("Second half:",Name[half:])
j = input("Enter Your name:")
print("Last 3 letters:",j[-3:])
w ="Lalitendra"
print(w[1::2])
word = input("Enter word:").lower()
if word == word[::-1]:
    print("palindrome")
else:
    print("Not palindrome")    