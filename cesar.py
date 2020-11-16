#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:43:27 2020

@author: zizala
"""
#---FONCTIONS
#Coder le mot (chaine de caracteres) en suite de nombre (liste de nombre entieres)
#En fonction de position de la lettre dans l'alphabet
def letter_to_number(word):
    word_to_num = []
    for letter in word:
        letter = alphabet.index(letter)
        word_to_num.append(letter)
    return word_to_num

#Transcrire la liste de nombres entieres en chaine de caractere
#En fonction de position DECALEE de la lettre dans l'alphabet
#Decalage determine par la var shift
def number_to_letter(num_list, shift):
#    if type(shift) != int :
#        exit("C'est pas bon.")
#        return
    num_to_word = []
    for number in num_list:
        number = alphabet[number+shift]
        num_to_word.append(number)
    return ''.join(num_to_word)

#---VARIABLES
#Decalage d'index dans la liste alphabet (definie ci-dessous)
shift = 1
#Liste de 26 lettres d'alphabet
alphabet=[]
for i in range(65,91):
    alphabet.append(chr(i))


original_word = input('Ave Cesar, what do you want to say?').upper()
original_to_num = letter_to_number(original_word)
original_to_coded = number_to_letter(original_to_num,shift)
print('Your word coded: ', original_to_coded)

coded_to_num = letter_to_number(original_to_coded)
coded_to_original = number_to_letter(coded_to_num,-shift)
print('Your word decoded: ', coded_to_original)


