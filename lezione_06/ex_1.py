class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.age)


if alice.age > bob.age:
    print(f"{alice.name} è la più vecchia.")
else:
    print(f"{bob.name} è il più vecchio")


luca = Person("luca", 25)
giovanni = Person("giovanni", 14)
mirko = Person("mirko", 28)
person_list: list = [bob, alice, luca, mirko ]



person = person_list[0]
for i in person_list[1:]:
    if i.age < person.age:
        person = i

print(f"{person.name} è il più giovane.")