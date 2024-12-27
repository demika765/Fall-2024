
#insert PA header here
#Name: Demilade Sonola
#Assignment: #5
#Due Date: 9/30/24
#Honor Code Statement: I received no assistance on this assignment that
#violates the ethical guidelines set forth by the professor and class syllabus
#Comments: N/A


#  Task 1: takes an integer and adds up and returns all the numbers from one to the integer
####################################
def sum_up(number):
    counter = 0
    total = 0
    while (counter <= number):
        total += counter
        counter += 1
    return  total
#print(sum_up(5))
#print(sum_up(9))
# write and print out some test cases
# COMMENT OUT YOUR TEST CASES before you submit to GradeScope

# Task 2: adds up all the numbers between and including a bottom and top integer
####################################
def sum_up2(bottom, top):
    counter = bottom
    total = bottom
    while (counter < top):
        counter += 1
        total += counter
    return total
#print(sum_up2(2, 3))
#print(sum_up2(2, 2))
#print(sum_up2(15, 19))

# Task 3: adds up and returns all multiples of 5 given an integer
#####################################
def sum_fivers(number):
    counter = 0
    total = 0
    while (counter <= number):
        total += counter
        counter += 5
    return total
#print(sum_fivers(5))
#print(sum_fivers(19))

# Task 4: Returns how many multiples of 5 an integer has
#####################################
def count_fivers(number):
    counter = 0
    total = 0
    while (counter < (number//5)):
        total += counter
        counter += 1
    return counter
#print(count_fivers(5))
#print(count_fivers(19))
#print(count_fivers(40))

# Task 5: Calculates and returns the counter to the power of the exp
#####################################
def power_up(base, exp):
    counter = 1
    total = base
    while (counter < exp):
        total = total * base
        counter += 1
    return total
#print(power_up(2, 3))
#print(power_up(5, 5))

# Task 6:Takes a number and starting from 1 checks if numbers in range are even or odd 
#if even, squares the number and adds it to the total
#if odd, multiplies the number by 2 and adds it to the total
#####################################

def mystery_sum(number):
    counter = 1
    total = 0
    while (counter < number):
        if ((counter%2) == 0):
            total += counter ** 2
        elif ((counter%2) != 0):
            total += counter * 2
        counter += 1
    return total
#print(mystery_sum(4))
#print(mystery_sum(13))

# Task 7: Takes a number and starting from 1 checks if numbers in range are even or odd 
#if even, divides the number by 2 and squares it, then adds it to the total
#if odd, squares the number and adds it to the total
#####################################
def mystery_sum2(number):
    counter = 1
    total = 0
    while (counter < number):
        if ((counter%2) == 0):
            total += (counter/2) ** 2
        elif ((counter%2) != 0):
            total += counter ** 2
        counter += 1
    return total
#print(mystery_sum2(4))
#print(mystery_sum2(13))

# Task 8: Compares the output of mystery_sum and mystery_sum2
#####################################
def bigger_mystery(number):
    if (mystery_sum(number) > mystery_sum2(number)):
        return 'ONE'
    elif (mystery_sum(number) < mystery_sum2(number)):
        return 'TWO'
    elif (mystery_sum(number) == mystery_sum2(number)):
        return 'SAME'
#print(bigger_mystery(5))
#print(bigger_mystery(20))
#print(bigger_mystery(0))