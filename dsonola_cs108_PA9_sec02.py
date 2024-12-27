##################################################
#Name: Demilade Sonola
#Assignment: PA9 - For Loops over Lists
#Due Date: 11/4/24
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
# Task 1:only_negs() takes a list of numbers and makes a new list that contains only the negative numbers from the original list
##################################################
def only_negs(numb):
    new_list = []
    for num in numb:
        if (num < 0):
            new_list.append(num)
    return(new_list)
#print(only_negs([-3,-1,2,6,8]))
#print(only_negs([2,12,6,16]))
##################################################
# Task 2:calc_avgs() takes a list of midterm and final exam scores and returns a list of averages
##################################################
def calc_avgs(mid_scores_lst, final_scores_lst):
    new_list = []
    for score in range(len(mid_scores_lst)):
        mid = mid_scores_lst[score]
        final = final_scores_lst[score]
        average = round((mid*0.4 + final*0.6), 1)
        new_list.append(average)
    return new_list
#print(calc_avgs([90],[100]))
#print(calc_avgs([80,80,60],[92, 88, 58]))
##################################################
# Task 3:coin_matches() takes a list of values and a list of names and returns the indices where value and name match
##################################################
def coin_matches(names_lst, values_lst):
    new_list = []
    for names in range(len(names_lst)):
        if names_lst[names] == 'penny' and values_lst[names] == 1:
            new_list.append(names)
        elif names_lst[names] == 'nickel' and values_lst[names] == 5:
            new_list.append(names)
        elif names_lst[names] == 'dime' and values_lst[names] == 10:
            new_list.append(names)
        elif names_lst[names] == 'quarter' and values_lst[names] == 25:
            new_list.append(names)
        elif names_lst[names] == 'dollar' and values_lst[names] == 100:
            new_list.append(names)
    return new_list
#print(coin_matches(['dime','dime','nickel'],[10,10,5]))
#print(coin_matches(['dime', 'dime', 'dime'], [10, 10, 5, 1]))
##################################################
# Task 4:greatest_neg() finds and returns the largest negative number in a list of numbers
##################################################
def greatest_neg(lst):
    storage = None
    if (lst == []):
        return 'No Elements'
    for num in lst:
        if (num < 0):
            if (storage == None) or (num > storage):
                storage = num
    if (storage == None):
        return 0
    return storage
#print(greatest_neg([1,6,2,8,9]))
#print(greatest_neg([-2,9,-1,0,3,-5]))
#print(greatest_neg([]))
##################################################
# Task 5:shift_insert() takes a list
##################################################
def shift_insert(lst, value, index):
    lst.append(0)
    for number in range(len(lst)-2, index -1, -1):
        lst[number + 1] = lst[number]
    lst[index] = (value)
    return lst
#print(shift_insert([5,2,8], 99, 2))
#print(shift_insert([6,-2,9,2,-4], 88, 0))
##################################################
# Task 6:adjust_list() takes a list 
##################################################
def adjust_list(lst):
    new_list = []
    for num in lst[:8]:
        new_list.append(num)
    for num in range(8 - len(new_list)):
        new_list.append(0)
    return new_list
#print(adjust_list([1,3,5]))
#print(adjust_list([1,2,3,4,5,6,7,8,9,10,11]))
#print(adjust_list(['a','a','a']))
#print(adjust_list([]))
##################################################
# Task 7:courses_with_A() 
##################################################
def courses_with_A(lst1, lst2):
    new_list = []
    for course in range(len(lst1)):
        if lst2[course] == 'A':
            new_list.append(lst1[course])
    return new_list
print(courses_with_A (['CS108','CS112','CS110'],['A','A','B']))
print(courses_with_A (['CS211','CS310','CS222'],['B','B','B']))