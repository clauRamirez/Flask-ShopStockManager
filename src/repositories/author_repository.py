from db.run_sql import run_sql
from models.author import Author
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