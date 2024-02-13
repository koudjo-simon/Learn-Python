from itertools import product
import time

start_time = time.time();
chaine = ""

for i in range(33, 123):
    chaine = chaine + chr(i)

length = int(input("Entrer the max length of the chaine: "))
word_list = []

for i in range(length+1):
    for item in product(chaine, repeat=i):
        chain = "".join(item)
        word_list.append(chain)
        print(chain)

end_time = time.time()
print(f"Temps d'exécution : {end_time - start_time} secondes")