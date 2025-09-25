PATH: str = "lezione_15/example.txt"
mode: str = "w"
encoding: str = "utf-8"

file = open(PATH, mode=mode, encoding=encoding)

print(file)

# output: str = file.read()

# print(output)


output: str = file.write("Ciao")
print(output)