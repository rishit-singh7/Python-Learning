#5. Write a program which finds out whether a given name is present in a list or not.

l = ["Rohan", "Rohit", "Ramesh", "Rakesh", "Ravi"]

name = input("Enter your name: ")

if(name in l):
    print("The name is present in the list")
else:
    print("The name is not present in the list")