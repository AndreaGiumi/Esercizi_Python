class Book:
    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool)-> None :
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self) -> bool | str:
        if not self.is_borrowed:
            self.is_borrowed =  True
        else:
            return "Il libro è già stato preso in prestito"
        return self.is_borrowed

    def return_book(self) -> bool | str:
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            return "Il libro è già stato riconsegnato"
        return self.is_borrowed
    

        