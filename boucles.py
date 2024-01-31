# som = 0
# for i in range(10):
#     print("Le i actuel est:", i)
#     som = som + i
#
# print("La somme des indices est: ", som)

for i in range(3, 20):
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
