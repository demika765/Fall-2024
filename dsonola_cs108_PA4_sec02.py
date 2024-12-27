
#insert PA header here!!!
#Name: Demilade Sonola
#Assignment: #4
#Due Date: 9/22/24
#Honor Code Statement: I received no assistance on this assignment that
#violates the ethical guidelines set forth by the professor and class syllabus
#Comments: N/A
####################################
#  Task 1: Convert centimeters to inches
####################################
def cm_to_in(c):
    inches = c/2.54
    return round(inches, 1)

print(cm_to_in(25.4))
#print((cm_to_in(30.5)))
#print((cm_to_in(69)))
#print((cm_to_in(145)))
# write and print out some test cases
# COMMENT OUT YOUR TEST CASES before you submit to GradeScope

# Task 2: Calculate the perimeter of a rectangle
####################################
def rect_perimeter(l, w):
    perimeter = (l*2)+(w*2)
    return perimeter

print(rect_perimeter(4, 6))
#print(rect_perimeter(2.5, 7))
#print(rect_perimeter(5, 5))
#print(rect_perimeter(1, 3))
#test cases, etc

# Task 3: Find the average of six numbers
#####################################
def avg_six(a, b, c, d, e, f):
    average = (a+b+c+d+e+f)/6
    return round(average, 2)
print(avg_six(10, 10, 10, 30, 30, 30))
#print(avg_six(2, 4, 6, 1, 3, 5))
#print(avg_six(1, 9, 42, 16, 93, 6))

# Task 4: Calculates x^y-y
#####################################
def reliant_num(x, y):
    answer = (x**y)-y
    return answer
print(reliant_num(7, 3))
#print(reliant_num(4, 2))
#print(reliant_num(11, 6.9))

# Task 5: Calculates the price of a bluetooth speaker
#####################################
def speaker_price(price, discount, tax):
    cost = (price-(price*(discount*0.01)))
    total = cost+(cost*(tax*.01))
    return round(total, 2)
print("Speaker price is", speaker_price(100.00, 11, 7))
#print(speaker_price(85.79, 50, 2))
#print(speaker_price(17.38, 42, 69))

# Task 6: Calculates the number of sleeves Kenia can bring if only full sleeves are allowed
#####################################
import math
def cups_to_sleeves(c):
    sleeves = math.ceil(c/50)
    return sleeves
print(cups_to_sleeves(165))
#print(cups_to_sleeves(170))
#print(cups_to_sleeves(536))

# Task 7: Returns a determinant of a quadratic function
#####################################
def determinant(a, b, c):
    answer = (b**2)-4*a*c
    return answer
print(determinant(4, 7, 3))
#print(determinant(6, 2, 9))

