import platform

def info_di_sistema():
    print("Il Sistema attualmente in uso è: " + platform.system())
    print("Info Release: " + platform.release())
    print("Il processore in uso è " + platform.processor())


info_di_sistema()