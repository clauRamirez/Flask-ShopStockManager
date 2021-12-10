import unittest
from src.models.book import Book
from src.models.author import Author
from src.models.publisher import Publisher

class TestBook(unittest.TestCase):
    def setUp(self):
        self.author = Author(
            name='John Test',
        )
        self.publisher = Publisher(
            name='Test Editions',
            website='www.examp.le',
        )
        self.book = Book(
            ISBN=111222333,
            title='Some Book',
            genre='Horror',
            author=self.author,
            illustrator=self.author,
            publisher=self.publisher,
            edition=2,
            cost=2.25,
            price=17.75,
            stock=5
        )
        
    def test_get_mark_up(self):
        self.assertEqual(15.50, self.book.get_mark_up())