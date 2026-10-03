marks = {"Harry": 100,
"Rohan": 26,
"Sohan" : 45}

print(marks.items())  #by marks.items() we can print th keys along with its values

print(marks.keys()) #by marks.key() we print the the keys 

print(marks.values()) #by marks.values() we can print the values

marks.update({"Harry":99, "Renuka":100}) # dictionary is mutable and by marks.upadate we can change the value of keys or add any new keys

print(marks)

# Difference between print(marks.get("")) and print(marks["Harry"])

print(marks.get("Harry"))

print(marks["Harry"])

#Both print 99

print(marks.get("Harry2")) # This shows none

print(marks["Harry2"]) #This shows key error