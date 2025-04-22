import random
import string

from mots import mots

def choisirVotreMots(mots):
    mot = random.choice(mots)
    return mot

def hangman():
    mot_original = choisirVotreMots(mots)
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
    else:
        print("Le mot à deviner est", mot, "vous avez gagné ☺️")



hangman()