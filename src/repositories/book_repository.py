from db.run_sql import run_sql
from models.author import Author
from models.book import Book
from models.publisher import Publisher
from repositories import author_repository, publisher_repository
from typing import List


def save(book: Book) -> None:
    results = run_sql(
        sql="\
            INSERT INTO books(isbn, title, genre, author_id, illustrator_id, publisher_id, edition, cost, price, stock) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;",
        values=[
            book.isbn,
            book.title,
            book.genre,
            book.author.id,
            book.illustrator.id,
            book.publisher.id,
            book.edition,
            book.cost,
            book.price,
            book.stock
        ]
    )
    print(results)
    book.id = results[0]['id']


def select(id: int) -> Book:
    results = run_sql(
        sql="SELECT * FROM books WHERE id = %s;",
        values=[id]
    )
    if results[0] is not None:
        return Book(
            isbn=results[0]['isbn'],
            title=results[0]['title'],
            genre=results[0]['genre'],
            author=author_repository.select(results[0]['author_id']),
            illustrator=author_repository.select(results[0]['illustrator_id']),
            publisher=publisher_repository.select(results[0]['publisher_id']),
            edition=results[0]['edition'],
            cost=results[0]['cost'],
            price=results[0]['price'],
            stock=results[0]['stock'],
            id=results[0]['id']
        )


def delete(id: int) -> None:
    run_sql(
        sql="DELETE FROM books WHERE id = %s;",
        values=[id]
    )


def update(book: Book) -> None:
    run_sql(
        sql="\
            UPDATE books SET(isbn, title, genre, author_id, illustrator_id, publisher_id, edition, cost, price, stock) \
            = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) \
            WHERE id = %s;",
        values=[
            book.isbn,
            book.title,
            book.genre,
            book.author.id,
            book.illustrator.id,
            book.publisher.id,
            book.edition,
            book.cost,
            book.price,
            book.stock,
            book.id
        ]
    )


def delete_all() -> None:
    run_sql(
        sql="DELETE FROM books;"
    )


def select_all() -> List[Book]:
    return [
        Book(
            isbn=row['isbn'],
            title=row['title'],
            genre=row['genre'],
            author=author_repository.select(row['author_id']),
            illustrator=author_repository.select(row['illustrator_id']),
            publisher=publisher_repository.select(row['publisher_id']),
            edition=row['edition'],
            cost=row['cost'],
            price=row['price'],
            stock=row['stock'],
            id=row['id']
        ) for row in run_sql(
            sql="SELECT * FROM books;"
        )
    ]