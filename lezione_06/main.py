from users import User
from users import Privileges
from users import Admin

u1: User = User("Andrea", "Giumi", "Andri97", "andreagiumi97@gmail.com")
p1: Privileges = Privileges(["Add post", "Remuve post"])


a1: Admin = Admin(u1, p1)

