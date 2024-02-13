dictio = {
    "nom":"John",
    "username": "John",
    "pwd": "1234",
    "conn":32,
    (1, 2):"Koffi"
}

listes = [
    {"nom": "John", "username": "John", "password": "1234"},
    {"nom": "Koffi", "username": "Koffi", "password": "1234"},
    {"nom": "Ama", "username": "Ama", "password": "1234"}
]

for i in range(len(listes)):
    print(listes[i].get("username", 0))

user = input("Enter your username: ")
password = input("Enter your password: ")

for i in range(len(listes)):
    if listes[i].get("username", 0) == user:
        pwd = listes[i].get("password")
        if pwd == password:
            print("Connection success")
            break
        else:
            print("wrong password")
            break
    else:
        if i == len(listes) - 1:
            print("wrong username")
        else:
            continue

