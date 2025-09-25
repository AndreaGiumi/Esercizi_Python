age: int = 87


if age < 2:
    print("The person is a baby!")
elif age >= 2 and age < 4:
    print("the person is a toddler!")
elif age >= 4 and age < 13:
    print("the person is a kid!")
elif age >= 13 and age < 20:
    print("the person is a teenager!")
elif age >= 20 and age < 65:
    print("the person is an adult!")
else:
    if age > 65:
        print("that the person is an elder!")