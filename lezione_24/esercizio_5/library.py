from book import Book
from member import Member
class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
    
    def add_book(self, book_id: str, title: str, author: str) -> dict | str:
        if book_id in self.books:
            return "Il libro è già presente"
        book = Book(title, author)

        self.books[book_id] = book

        return self.books[book_id]
    
    def register_member(self, member_id:str, name: str) -> dict | str:
        if member_id in self.members:
            return "Il membro è già presente"
        member = Member(name)

        self.members[member_id] = member

        return self.members[member_id]
    
    def borrow_book(self, member_id: str, book_id: str) -> dict | str:
        if member_id not in self.members or book_id  not in self.books:
            return "Il membro o il libro non sono presenti"
        