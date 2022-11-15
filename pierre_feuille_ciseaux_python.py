#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      llafin
#
# Created:     14/11/2022
# Copyright:   (c) llafin 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from math import*
import random

# On exécute une fonction pierre_feuille_ciseaux
def pierre_feuille_ciseaux():
    # On défint victoire_ordinateur=0
    victoire_ordinateur=0
     # On défint victoire_ordinateur=0
    victoire_joueur=0
    # on execute la fonction input pour demander au joueur combien de victoire il faut pour gagner et on stocke ce int dans la variable nb_victoire
    nb_victoire=int(input("choisissez le nombre de victoire pour gagner"))
    #tant que victoire_joueur est différent de nb_victoire et victoire_ordinateur est différent de nb_victoire
    while victoire_joueur!=nb_victoire and victoire_ordinateur!=nb_victoire:
        # on execute la fonction input pour demander au joueur si il joue pierre, feuille ou ciseaux et on stocke ce résultat dans la variable choix
        choix=input("Choisissez pierre, feuille ou ciseaux")
        #tant que choix est différent de pierre feuille et ciseaux
        while choix !="pierre" and choix !="feuille" and choix !="ciseaux"  :
            #on redemande au joueur de saisir son choix
            choix=input("Mauvaise saisit, réessayer")
        # si choix est égale à pierre
        if choix=="pierre":
            # alors si random est égale à 0
            if random.randint(0,2)== 0:
                # afficher : l'ordinateur à aussi fait pierre, vous êtes à égalité
                print("l'ordinateur à aussi fait pierre, vous êtes à égalité")
            # alors sinon si random est égale à 1
            elif random.randint(0,2)== 1:
                # afficher : l'ordinateur à fait feuille, vous avez perdu
                print("l'ordinateur à fait feuille, vous avez perdu")
                #ajouter 1 à victoire_ordinateur
                victoire_ordinateur=victoire_ordinateur+1
            # alors sinon
            else:
                print("l'ordinateur à fait ciseaux, vous avez gagnez")
                # afficher : l'ordinateur à fait ciseaux, vous avez gagnez
                victoire_joueur=victoire_joueur+1
                #ajouter 1 à victoire_joueur
        # si choix est égale à feuille
        if choix=="feuille":
            # alors si random est égale à 0
            if random.randint(0,2)== 0:
                # afficher : l'ordinateur à fait pierre, vous avez gagnez
                print("l'ordinateur à fait pierre, vous avez gagnez")
                #ajouter 1 à victoire_joueur
                victoire_joueur=victoire_joueur+1
            # alors sinon si random est égale à 1
            elif random.randint(0,2)== 1:
                # afficher : l'ordinateur à fait feuille, vous êtes à égalité
                print("l'ordinateur à aussi fait feuille, vous êtes à égalité")
            # alors sinon
            else:
                # afficher : l'ordinateur à fait ciseaux, vous avez perdu
                print("l'ordinateur à fait ciseaux, vous avez perdu")
                #ajouter 1 à victoire_ordinateur
                victoire_ordinateur=victoire_ordinateur+1
        #si choix est égale à ciseaux
        if choix=="ciseaux":
            # alors si random est égale à 0
            if random.randint(0,2)== 0:
                # afficher : l'ordinateur à fait pierre, vous avez perdu
                print("l'ordinateur à fait pierre, vous avez perdu")
                #ajouter 1 à victoire_ordinateur
                victoire_ordinateur=victoire_ordinateur+1
            # alors sinon si random est égale à 1
            elif random.randint(0,2)== 1:
                # afficher : l'ordinateur à fait feuille, vous avez gagnez
                print("l'ordinateur à fait feuille, vous avez gagnez")
                #ajouter 1 à victoire_joueur
                victoire_joueur=victoire_joueur+1
            #alors sinon
            else:
                # afficher : l'ordinateur à fait ciseaux, vous êtes à égalité
                print("l'ordinateur à aussi fait ciseaux, vous êtes à égalité")
    #si victoire_joueur est égale à nb_victoire
    if victoire_joueur==nb_victoire:
        # alors afficher vous avez gagnez et le score
        print("Vous avez gagnez",victoire_joueur,victoire_ordinateur)
    #sinon
    else:
        # alors afficher vous avez perdu et le score
        print("Vous avez perdu",victoire_ordinateur,victoire_joueur)
# on exécute le fonction pierre_feuille_ciseaux
pierre_feuille_ciseaux()



