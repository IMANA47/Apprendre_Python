import random
import string
from mots import mots

#declaration des variable
score = 0
nom_joueur = ""

def choisir_votre_mots(mots):
    mot = random.choice(mots)
    return mot

#la fonction pour donner la possibilite de rejouer
def jouer_de_nouveau():
    jouer_jeu = input("Souhaitez vous continuer à jouer? (O = oui, N = Non)")
    while jouer_jeu not in {"O","o","N","n"}:
        jouer_jeu = input("Souhaitez vous continuer à jouer? (O = oui, N = Non)")
    if jouer_jeu == "O" or jouer_jeu == "o":
        hangman()
    elif jouer_jeu == "N" or jouer_jeu == "n":
        print("Merci d'avoir jouer et bye!")
        exit()

#Fonction pour recuperer le nom du jouer
def recuperer_nom_jouer():
    nom_joueur = input("Merci de saisir votre nom : ")
    nom_joueur = nom_joueur.capitalize() # Pour mettre la premier lettre en majuscule
    if not nom_joueur.isalpha() or len(nom_joueur) < 5: #Pour verifier si le user a mis des lettre et la taille est < 5
         print("Le nom que vous avez saisi est invalide")
         return  recuperer_nom_jouer()
    else:
        return nom_joueur


def hangman():
    global nom_joueur

    if nom_joueur == "":
        nom_joueur = recuperer_nom_jouer()

    global score
    mot_original = choisir_votre_mots(mots)
    #mettre les mots majuscule
    mot = mot_original.upper()
    #stocker les mots dans un ensemble
    mot_lettre = set(mot)

    #Pour regrouper tout les lettre en majuscule
    alphabet = set(string.ascii_uppercase)
    lettre_jouees = set()
    essai = 6

    while len(mot_lettre) > 0 and essai > 0:
        print("Vous avez", essai, "essai(s) et vous avez utilise les lettres suivantes:", ','.join(lettre_jouees))
        mot_list =[lettre if lettre in lettre_jouees else "_" for lettre in mot]
        print("Le mot actuel est :", ' '.join(mot_list))
        lettre_choisie = input("Entrer une lettre : ").upper()

        if lettre_choisie in alphabet - lettre_jouees:
            lettre_jouees.add(lettre_choisie)
            if lettre_choisie in mot_lettre:
                mot_lettre.remove(lettre_choisie)
                essai = 6
            else:
                essai -= 1
                print("il vous reste ", essai, "essai(s) encore")

        elif lettre_choisie in lettre_jouees:
            print("Oups vous avez deja utilise cette lettre , choisissez une lettre!")
        else:
            print("Votre choix est invalide, merci de saisir une lettre!")

    if essai == 0:
        print("🥴 Dommage vous avez perdu, il ne vous reste aucun essai!")
        #appel de la fonction pour essayer a nouveau
        jouer_de_nouveau()
    else:
        print(nom_joueur,"le mot à deviner est", mot, "vous avez gagné ☺️")
        score += 10
        print(nom_joueur,"votre score est de : ", score,"points")
        #appel de la fonction jouer a nouveau pour reasseyer
        jouer_de_nouveau()

hangman()