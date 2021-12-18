from models.author import Author
from models.publisher import Publisher

class Book:
    def __init__(
        self,
        isbn: str,
        title: str,
        genre: str,
        author: Author,
        illustrator: Author,
        publisher: Publisher,
        edition: int,
        cost: float,
        price: float,
        stock: int,
        id = None
    ):

        self.isbn = isbn
        self.title = title
        self.genre = genre
        self.author = author
        self.illustrator = illustrator
        self.publisher = publisher
        self.edition = edition
        self.cost = cost
        self.price = price
        self.stock = stock
        self.id = id
    
    def __repr__(self) -> str:
        return f"Book: {{ \
            id: {self.id}, isbn: {self.isbn}, title: {self.title}, genre: {self.genre}, \
            author: {self.author}, illustrator: {self.illustrator}, publisher: {self.publisher}, \
            edition: {self.edition}, cost: {self.cost}, price: {self.price}, stock: {self.stock} \
        }}"
    
    def get_mark_up(self) -> float:
        return round(self.price - self.cost, 2)
    