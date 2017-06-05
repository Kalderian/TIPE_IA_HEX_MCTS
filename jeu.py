# -*- coding: utf-8 -*-
import pygame
from IA import *
from plateau import *
from classeArbre import *

plateau = Plateau(9, [], (-1,-1))
joueur = 1
pasDeGagnant = True
arbreGeneral = initialisation(plateau, 1)
arbreCoups = arbreGeneral
cheminGeneral = []

# while(pasDeGagnant):
#     marchePas = True
#     while(marchePas):
#         if joueur == 1:
#             x = int(input("Xjoueur1 = "))
#             y = int(input("Yjoueur1 = "))
#         elif joueur == 2:
#             x = int(input("Xjoueur2 = "))
#             y = int(input("Yjoueur2 = "))
#         marchePas = not(plateau.joue(joueur, (x, y)))
#     pasDeGagnant = not(plateau.checkVictoire(joueur))
#     if(pasDeGagnant):
#         joueur = 3 - joueur
#     plateau.affiche(1)

'''On laisse pour l'instant l'IA jouer en premier. Elle execute l'algorithme MCTS et joue le coup dans la racine de l'arbre renvoyé. 
On insere ensuite le plateau à la place de cette racine, pour de futures simulations'''
while(pasDeGagnant):
    caseOccupee = True
    while(caseOccupee):
        if joueur == 1:
            arbreCoups = mcts(arbreGeneral, cheminGeneral, arbreCoups, plateau, 1)
            x = arbreCoups.racine[0][0]
            y = arbreCoups.racine[0][1]
        elif joueur == 2:
            x = int(input("Xjoueur2 = "))
            y = int(input("Yjoueur2 = "))
        caseOccupee = not(plateau.joue(joueur, (x, y)))
    pasDeGagnant = not(plateau.checkVictoire(joueur))
    if joueur == 2: #On actualise l'arbre de recherche de l'IA avec le coup de l'adversaire
        arbreCoups = rechercheCoup(arbreCoups, plateau, cheminGeneral, 1)
    if(pasDeGagnant):
        joueur = 3 - joueur
    plateau.affiche2()

pygame.quit()  
print("joueur n°" + str(joueur) + " gagne")