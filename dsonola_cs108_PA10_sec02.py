##################################################
#Name: Demilade Sonola
#Assignment: PA10 - Nested Loops and 2D Lists
#Due Date: 11/18/24
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
# Task 1: merge_namelist() combines two lists into a single list of unique names, ensuring that each attendee is listed only once
##################################################
def merge_namelist(namelst1, namelst2):
    uniquelst = []
    uniquelst2 = []
    for name in range(len(namelst1)):
        uniquelst.append(namelst1[name])
    for name in range(len(namelst2)):
        uniquelst.append(namelst2[name])
    for name in range(len(uniquelst)):
        if uniquelst[name] not in uniquelst2:
                uniquelst2.append(uniquelst[name])
    return uniquelst2
#print(merge_namelist(["Hanna", "Jaime"],["Hanna", "Lynn"]))
#print(merge_namelist(['John', 'Mary', 'Ashley', 'William', 'Jessica'], ['Michael', 'Jennifer', 'James', 'Emily', 'Robert']))
##################################################
# Task 2: menu() creates a menu for a bakery that offers different flavors of pastries with variousvtoppings
##################################################
def menu(flavors, toppings):
    yummylst = []
    for flav in flavors:
        for topp in toppings:
            yummylst.append(flav + ' ' + topp)
    return yummylst
#flavors = ["Vanilla", "Chocolate"]
#toppings = ["Sprinkles", "Almonds"]
#print(menu(flavors, toppings))
##################################################
# Task 3: count_one_name() takes a list of names and a single name and returns the total number of occurrences of the single name in the list
##################################################
def count_one_name(all_names, common_name):
    counter = 0
    for name in range(len(all_names)):
        if all_names[name] == common_name:
            counter += 1
    return counter
#all_names = ["Earl", "Cathy", "Petra", "Earl", "Jane", "Petra", "Jane", "Omar", "Earl", "Jane", "Cathy", "Kendra", "Earl", "Beth",
#"Bari", "Petra", "Cathy", "Earl", "Petra", "Horace", "Bert"]
#common_name = "Petra"
#print(count_one_name(all_names, common_name))
##################################################
# Task 4: count_many_names() takes two lists of names and returns the total number of occurrences of the common names in the larger list
##################################################
def count_many_names(all_names, common_names):
    counter = 0
    for name in all_names:
        for names in common_names:
            if name == names:
                counter += 1
    return counter
#all_names = ["Earl", "Cathy", "Petra", "Earl", "Jane", "Joan", "Jane", "Omar", "Earl", "Jane", "Cathy", "Kendra", "Earl", "Beth", "Bari", "Hanna", "Cathy", "Earl", "Armando", "Horace", "Bert"]
#common_names = ["Earl", "Petra", "Jane"]
#print(count_many_names(all_names, common_names))
##################################################
# Task 5: sum_up() takes a list of mini-lists that contain numbers and finds the sum of all the numbers in the mini-lists 
##################################################
def sum_up(list_of_lists):
    final = 0
    for i in list_of_lists:
        for elem in i:
            final += elem
    return final
#list1 = [[3,4,5],[6,7,8],[1,1,1,1]]
#print(sum_up(list1))
##################################################
# Task 6: find_largest() takes a list of mini-lists that contain numbers and finds the largest of all the numbers  
##################################################
def find_largest(list_of_lists):
    final = 0
    for i in list_of_lists:
        for elem in i:
            if (elem > final):
                final = elem
    return final
#list1 = [[3,4,5],[6,7,8],[1,1,1,1]]
#print(find_largest(list1))
#list2 = [[], [100], [1], [],[]]
#print(find_largest(list2))
##################################################
# Task 7:  is_square() takes a 2-dimensional list of values and determines if the 2-dimensional list is a square
##################################################
def is_square(twoD_list):
    counter1 = 0
    counter2 = 0
    for i in twoD_list:
        counter1 += 1
    for elem in i:
        counter2 += 1
    if (counter1 == counter2):
        return True
    else:
        return False
list1 = [[3,4,5],
         [6,7,8],
         [1,1,1]]
list2 = [[], [100], [1], [],[]]
print(is_square(list1))
print(is_square(list2))