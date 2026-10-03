a = ("rohan", 12,23.54,"Gaurav") # a tuple is a collection of values
print(type(a))

NO = a.count("Gaurav") # count method counts the number of occurrences of a specific value in the tuple
print(NO)

no = a.index("Gaurav") # index method returns the index of the first occurrence of a specific value in the tuple

print(no)
##############################################
t = (1,2,3,4,5,6,7,8,9,0,-1,10,112,234,-87,5,-34,-2,2,2,22,2)

print(t.count(2)) # 4

print(max(t)) #234

print(min(t)) #-84

print(len(t)) #22

print(sum(t)) #310

print(sorted(t)) #[-87, -34, -2, -1, 0, 1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 22, 112, 234]

sliced = t[1:4]

print(sliced) #(2, 3, 4)



