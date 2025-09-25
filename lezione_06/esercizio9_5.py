class User:
    def __init__(self,frist_name:str,last_name:str,age:int,email:str):
        self.frist_name = frist_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    
    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts
    


    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts



print(f"Numero prove accesso: 0")

andri:User = User("Andrea", "Giumi", 27, "andreagiumi97@gmail.com")

print(andri.increment_login_attempts())
print(andri.increment_login_attempts())
print(andri.increment_login_attempts())
print(andri.increment_login_attempts())
print(andri.increment_login_attempts())
print(andri.increment_login_attempts())
print(andri.reset_login_attempts())
print(andri.increment_login_attempts())











