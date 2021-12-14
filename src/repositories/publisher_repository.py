from db.run_sql import run_sql
from models.publisher import Publisher
from models.book import Book
from repositories import author_repository
from typing import List


def save(publisher: Publisher) -> None:
    results = run_sql(
        sql="\
            INSERT INTO publishers(name, website, salesperson, contact) \
            VALUES (%s, %s, %s, %s) RETURNING *;",
        values=[
            publisher.name,
            publisher.website,
            publisher.salesperson,
            publisher.contact
        ]
    )
    publisher.id = results[0]['id']


def select(id: int) -> Publisher:
    results = run_sql(
        sql="SELECT * FROM publishers WHERE id = %s;",
        values=[id]
    )
    if results[0] is not None:
        res = results[0]
        return Publisher(
            name=res['name'],
            website=res['website'],
            salesperson=res['salesperson'],
            contact=res['contact'],
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
        sql="DELETE FROM publishers;"
    )


def select_all() -> List[Publisher]:
    return [
        Publisher(
            name=row['name'],
            website=row['website'],
            salesperson=row['salesperson'],
            contact=row['contact'],
            id=row['id']
        ) for row in run_sql(
            sql="SELECT * FROM publishers ORDER BY name;"
        )
    ]


def get_books_by_publisher(publisher: Publisher):
    return [
        Book(
            isbn=row['isbn'],
            title=row['title'],
            genre=row['genre'],
            author=author_repository.select(row['author_id']),
            illustrator=author_repository.select(row['illustrator_id']),
            publisher=select(row['publisher_id']),
            edition=row['edition'],
            cost=row['cost'],
            price=row['price'],
            stock=row['stock'],
            id=row['id']
        ) for row in run_sql(
            sql="SELECT * FROM books WHERE publisher_id=%s ORDER BY title",
            values=[publisher.id]
        )
    ]