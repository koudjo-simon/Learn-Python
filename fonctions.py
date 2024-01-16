########################## Fonctions #########################
def dire_bonjour():
    print("Bonjour")


def dire_bonjour2(nom):
    print(f"Bonjour {nom}")


def dire_bonjour3(nom, prenom="Afi"):
    return f"{nom} {prenom}"


print(dire_bonjour3("Koffi", prenom="Koudjo"))
