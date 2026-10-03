#PROBLEM 1  Write a program to create a dictionary of Hindi words with values as their English
#translation. Provide user with an option to look it up!


Names = {"Kutta": "Dog",
         "Billi": "Cat",
         "Kursi": "Chair"
}

name = input("Enetr the name of the OBJECT:")

print("Your Translated word is:",Names[name])

#PROBLEM2 Write a program to input eight numbers from the user and display all the unique numbers

Numbers = set()

number = input("Enter your number:")
Numbers.add(int(number))
number = input("Enter your number:")
Numbers.add(int(number))
number = input("Enter your number:")
Numbers.add(int(number))
number = input("Enter your number:")
Numbers.add(int(number))
number = input("Enter your number:")
Numbers.add(int(number))
number = input("Enter your number:")
Numbers.add(int(number))
number = input("Enter your number:")
Numbers.add(int(number))

print(Numbers)

