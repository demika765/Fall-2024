####################################
#insert PA header here
#Name: Demilade Sonola
#Assignment: PA7 - writing functions with FOR-Loops
#Due Date: 10/21/24
#Honor Code Statement: I received no assistance on this assignment that
#violates the ethical guidelines set forth by the professor and class syllabus
#Comments: N/A
####################################
#Task 1: takes an integer and computes its even factorial
####################################
def even_factorial(number):
    total = 1
    for i in range(1, number + 1):
        if (i%2 == 0):
            total *= i
    return total
        
#print(even_factorial(5))
#print(even_factorial(8))
####################################
#Task 2: takes an integer input and computes the sum of all integers from number up to number + 10, inclusive
####################################
def sum_from_n(number):
    total = 0
    for i in range(number, number + 11):
        total += i
    return total
#print(sum_from_n(3))
#print(sum_from_n(10))
####################################
#Task 3: takes an integer and adds up and returns the sum of all the odd numbers that are less than or equal to that number
####################################
def sum_odds(number):
    total = 0
    for i in range(1, number + 1):
        if (i%2 != 0):
            total += i
    return total
#print(sum_odds(5))
#print(sum_odds(10))
####################################
#Task 4: accepts two integers, bottom and top, and calculates the sum of numbers between bottom and top that are divisible by 3
####################################
def sum_3mults(bottom, top):
    total = 0
    for i in range(bottom, top + 1):
        if (i%3 == 0):
            total += i
    return total
#print(sum_3mults(1, 10))
#print(sum_3mults(9, 15))
#print(sum_3mults(6, 19))
####################################
#Task 5: takes two integers, first and second, and adds up and returns all the integers between divisible by 3 including the values themselves
####################################
def sum_div5_range(first, second):
    total = 0
    if (first >= second):
        for i in range(second, first + 1):
            if (i%5 == 0):
                total += i
    else:
        for i in range(first, second + 1):
            if (i%5 == 0):
                total += i
    return total
#print(sum_div5_range(25, 1))
#print(sum_div5_range(1, 10))
#print(sum_div5_range(15, 15))
#print(sum_div5_range(11, 11))
####################################
#Task 6: counts up and returns the number of proper factors of a given integer
####################################
    
def count_prop_facs(number):
    total = 0
    for i in range(1, number + 1):
        if (number%i == 0 and i != number):
            total += 1
    return total
#print(count_prop_facs(10))
#print(count_prop_facs(12))

####################################
#Task 7: compute and return the value of base raised to the power of exp
####################################
def custom_exponential(base, exp):
    total = 1
    if (exp > 0):
        for i in range(exp):
            total *= base
    elif (exp < 0):
        for i in range(-exp):
            total *= base
        total = 1/total
    elif (exp == 0):
            return 1
    return total
#print(custom_exponential(3, 4))
#print(custom_exponential(2, -3))
#print(custom_exponential(8, 0))
####################################
#Task 8: takes two integers as input and returns the number of common factors.
####################################
def common_factors_count(num1, num2):
    total = 0
    for i in range(1, num2):
        if (num1%i == 0 and num2%i == 0):
            total += 1
    return total
print(common_factors_count(9, 18))
print(common_factors_count(24, 36))