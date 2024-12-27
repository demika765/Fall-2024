##################################################
#Name: Demilade Sonola
#Assignment: PA8 - For Loops over Lists
#Due Date: 10/28/24
#Honor Code Statement: I received no assistance on this assignment that
#violates the ethical guidelines set forth by the professor and class syllabus
#Comments: N/A
##################################################
##################################################
# By submitting this programming assignment, you 
# acknowledge your responsibility to complete   
# all aspects of the assignment independently,  
# without seeking assistance from any online    
# sources. This assignment is to be conducted   
# in accordance with the GMU and Computer       
# Science honor code, and any violation will be 
# promptly reported to the Office of Academic   
# Integrity.                                    
##################################################
# Task 1:add_elems() takes a list and returns the sum of the elements in the list
##################################################
def add_elems(num_list):
    total = 0
    for num in (num_list):
        total += num
    return total
#print(add_elems([1,2,3,4,5]))
#print(add_elems([8, 1, 4, 5, 2, 100]))
##################################################
# Task 2:total_value() takes a list of coin names and returns the total value in cents of the coins in the list
##################################################
def total_value(coins):
    total = 0
    for coin in (coins):
        if (coin == 'dollar'):
            total += 100
        elif (coin == 'quarter'):
            total += 25
        elif (coin == 'dime'):
            total += 10
        elif (coin == 'nickel'):
            total += 5
        elif (coin == 'penny'):
            total += 1
    return total
#lst = ['dime', 'dime', 'nickel']
#print(total_value(lst))
#lst = ['penny', 'nickel', 'penny', 'quarter', 'penny']
#print(total_value(lst))
##################################################
# Task 3: count_nickels() takes a list of coin names and returns the number of nickels in the list
##################################################
def count_nickels(coins):
    total = 0
    for coin in (coins):
        if (coin == 'dollar'):
            total += 100
        elif (coin == 'quarter'):
            total += 0
        elif (coin == 'dime'):
            total += 0
        elif (coin == 'nickel'):
            total += 1
        elif (coin == 'penny'):
            total += 0
    return total
#print(count_nickels(['dime','nickel','nickel','penny','dime']))
#print(count_nickels(['quarter','quarter','quarter']))
##################################################
# Task 4: even_index_sum() takes a list of numbers and generates a number for the list by taking the sum of the indices that hold an even number
##################################################
def even_index_sum(num_lst):
    total = 0
    for num in range(len(num_lst)):
        if (num_lst[num]%2 == 0):
            total += num
    return total
        
#print(even_index_sum([1,2,3,4,5,6]))
#print(even_index_sum([102]))
#print(even_index_sum([3,5,7]))
##################################################
# Task 5: half_em() takes a list of numbers and replaces the even numbers with half their value
##################################################
def half_em(lst):
    for num in range(len(lst)):
        if (lst[num]%2 == 0):
            lst[num] = int(lst[num]/2)
    return lst
#print(half_em([1,6,10,5]))
#print(half_em([3, 4, 20, 5, 32]))
##################################################
# Task 6: avg_pos() takes a list of numbers and return the average of the positive numbers
##################################################

def avg_pos(lst):
    total = 0
    counter = 0
    for num in (lst):
        if (num > 0):
            total += num
            counter += 1
    if (counter == 0):
        return 0
    return round(total/counter, 1)
#print(avg_pos([1,2,9,-9,-10]))
#print(avg_pos([-1,-2]))
#print(avg_pos([]))
##################################################
# Task 7: odd_or_even() takes a list of integers and determines whether there are more odd  or even numbers
##################################################
def odd_or_even(lst):
    even_count = 0
    odd_count = 0
    for num in range(len(lst)):
        if (lst[num]%2 == 0):
            even_count += 1
        elif (lst[num]%2 != 0):
            odd_count += 1
    if (even_count > odd_count):
        return 'Even'
    elif (odd_count > even_count):
        return 'Odd'
    else:
        return 'Equal'
#print(odd_or_even([1,2,3,4,5]))
#print(odd_or_even([6,8,9]))
#print(odd_or_even([2,6,5,9]))
#print(odd_or_even([]))
   

        





