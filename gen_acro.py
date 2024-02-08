#Demander aux users une phrase
texte = str(input("Renseigner une chaine de caractère "))

#Fonction pour mettre en place un acronyme en majuscule
def accro_gen(chaine):
    mots = chaine.split()
    accro = ''
    for i in mots:
        accro = accro + str(i[0]).upper()
    return accro

#Appel de la fonction sur l'input de l'utilisateur
r=accro_gen(texte)

print("Voici l'acronyme : ",r)