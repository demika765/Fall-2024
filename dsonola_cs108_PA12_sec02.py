##################################################
#Name: Demilade Sonola
#Assignment: PA12 - Working With Strings
#Due Date: 12/4/24
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
# Task 1: count_vowels()btakes a string and counts the number of vowels in the string
#################################################
def count_vowels(word):
    counter = 0 #counts the number of values
    for letter in word: #iterates through the word
        if letter in "AEIOUaeiou": #all the vowels stored as a string
            counter += 1 #adds to the counter if the letter is a vowel
    return counter
#print(count_vowels("strawberry"))
#print(count_vowels("This is not a test"))
#print(count_vowels("I am not going to clean up your mess, Anya!"))
##################################################
# Task 2: cap2() takes a word and capitalizes only the second and last letter
#################################################
def cap2(word):
    word = word.lower() #makes all the letters are lowercase
    if len(word) == 2:
        word = word[:1] + word[-1].capitalize()
    elif len(word) < 2:
        return word
#all above code handles cases in which the word is too short to be handled normally
    else:
        word = word[:1] + word[1].capitalize() + word[2:-1] + word[-1].capitalize()
#reassigns the value of word to the first letter + the 2nd letter capitalized + all but the last letter + the last letter capitalized
    return word
#print(cap2('Q'))
#print(cap2(''))
#print(cap2('ok'))
#print(cap2("seven"))
#print(cap2('Coffee'))
#print(cap2('GradeScope'))
##################################################
# Task 3: pig_latin() takes a word and converts the word to Pig Latin
#################################################
def pig_latin(word):
    if word[0] in "AEIOUaeiou": #all the vowels stored as a string
        return word + "ay" #if first letter is a vowel than it doesnt need to be added to the words end; just print word plus ay
    else:
        return word[1:] + word[0] + "ay" #if first letter is consonant add it to the end of the word before adding ay
#print(pig_latin('weekend'))
#print(pig_latin('coffee'))
#print(pig_latin('indoors'))
##################################################
# Task 4: def pig_latin_sentence(sentence) takes a sentence and converts it to pig latin
#################################################
def pig_latin_sentence(sentence):
    sentence = sentence.split() #splits sentence into individual words
    finalpig = '' #creates empty string for concatonation
    for word in range(len(sentence)):
        pigword = pig_latin(sentence[word])
        finalpig += pigword #string with only space to be added between words turned into pig latin
        if word < len(sentence) - 1: #if you havent gotten to the last word in the sentence
            finalpig += " " #add a space; this is so there isnt a space at the last word
    return finalpig
#print(pig_latin_sentence("happy birthday to you"))
#print(pig_latin_sentence("summer is coming and I couldn't be more excited"))
#print(pig_latin_sentence('Thanksgiving'))
##################################################
# Task 5: count_these() takes a string and a list and counts the number of occurrences of the characters that occur
#################################################
def count_these(word, char_list):
    counter = 0 #will count occurences
    for letter in word:
        if letter in char_list:
            counter += 1 #if a letter in the word is in the character list add to the counter
    return counter
#print(count_these("strawberry", ['r','a']))
#print(count_these("This is not a test", ['s']))
#print(count_these("Mississippi",['s','i','p']))
##################################################
# Task 6: hidden_word_horiz() takes a 5x5 list of 5 letter long words, and a 3 letter word and finds the word in the box horizontally
#################################################
def hidden_word_horiz(box, word):
    letter_list = "" #creates empty string to concatonate to
    for phrase in box:
        for letter in phrase: #enters the first letter in the 2d list
            letter_list += letter #adds the letter to a new string 
    if word in letter_list: #if the word is in the string of letters 
        return True
    else:
        return False
box = ['roast',
'ectro',
'dtopk',
'grooe',
'pinky']
#print(hidden_word_horiz(box, 'pin'))
#print(hidden_word_horiz(box, 'and'))
#print(hidden_word_horiz(box, 'top'))
##################################################
# Task 7: hidden_word_vert() takes a 5x5 list of 5 letter long words, and a 3 letter word and finds the word in the box vertically
#################################################
def hidden_word_vert(box, word):
    for letter in range(5): #goes through all 5 words in the 2d list
        for phrase in range(3): 
            vert_word = box[phrase][letter] + box[phrase + 1][letter] + box[phrase + 2][letter] #length of word is three so count up to 3
            if vert_word == word: #vert_word has all the letters up to 3 vertically assigned to it 
                return True
    return False
#print(hidden_word_vert(box, 'red'))
#print(hidden_word_vert(box, 'key'))
#print(hidden_word_vert(box, 'top'))
##################################################
# Task 8: hidden_word() takes a 5x5 list of 5 letter long words, and a 3 letter word and finds the word in the box
#################################################
def hidden_word(box, word): #body of this function is just the previous 2 functions copy pasted
    letter_list = ""
    for phrase in box:
        for letter in phrase:
            letter_list += letter
    if word in letter_list:
        return True
    for letter in range(5):
        for phrase in range(3):
            vert_word = box[phrase][letter] + box[phrase + 1][letter] + box[phrase + 2][letter]
            if vert_word == word:
                return True
    return False
print(hidden_word(box, 'red'))
print(hidden_word(box, 'and'))
print(hidden_word(box, 'top'))
