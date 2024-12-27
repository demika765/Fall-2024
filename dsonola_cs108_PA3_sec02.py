##################################################
#Name: Demilade Sonola
#Assignment: #2
#Due Date: 9/9/24
#Honor Code Statement: I received no assistance on this assignment that
#violates the ethical guidelines set forth by the professor and class syllabus
#Comments: N/A
##################################################

#################################################
###        DO NOT CHANGE THIS SECTION         ###
#################################################
def largest(x, y, z):							#
    if (x >= y) and (x >= z):					#
        return x								#
    if (y >=x) and (y >= z):					#
        return y								#
    return z									#
                                                #
def average_three(a,b,c):						#
    return (a+b+c)/3							#
                                                #
def mystery_fn(a,b,c):							#
    return (b//c)*(c%b)							#
                                                #
def odd_or_even(the_num):						#
    if (the_num%2)==0:							#
        result = "even"							#
    else:										#
        result = "odd"							#
    return result								#
##### END OF 'DO NOT CHANGE' SECTION ############


##################################################
###                   PA3 Work                 ###
##################################################
 
# Task 1: Getting values from user
####################################
int1 = float(input("What is the first integer?"))
int2 = float(input("What is the second integer?"))
int3 = float(input("What is the third integer?"))
float1 = float(input("What is the first float?"))
float2 = float(input("What is the second float?"))
float3 = float(input("What is the third float?"))
##  Task 2: find the largest
#############################
print("Largest is:" ,largest(5, 12,9))
print("Largest is:" ,largest((int(int1)), (int(int2)),(int(int3))))
print("Largest is:" ,largest((float1), (float2),(float3)))
print()
##  Task 3: average of 3
#############################
print("The average is:" ,(average_three(2.009, 19.7,12.002)))
print("The average is:" ,round(average_three((int1), (int2),(int3)), 1))
print("The average is:" ,round(average_three((float1), (float2),(float3)), 2))
## Task 4: Mystery
###############################
print()
print("The mystery result is:" ,mystery_fn((int(int1)), (int(int2)),(int(int3))))
print("The mystery result is:" ,mystery_fn((int(int3)), (int(int1)),(int(int2))))
print("The mystery result is:" ,mystery_fn((int(int1)), (int(int1)),(int(int1))))
## Task 5: test odd/even
###############################
print()
print(int(int1) , "is" ,odd_or_even(int1))
print(int(int2) , "is" ,odd_or_even(int2))
print(int(int3) , "is" ,odd_or_even(int3))
## Task 6: test odd/even on results of mystery_fn()
###############################
print()
print("First result is" ,odd_or_even(mystery_fn((int(int1)), (int(int2)), (int(int3)))))
print("Second result is" ,odd_or_even(mystery_fn((int(int3)), (int(int1)), (int(int2)))))
print("Third result is" ,odd_or_even(mystery_fn((int(int1)), (int(int1)), (int(int1)))))

