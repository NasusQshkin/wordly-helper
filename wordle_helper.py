# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import copy
import re
def idiot_check(queston):
    
    answer = input(queston)
    while answer not in correctanswers:
        answer = input('Are u dumb? '+queston)
    return answer

def input_letter():
    
    
    letter = input('Input letter: ')
    while len(letter)>1 or not re.match('[а-яА-Я]', letter):
        letter = str.upper(input('Input letter: '))
    
    number = None
    ans = idiot_check("you're know letter number? Y/N: ")
    if ans == 'Y' or ans == 'y':
        number = input('Input this letter number: ')
        while number not in z:
            number = input('Input this letter number: ')
    return letter,number


def words_out(word):
    if count < len(letters):
        if word in list_of_words:
            if letters[count][1] == None:
                if letters[count][0] not in word:
                    list_of_words.remove(word)
            else:
                if letters[count][0] != word[int(letters[count][1])-1] or letters[count][0] not in word:
                    list_of_words.remove(word)
    if count < len(no_letters):
        if word in list_of_words:
            if no_letters[count][1] == None:
                if no_letters[count][0] in word:
                    list_of_words.remove(word)


def no_letter_append():

    while True:
        print("Ввод букв отсутвующих в слове")
        no_letters.append(list(input_letter()))
        ans = idiot_check('want continue? Y/N: ')
        if ans == 'N' or ans == 'n':
            break    
        
def letter_append():
    global q
    q = 0
    print("Ввод букв присутсвующих в слове")
    while q<=4:
        letters.append(list(input_letter()))
        q+=1
        ans = idiot_check('want continue? Y/N: ')
        if ans == 'N' or ans == 'n':
            break    
          

letters = []
correctanswers = ['Y','N','R','r','n','y']
no_letters = []
list_of_words = []    
words_with_5_letters = []
count = 0 
z = ('1',"2","3","4","5")
a = 1
n = 0


with open('3.txt','r') as infile:
    for line in infile:
        words_with_5_letters.append(line[0:5])


letter_append()
no_letter_append()
       
list_of_words = copy.copy(words_with_5_letters) 
while True:
    for word in words_with_5_letters:
        while count < max(len(letters),len(no_letters)):
            words_out(word)
            count+=1
        count=0
    if len(list_of_words)>0:    
        print(list_of_words)
        main_ans = input('Add letter or restart? Y/N/R: ' )
        if main_ans == 'Y' or main_ans == 'y':
           letter_append()
        elif main_ans == 'R' or main_ans =='r':
            q=0
            letters = []
            no_letter = []
            list_of_words = copy.copy(words_with_5_letters)
            letter_append()
            no_letter_append()
        else:
            q = 0
            break
    else:
        print('No words( Restarting')
        q=0
        letters = []
        no_letters = []
        list_of_words = copy.copy(words_with_5_letters)
        letter_append()
        no_letter_append()
   