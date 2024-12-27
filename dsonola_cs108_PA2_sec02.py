'''
-------------------------------------------------------------------------------
Name: Demilade Sonola
Assignment: #2
Due Date: 9/9/24
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
Comments: N/A
-------------------------------------------------------------------------------
'''

####################################
# Task 1: Average six numbers together
####################################
test1 = 99
test2 = 89
test3 = 86
test4 = 88
test5 = 92
test6 = 95
avg = (test1 + test2 + test3 + test4 + test5 + test6)/6
print("The average is" , avg , ".")
print()
####################################
#Task 2: Solve the quadratic formula
####################################
a = 1
b = 0
c = -9
ans1 = (-b +((b**2 - 4*a*c)**0.5))/(2*a)
ans2 = (-b -((b**2 - 4*a*c)**0.5))/(2*a)

print("The first root is" , ans1 , ".")
print("The second root is" , ans2 , ".")
####################################
#Task 3: Solve the quadratic formula with reassigned variables
####################################
a = 1
b = -10
c = -24
ans1 = (-b +((b**2 - 4*a*c)**0.5))/(2*a)
ans2 = (-b -((b**2 - 4*a*c)**0.5))/(2*a)

print()
print("The first root is" , ans1 , ".")
print("The second root is" , ans2 , ".")
####################################
#Task 4: Calculate feet and additional inches
####################################
one = 50
feet1 = one//12
inches1 = one%12
two = 100
feet2 = two//12
inches2 = two%12
three = 122
feet3 = three//12
inches3 = three%12
four = 8986
feet4 = four//12
inches4 = four%12

print()
print(one , "inches is" , feet1 , "feet and" , inches1 ,  "inches.")
print(two , "inches is" , feet2 , "feet and" , inches2 ,  "inches.")
print(three , "inches is" , feet3 , "feet and" , inches3 ,  "inches.")
print(four , "inches is" , feet4 , "feet and" , inches4 ,  "inches.")
