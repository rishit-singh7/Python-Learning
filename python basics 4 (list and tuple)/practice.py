## Write a program to store three fruits in a list entered by the user

fruits = []

f1 = input("Enter fruit name:")
fruits.append(f1)

f2 = input("Enter fruit name:")
fruits.append(f2)

f3 = input("Enter fruit name:")
fruits.append(f3)

print(fruits)


#Write a program to accept marks of 3 students and display them in a sorted manner.

Marksheet = []

s1 = int(input("Enter your score:"))
Marksheet.append(s1)

s2 = int(input("Enter your score:"))
Marksheet.append(s2)

s3 = int(input("Enter your score:"))
Marksheet.append(s3)
print(Marksheet)

Marksheet.sort()

print("Sorted Marks:",Marksheet)


