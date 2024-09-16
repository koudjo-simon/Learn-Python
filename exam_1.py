############################# Exercice 1 ##############################
# 1.
def supprimer_accents(chaine):
    accents = {
        'à': 'a', 'â': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'î': 'i', 'ï': 'i',
        'ô': 'o', 'ö': 'o',
        'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c'
    }

    # chaine_sans_accents = ''.join(accents.get(char, char) for char in chaine)
    for i in range(len(chaine)):
        if chaine[i] in accents.keys():
            chaine = chaine[:i] + accents[chaine[i]] + chaine[i+1:]
    return chaine


phrase_accentuee = "C'est une journée ensoleillée à Montévidéo."
phrase_sans_accents = supprimer_accents(phrase_accentuee)

print("Phrase originale :", phrase_accentuee)
print("Phrase sans accents :", phrase_sans_accents)

"""
 2. l'instruction "".join(sorted(s)) 
 crée une nouvelle chaîne de caractères qui est une 
 version triée de la chaîne initiale s.
"""


# 3.
def sont_anagrammes(mot1, mot2):
    mot1 = mot1.lower()
    mot2 = mot2.lower()

    if len(mot1) != len(mot2):
        return False

    mot1_trie = "".join(sorted(mot1))
    mot2_trie = "".join(sorted(mot2))
    print(mot1_trie, mot2_trie)

    return mot1_trie == mot2_trie


mot1 = "listen"
mot2 = "silent"
print(sont_anagrammes(mot1, mot2))

########################## Exercice 2 #########################
inventaire = {
    "ordinateur": (3, 100000),
    "ventilateur": (10, 5000),
    "valise": (6, 10000),
    "projecteur": (2, 20000),
    "cable": (20, 3000)
}

print(inventaire)

inventaire["phone"] = (15, 70000)
print(inventaire)

inventaire["valise"] = (30, inventaire.get("valise", 0)[1])
print(inventaire)

result = 0
for key, value in inventaire.items():
    result += value[0] * value[1]

print("La Valeur total de l'inventaire est", result)

with open("inventaire.txt", "w") as f:
    for key, value in inventaire.items():
        f.write(f"{key},{value[0]},{value[1]}\n")

############################# Exercice 3 #########################
# with open("document.txt", "w", encoding="utf-8") as file:
#     file.write("""Ce document contient plusieurs paragraphes. Chacun d'eux est destiné à illustrer
#     différentes parties de l'analyse. L'objectif est de compter les mots, trouver les mots les
#     plus fréquents, et trier les mots par la longueur.""")

def analyser_document():
    with open("document.txt", "r", encoding="utf-8") as file:
        contenu = file.read()

    mots = contenu.lower().split()

    # Retirer la ponctuation
    mots_propres = []
    for mot in mots:
        mot_propre = ''
        for char in mot:
            if char.isalnum():
                mot_propre += char
        mots_propres.append(mot_propre)

    # Compter le nombre total de mots
    nb_mots = len(mots_propres)

    # Compter la fréquence des mots
    frequence_mots = {}
    for mot in mots_propres:
        frequence_mots[mot] = frequence_mots.get(mot, 0) + 1

    # Trouver les 5 mots les plus fréquents
    mots_frequents = sorted(frequence_mots.items(), key=get_longueur, reverse=True)[:5]

    longueurs_mots = []
    for mot in set(mots_propres):
        longueurs_mots.append((mot, len(mot)))

    longueurs_mots_triees = sorted(longueurs_mots, key=get_longueur, reverse=True)

    # Enregistrer les résultats dans un fichier
    with open("analyse_resultats.txt", "w", encoding="utf-8") as result_file:
        result_file.write(f"Nombre total de mots : {nb_mots}\n\n")

        result_file.write("Les 5 mots les plus fréquents :\n")
        for mot, frequence in mots_frequents:
            result_file.write(f"{mot}: {frequence} fois\n")

        result_file.write("\nListe des mots triés par longueur :\n")
        for mot, longueur in longueurs_mots_triees:
            result_file.write(f"{mot}: {longueur} caractères\n")


# Fonction auxiliaire pour obtenir la longueur d'un mot
def get_longueur(item):
    return item[1]


# Appeler la fonction d'analyse
analyser_document()



