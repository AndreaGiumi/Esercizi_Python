def  School_Grading_System(student_name:str, score: dict[str, int]) -> None:
    media = sum(score.values()) / len(score)
       
    if media >= 60:
        status: str = "Passed"
    else:
        status: str = "Failed"

    print(f"Studente: {student_name}, Media: {media:.2f}, Stato: {status}")




studenti: list[tuple[str, dict[str, int]]] = [
    ("Alice", {"Math": 75, "Science": 80, "English": 70}),   
    ("Bob", {"Math": 50, "Science": 45, "English": 55}),       
    ("Charlie", {"Math": 90, "Science": 95, "English": 85}),
]



for stud, score in studenti:
    School_Grading_System(stud,score)