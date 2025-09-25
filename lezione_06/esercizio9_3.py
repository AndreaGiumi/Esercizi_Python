class User:
    def __init__(self,frist_name:str,last_name:str,age:int,email:str,):
        self.frist_name = frist_name
        self.last_name = last_name
        self.age = age
        self.email = email  


    def describe_user(self):
        print(f"Nome: {self.frist_name}\nCognome: {self.last_name}\nEtà: {self.age}\nEmail: {self.email}")


    def greet_user(self):
        print(f"Ciao {self.frist_name} un abbraccio!")


andri09 = User("Andrea","Giumi", 27, "andreagiumi97@gmail.com")
fabix98 = User("Fabio", "Rossi", 15, "fabiorossi98@hotmail.com")
lauretta23 = User("Laura", "Bianchi", 23, "laurabianchi23@gmail.com")

andri09.describe_user()
print("------------------------------------------------------")
fabix98.describe_user()
print("------------------------------------------------------")
lauretta23.describe_user()
print("-------------------------------------------------")
andri09.greet_user()
fabix98.greet_user()
lauretta23.greet_user()