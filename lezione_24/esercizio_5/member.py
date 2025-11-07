from book import Book
class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_list: list[Book] = []

    def borrow_book(self, book: Book) -> None:
        if not book.is_borrowed:
            self.borrowed_list.append(book)
            book.borrow()
        print(f"Il libro {book} è stato preso in prestito")
    
    def return_book(self, book: Book) -> None:
        if book.is_borrowed:
            self.borrowed_list.remove(book)
            book.return_book()
        print(f"Il libro {book} è stato restituito")
    

        

