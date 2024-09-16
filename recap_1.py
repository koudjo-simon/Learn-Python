contacts = []

def enregistrerContact():
    compteur = 1
    while compteur < 4:
        print("*" * 20, " Contact ", compteur, "*" * 20, sep="")
        nom = input("Entrer le nom: ")
        prenom = input("Entrer le prenom: ")
        numero = input("Entrer le numero: ")
        dictio = {"nom": nom, "prenom": prenom, "numero": numero}
        contacts.append(dictio)
        compteur += 1


def afficherContacts():
    for contact in contacts:
        print(contact)


def rechercherContact():
    nom = input("Entrer le nom du contact à rechercher: ")
    for contact in contacts:
        if contact["nom"] == nom:
            print("Contact trouvé:", contact)
            return
    print("Contact non trouvé !")


def miseAjour():
    nom = input("Entrer le nom du contact à mettre à jour: ")
    for contact in contacts:
        if contact["nom"] == nom:
            print("Contact trouvé:", contact)
            print("******* Modifcation du contact *******")
            contact["nom"] = input("Entrer le nouveau nom du contact: ")
            contact["prenom"] = input("Entrer le nouveau prenom du contact: ")
            contact["numero"] = input("Entrer le nouveau numero du contact: ")
            print("Contact mis à jour avec succès !!! ===>", contact)
            return
    print("Contact non trouvé !")


def suppressionContact():
    nom = input("Entrer le nom du contact à supprimer: ")
    for contact in contacts:
        if contact["nom"] == nom:
            print("Suppression en cours ...")
            contacts.remove(contact)
            print("Supprimer avec success !")
            return
    print("Contact non trouvé !")


enregistrerContact()
afficherContacts()
rechercherContact()
miseAjour()
suppressionContact()

print(contacts)

