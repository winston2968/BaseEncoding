# -*- coding:utf-8 -*-
# //////////////////////////////////////////////////////////////////////////////////////////////////
#                       Chiffrement par base - Formatage Texte
# //////////////////////////////////////////////////////////////////////////////////////////////////


"""
Avant d'axécuter le programme,
veuillez entrez votre texte de chiffrement à la place du triple
saut de ligne ci-dessous entre les guillemets
"""

text = """



"""

path = input('Entrez le chemin de votre fichier texte...')

def replace(text):
    text = text.replace('é', 'e')
    text = text.replace('è', 'e')
    text = text.replace('ê', 'e')
    text = text.replace('à', 'a')
    text = text.replace('ç', 'c')
    text = text.lower()
    return text

def write(text, path):
    base = open(path, 'w')
    base.write(text)
    base.close()

text = replace(text)
write(text, path)

print()
print('Texte copié dans votre ficher !')
