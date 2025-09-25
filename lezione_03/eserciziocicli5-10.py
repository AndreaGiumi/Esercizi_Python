current_users: list[str] = ["Fabio", "Mirko", "Giovanni", "Andrea", "Rosa"]
current_users: list[str] = ["Fabio".lower(), "Mirko".lower(), "Giovanni".lower(), "Andrea".lower(), "Rosa".lower()]
new_users: list[str] = ["Mirko", "Andrea", "Franco", "Simone", "Simona"]

for user in new_users:
     if user in current_users:
          print("The person will need to enter a new username.")
     else:
          print("The username is available.")