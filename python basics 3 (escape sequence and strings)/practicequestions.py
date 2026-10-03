name = input("Enter your name")  # Prompt the user to enter their name

print(f"Good Afternoon, {name}")  # use the f string to format the output with the user's name

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>","Rishit").replace("<|Date|>","september 26,2026"))  # Replace placeolders in the letter with actual values

string = "Harry is a  good boy."

print(string.find("  "))  # Find the index of the first occurrence of double spaces in the string



str = "Harry is a  good boy."

print(str.replace("  "," ")) # Replace double spaces with a single space in the string and print the result







