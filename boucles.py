# som = 0
# for i in range(10):
#     print("Le i actuel est:", i)
#     som = som + i
#
# print("La somme des indices est: ", som)
n = int(input("Entrer un nombre: "))
m = int(input("Entrer un nombre: "))
for i in range(n, m):
    print("*" * i)

print("\n################################################\n")
for i in range(20, 0, -1):
    print("*" * i)

print("\n################################################\n")
for i in range(20, 0, -1):
    print(" " * (20 - i), "*" * i, sep="")

print("\n################################################\n")

for i in range(1, 20):
    print(" " * (20 - i), "*" * (2 * i - 1))

print("\n################################################\n")


def quadry_full(L, l):
    for i in range(l):
        for j in range(L):
            print("*", end="")
        print()


quadry_full(20, 10)

print("\n################################################\n")


def quadry_no_full1(L, l):
    for i in range(l):
        for j in range(L):
            if i == 0 or i == l - 1 or j == 0 or j == L - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


quadry_no_full1(20, 10)


print("\n################################################\n")

def imprimer_motif(nombre_lignes):
    pas = 3
    valeur_courante = 1

    for i in range(1, nombre_lignes+1):
        for j in range(1, i+1):
            print(valeur_courante, end=" ")
            if j != i:
                valeur_courante += 2
            else:
                if i > 2:
                    pas += 1
                valeur_courante += pas
        print()


if __name__ == "__main__":
    nombre_lignes = 10
    imprimer_motif(nombre_lignes)



