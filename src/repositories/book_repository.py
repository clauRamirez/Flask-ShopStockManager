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


def select(id: int) -> Publisher:
    results = run_sql(
        sql="SELECT * FROM publishers WHERE id = %s;",
        values=[id]
    )
    if results[0] is not None:
        return Publisher(
            name=results[0]['name'],
            website=results[0]['website'],
            salesperson=results[0]['salesperson'],
            contact=results[0]['contact'],
            id=id
        )


def delete(id: int) -> None:
    run_sql(
        sql="DELETE FROM publishers WHERE id = %s;",
        values=[id]
    )


def update(publisher: Publisher) -> None:
    run_sql(
        sql="\
            UPDATE publishers SET(name, website, salesperson, contact) = (%s, %s, %s, %s) \
            WHERE id = %s;",
        values=[
            publisher.name,
            publisher.website,
            publisher.salesperson,
            publisher.contact,
            publisher.id
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