#6. Write a program to calculate the grade of a student from his marks from the following
#scheme:
#90 – 100 => Ex
#80 – 90 => A
#70 – 80 => B
#60 – 70 => C
#50 – 60 => D
#<50 => F

marks = int(input("Enter your marks:" ))

if(marks>= 90 and marks<=100):
    print ("YOUR GRADE IS :EXCELLENT")
if(marks>=80 and marks<90):
    print ("YOUR GRADE IS : A")
if(marks>= 70 and marks<80):
    print ("YOUR GRADE IS : B")
if(marks>= 60 and marks<70):
    print ("YOUR GRADE IS : C")
if(marks>=50 and marks <60):
    print ("YOUR GRADE IS : D")
if(marks<50):
    print ("YOUR GRADE IS : F")
