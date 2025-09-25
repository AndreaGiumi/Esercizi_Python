class Student:
    def __init__(self, name:str, studyProgram:str, age:int, gender:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(f"{self.name}, {self.studyProgram}, {self.age}, {self.gender}")

andrea = Student("Andrea", "ItsAcademy", 27, "Maschio")
mirko = Student("Mirko", "TCR", 27, "Maschio")
alessio = Student("Alessio", "OSS", 30, "MAschio")


andrea.printInfo()
mirko.printInfo()
alessio.printInfo()