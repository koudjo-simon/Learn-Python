a = "Amma va à l'école"
b = "Koffi va au marché"
print(a+b)
print(a*4)

print("La taille de la chaine a", len(a))
print(a[5])
print(a[1:9:2])
print(a[:])
n = 5
print("Le type de a est: ", type(a))
print("Le type de n est: ", type(n))
print("Conversion du n est str: ", type(str(n)))
if 'va' in a:
    print("La chaine a contient le mon `va`")
print(a.split("'"))
matricule = "esig-99999-+-2021"
print(matricule)
print(matricule.split("-+-"))
print("On a", a.lower().count("a"), "A dans la chaine a")
print(a.replace(" ", "-"))
print(a.find("p"))

chaine = "     Maman est au magché              "
print(chaine)
print(chaine.rstrip())
print(chaine.lstrip())

nom = "Ama"
age = 13
pattern = f"Je m'appel {nom} et j'ai {age} ans"
print(pattern)
pattern_2 = "Je m'appel %s et j'ai %s ans"%(nom, age)
print(pattern_2)
pattern_3 = "Je m'appel {1} et j'ai {0} ans".format(nom, age)
print(pattern_3)


for i in range(27, 123):
    print(chr(i), end=' ')

for i in 'abcdefghijklmnopqrstuvwxyz':
    print(f"Le code ASCII de {i} est: {ord(i)}")

