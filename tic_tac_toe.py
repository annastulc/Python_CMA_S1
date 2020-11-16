#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:59:12 2020

@author: zizala
"""
#---FONCTIONS
#Visualiser le plateau du jeu, cases innoccupees marquees par numero, cases occupees par un symbole "X" ou "O"
def print_grille():
    print(list_cases[0],"|",list_cases[1],"|", list_cases[2])
    print("-----")
    print(list_cases[3],"|",list_cases[4],"|",list_cases[5])
    print("-----")
    print(list_cases[6],"|",list_cases[7],"|",list_cases[8])

#Demander l'entree du joueur(numero de case ou il veut placer son symobole)
def input_player(joueur):
    print("C'est a joueur ",joueur,".") 
    position = int(input("Ou voulez vous jouer?"))
    list_cases[position-1] = joueur
    print_grille()

#Determiner si c'est le tour de "X" ou de "O"   
def definir_joueur():
    denominateur_tour=int()
    if denominateur_tour%2 == 0:
        joueur = "X"
    else:
        joueur = "O"
        
#Verifier si la victoire a ete atteinte par le "X" ou le "O"    
def verify_victory():
    victory_diagonals = bool(list_cases[0]==list_cases[4]==list_cases[8] or list_cases[2]==list_cases[4]==list_cases[6])
    victory_columns = bool(list_cases[0]==list_cases[3]==list_cases[6] or list_cases[1]==list_cases[4]==list_cases[7] or list_cases[2]==list_cases[5]==list_cases[8])
    victory_rows = bool(list_cases[0]==list_cases[1]==list_cases[2] or list_cases[3]==list_cases[4]==list_cases[5] or list_cases[6]==list_cases[7]==list_cases[8])
    if(victory_rows or victory_columns or victory_diagonals == True):
        return True
    else:
        return False
#En commentaire, la facon precedente de determiner les colonnes et les lignes gagnantes
#    while victory_rows == False:
#        for n in (0,3,6):
#            victory_rows = bool(list_cases[n]==list_cases[n+1]==list_cases[n+2])
#    while victory_columns == False:
#        for n in (0,1,2):
#            victory_columns = bool(list_cases[n]==list_cases[n+3]==list_cases[n+6])  

#Demander aux joueurs qu'ils placent les symboles tant que la victoire n'est pas acquise
#ou toutes les cases ne sont pas remplies
def play():
    victory = False
    denominateur_tour = 0
    joueur = "X"
    while victory == False and denominateur_tour < 9:
        if denominateur_tour%2 == 0:
            joueur = "X"
        else:
            joueur = "O"
        input_player(joueur)
        victory = verify_victory()
        denominateur_tour +=1
    if denominateur_tour >= 9:
        print('Match nul.')
    else:
        print("Game over.", joueur,"a gagne.")

#---VARIABLES
list_cases = list(range(1,10))

print_grille()
play()