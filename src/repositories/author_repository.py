from db.run_sql import run_sql
from models.author import Author
from models.book import Book
from repositories import publisher_repository
from typing import List


def save(author: Author) -> None:
    results = run_sql(
        sql="\
            INSERT INTO authors(name) \
            VALUES (%s) RETURNING *;",
        values=[author.name]
    )
    author.id = results[0]['id']


def select(id: int) -> Author:
    results = run_sql(
        sql="SELECT * FROM authors WHERE id = %s;",
        values=[id]
    )
    if results[0] is not None:
        return Author(
            name=results[0]['name'],
            id=id
        )


def delete(id: int) -> None:
    run_sql(
        sql="DELETE FROM authors WHERE id = %s;",
        values=[id]
    )


def update(author: Author) -> None:
    run_sql(
        # ROW('value') METHOD IS REQUESTED BY POSTGRESQL IN THIS CASE IN PARTICULAR
        # REMOVING IT WILL LEAD TO ERRORS WHILE RUNNING THIS FUNCTION
        sql="\
            UPDATE authors SET(name) = ROW(%s) \
            WHERE id = %s;",
        values=[
            author.name,
            author.id
        ]
    )


def delete_all() -> None:
    run_sql(
        sql="DELETE FROM authors;"
    )


def select_all() -> List[Author]:
    return [
        Author(
            name=row['name'],
            id=row['id']
        ) for row in run_sql(
            sql="SELECT * FROM authors ORDER BY name;"
        )
    ]


def get_books_by_author(author: Author) -> List[Author]:
    return [
        Book(
            isbn=row['isbn'],
            title=row['title'],
            genre=row['genre'],
            author=select(row['author_id']),
            illustrator=select(row['illustrator_id']),
            publisher=publisher_repository.select(row['publisher_id']),
            edition=row['edition'],
            cost=row['cost'],
            price=row['price'],
            stock=row['stock'],
            id=row['id']
        ) for row in run_sql(
            sql="SELECT * FROM books WHERE author_id=%s ORDER BY title",
            values=[author.id]
        )
    ]


def get_books_by_illustrator(illustrator: Author) -> List[Author]:
    return [
        Book(
            isbn=row['isbn'],
            title=row['title'],
            genre=row['genre'],
            author=select(row['author_id']),
            illustrator=select(row['illustrator_id']),
            publisher=publisher_repository.select(row['publisher_id']),
            edition=row['edition'],
            cost=row['cost'],
            price=row['price'],
            stock=row['stock'],
            id=row['id']
        ) for row in run_sql(
            sql="SELECT * FROM books WHERE illustrator_id=%s ORDER BY title",
            values=[illustrator.id]
        )
    ]