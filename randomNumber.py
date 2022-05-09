#jeu c'est plus c'est moins
#Importation de la classe random

import random

#définitions des variables
aléa = 0
X = 0
Min = 0
compteur = 0
Max = 100
reponse = True
ReponseInput = ""
grammaire = 0
EtatJeu = True

print("bienvenue")
#boucle etat de jeu, gestionnaire de jeu
while EtatJeu:

    #reinitialisation des variables pour la nouvelle partie
    compteur = 0
    grammaire = ""
    X = 0
    aléa = random.randint(Min,Max)

    print("c'est parti")
    #boucle si l'utilisateur n'a pas la bonne réponse
    while X!= aléa:
    #Incrémentations du compteur de tentatives.
        compteur += 1
        #saisie utilisateur
        print("Le but est de trouver un chiffre aléatoire en moins de 10 coups. ")
        X=int(input(" Entrez un chiffre : "))
        #c'est plus
        if (X < aléa):
            print("C'est plus")
        #c'est moins
        elif (X > aléa):
            print("C'est moins")
        #sinon c'est le bon , avec le nombre de tentatives
        else:
            print("bingo"+  " en " + str(compteur) + " tentatives" )
            break

        #boucle pour la reponse du recommancer
    while reponse:
        ReponseInput = input("On recommance ? :")
        #recupération de la réponse "o" ou "n"
        if (ReponseInput == "o"):
            #affectation des bool pour la réponse positive est recommance la boucle
            reponse = False
            EtatJeu = True
            #affectation des bool pour la reponse négative on casse la boucle
        elif (ReponseInput == "n"):
            reponse = False
            EtatJeu = False
        else:
            continue
print ("à la prochaine")