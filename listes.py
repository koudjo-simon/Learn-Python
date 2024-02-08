liste = []
liste.append("Koffi")
liste.append("Afi")
liste.append(2.4)
liste.append(3)

print(liste)
print(len(liste))
liste.insert(2, "Lomé")
liste.insert(14, "AT")
print(liste)
liste.remove(2.4)
print(liste)
print(liste[1])
liste.insert(1, "ABC")
print(liste)
print(liste[len(liste) - 1])
print(liste[-1])
print(liste[1], liste[2])
print(liste[0:3])
print(liste[-3:-1])
print(liste[:3])
print(liste[2:])
print(liste[1:4:2])
print(liste[1::2])
print(liste[::2])

liste_p = list(range(0, 11))
print(liste_p)
print(liste_p[0::3])

################## Parcours d'un liste ############
for elt in liste:
    print(elt)

for i in range(len(liste)):
    print("L'element à l'indice", i, "est", liste[i])
