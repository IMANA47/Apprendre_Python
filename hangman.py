import random
from liste_mots import mots

def choisirVotreMots(mots):
    mot = random.choice(mots)
    return mot

print(choisirVotreMots(mots))