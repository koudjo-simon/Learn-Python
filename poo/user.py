class User:
    PI = 3.141592653589793

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def afficher(self):
        print("Hello World")


user1 = User("John", "Doe")
user1.first_name = "WWWWW"
print(user1.first_name)