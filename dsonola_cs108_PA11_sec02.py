##################################################
#Name: Demilade Sonola
#Assignment: PA11 - Working With Tuples
#Due Date: 11/24/24
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
# Task 1: extremes(): returns a tuple containing the smallest and largest numbers in a list
#################################################
def extremes(my_list):
    if my_list == []:
        return None
    largest = my_list[0]
    smallest = my_list[0]
    for elem in my_list:
        if elem > largest:
            largest = elem
        if elem < smallest:
            smallest = elem
        if my_list == []:
            return None
    if len(my_list) == 1:
        return elem, None
    big_small = (smallest, largest)
    return big_small
#print(extremes([5, 4, 100, 33, 1, 9]))
#print(extremes([6]))
#print(extremes([]))
##################################################
# Task 2: find_range(): takes a list of numbers and returns the range
#################################################
def find_range(my_list):
    rng = extremes(my_list)
    if len(my_list) <= 1:
        return None
    else:
        return rng[1] - rng[0]
#print(find_range([5, 4, 100, 33, 1, 9]))
##################################################
# Task 3: lengths(): takes a two-dimentional list and counts the number of elements in each sublist
#################################################
def lengths(nested_list):
    elements = ()
    for tup in nested_list:
        counter = 0
        for elem in tup:
            counter += 1
        elements += (counter,)
    return elements
#print(lengths([[6,2],[1,2,2,8],[6,6]]))
#print(lengths([[6]]))
#print(lengths([[]]))
##################################################
# Task 4: count_vowels(): takes a list of characters and counts the number of each vowel that appears in the list
#################################################
def count_vowels(my_list):
    avowel = 0
    evowel = 0
    ivowel = 0
    ovowel = 0
    uvowel = 0
    for letter in my_list:
        if letter == "a":
            avowel += 1
        elif letter == "e":
            evowel += 1            
        elif letter == "i":
            ivowel += 1
        elif letter == "o":
            ovowel += 1
        elif letter == "u":
            uvowel += 1
    vowel_count = (avowel, evowel, ivowel, ovowel, uvowel)
    return vowel_count
#print(count_vowels(['e','a','r','t','h','l','i','n','g']))
#print(count_vowels(['a','e','o','o']))
#print(count_vowels([]))
##################################################
# Task 5: backwards(): takes a tuple and returns a list with the elements from the tuple in reverse order
#################################################
def backwards(my_tuple):
    list_result = []
    for elem in my_tuple[::-1]:
        list_result.append(elem)
    return list_result
#print(backwards((3,4,5,6,7)))
##################################################
# Task 6: generate_sequence(): takes a tuple containing two elements and generates a list from smallest to largest, incrementing by 1
#################################################
def generate_sequence(my_tuple):
    if my_tuple[0] < my_tuple[1]:
        (start, end) = my_tuple[0], my_tuple[1]
    else:
        (start, end) = my_tuple[1], my_tuple[0]
    sequence = []
    for elem in range(start, end + 1):
        sequence.append(elem)
    return sequence
#print(generate_sequence((2,6)))
#print(generate_sequence((8,5)))      
##################################################
# Task 7: count_distinct_elements(): finds the number of distinct elements in a tuple. If the tuple is empty, return None
#################################################
def count_distinct_elements(my_tuple):
    counter = 0
    if my_tuple == ():
        return None
    unique_elem = ()
    for elem in my_tuple:
        if elem not in unique_elem:
            unique_elem += (elem,)
            counter += 1
    return counter
#print(count_distinct_elements((1,1,1,2,3,3)))
#print(count_distinct_elements(('a','l',2,4,'b')))
#print(count_distinct_elements(()))
##################################################
# Task 8: largest_difference(): takes a list of tuples and computes the difference between the numbers in each tuple returning the largest difference
#################################################
def largest_difference(my_list):
    big_diff = 0
    for tup in my_list:
        if tup[0] > tup[1]:
            difference = tup[0] - tup[1]
        else:
            difference = tup[1] - tup[0]
        if difference > big_diff:
            big_diff = difference
    return big_diff
print(largest_difference([(1,5),(6,1),(10,9),(8,3)]))
print(largest_difference([(2,3),(1,9),(5,2),(6,8)]))

            
