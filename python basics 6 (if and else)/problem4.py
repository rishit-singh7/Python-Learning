#4. Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your name")

if (len(username) < 10 ):
    print("The username has less than 10 characters")
else:
    print("All is okay")