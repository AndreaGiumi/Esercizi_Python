class User:
    def __init__(self, first_name:str, last_name:str, username:str, email:str):
        self.frist_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email


    def describe_user(self):
        print(f"Nome: {self.frist_name}\nCognome: {self.last_name}\nUsername: {self.username}\nEmail: {self.email}")

    def greet_user(self):
        print(f"Benvenuto {self.frist_name}!")

class Privileges:
    def __init__(self):
        pass


    def show_privileges(self, list_privileges:list[str]):
        print(f"{list_privileges}")


class Admin:
    def __init__(self,user, privileges):
        self.user = user
        self.privileges = privileges