# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import copy
import re
import io

def idiot_check(queston):
    
    answer = input(queston)
    while answer not in correctanswers:
        answer = input('Не тупи! '+queston)
    return answer

def input_letter():
    
    
    letter = input('Введите букву или несколько букв номер которых вы не знаете: ')
    while not re.match('[а-яА-Яъьы]', letter):
        letter = str.upper(input('Не тупи! Введи букву: '))
    
    number = None
    if len(letter)==1:
        ans = idiot_check("Вы знаете номер буквы? Д/Н: ")
        if ans == 'д' or ans == 'Д':
            number = input('Введите номер буквы: ')
            while number not in z:
                number = input('Не тупи! Введи номер буквы: ')
    
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
    print("\nВвод букв отсутвующих в слове")
    
    while True:
        
        temp = list(input_letter())
        if len(temp[0])>1: 
            temp2 = re.sub('\W+', '', temp[0])
            for i in temp2:
                no_letters.append([i,None])
        else:
            no_letters.append(temp)
        ans = idiot_check('Ещё одну? Д/Н: ')
        if ans == 'Н' or ans == 'н':
            break    
        
def letter_append():
    print("\nВвод букв присутсвующих в слове")
    
    while True:
        temp = list(input_letter())
        if len(temp[0])>1: 
            temp2 = re.sub('\W+', '', temp[0])
            for i in temp2:
                letters.append([i,None])
        else:
            letters.append(temp)
        ans = idiot_check('Ещё одну? Д/Н: ')
        if ans == 'Н' or ans == 'н':
            break    
          

letters = []
correctanswers = ['Д','Н','З','д','н','з']
no_letters = []
list_of_words = []    
words_with_5_letters = []
count = 0 
z = ('1',"2","3","4","5")
a = 1
n = 0


with io.open('dict.txt',mode = 'r',encoding="utf-8" ) as infile:
    for line in infile:
        words_with_5_letters.append(str.upper(line[0:5]))


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
        print("\n")
        for i in range(0,len(list_of_words)):
            print(list_of_words[i], end='  ')
            if ((i+1)%5)==0 and i!=0:
                print('\n')
        print('\n')
        main_ans = input('Добавить букву или начать заново? Д/Н/З: ' )
        if main_ans == 'Д' or main_ans == 'д':
           letter_append()
        elif main_ans == 'З' or main_ans =='з':
            q=0
            letters = []
            no_letters = []
            list_of_words = copy.copy(words_with_5_letters)
            letter_append()
            no_letter_append()
        else:
            q = 0
            break
    else:
        print('Подходящих слов не найдено(\n Restarting')
        q=0
        letters = []
        no_letters = []
        list_of_words = copy.copy(words_with_5_letters)
        letter_append()
        no_letter_append()