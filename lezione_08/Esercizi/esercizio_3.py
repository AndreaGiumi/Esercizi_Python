class Book:
    _title: str
    _author: str
    _isbn: str
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.set_title(title)
        self.set_author(author)
        self.set_isbn(isbn)
        
    def set_title(self, title: str) -> None:
        self._title = title

    def set_author(self, author: str) ->None:
        self._author = author

    def set_isbn(self, isbn: str) -> None:
        self._isbn = isbn


    def title(self) -> str:
        return self._title
    
    def author(self) ->str:
        return self._author
    
    def isbn(self) ->str:
        return self._isbn
    

    def __str__(self):
        return f"Title: {self.set_title()}  Author: {self.set_author()}  ISBN: {self.set_isbn()}"
        
        
