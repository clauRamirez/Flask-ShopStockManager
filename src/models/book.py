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
        
    def get_mark_up(self) -> float:
        return round(self.price - self.cost, 2)
    