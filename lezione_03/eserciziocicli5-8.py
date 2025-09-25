users: list[str] = ["Luca", "Alessio", "Francesco", "Jaden", "Admin"]

for name in users:
    if name == "Admin":
        print(f"Hello {name}, would you like to see a status reporto")
    else:
        print(f"Hello {name}, thank you for logging in again.")