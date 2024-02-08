def check_number(number):
    if number < 2:
        return False
    else:
        counter = 0
        for i in range(2, number + 1):
            if number % i == 0:
                counter += 1
        if counter > 2:
            return False
        else:
            return True


def check_number_2(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


n = int(input("Entrer un nombre: "))
resultat = check_number(n)
if resultat:
    print(f"Le nombre {n} est premier")
else:
    print(f"Le nombre {n} n'est pas premier")
