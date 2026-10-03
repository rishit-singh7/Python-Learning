##2. Write a program to find out whether a student has passed or failed if it requires a total of
#40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
#input from the user.

n1 = int(input("Enter marks of subject 1 :"))
n2 = int(input("Enter marks of subject 2 :"))
n3 = int(input("Enter marks of subject 3 :"))
n4= int(input("Enter marks of subject 4 :"))

total = n1 + n2 + n3 + n4
percentage = total/400 * 100

if(percentage>=40 and n1>=33 and n2>=33 and n3>=33 and n4>=33):
    print("Congratulations! You have passed the exam:", percentage, "%")

else:
    print("Better Luck Next Time! You have Failed the exam")


