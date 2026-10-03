a = int(input("Enter your age:"))

#First IF statement
if(a%2 == 0):
    print("The number is a Even Number")

# Second IF statement
if(a >= 18):
    print("You are above the age of consent")  #The blank space is indentation
    print("Good For You")
    
elif(a<=0):
    print("You are entering an invalid age")

else:
    print("You are below the age of consent")

print("End of program")

