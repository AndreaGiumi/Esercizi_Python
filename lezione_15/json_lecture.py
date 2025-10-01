import json
PATH: str = "config.json"
mode: str = "r"
encoding: str = "utf-8"


with open(PATH, mode=mode, encoding=encoding) as file:

    config: dict = json.load(file)


    print(config)


# PATH: str = "info_json.json"
# with open(PATH, mode="r", encoding=encoding) as file:
#     config: dict = json.load(file)
#     print(config)


# with open(PATH, mode="w") as file:
#     # dump salva un dizionario come un file json
#     json.dump(config,file,indent=4)


