from src.db.run_sql import run_sql as query
from src.models.author import Author
from typing import List


def delete_all() -> None:
    query(
        sql="DELETE FROM authors"
    )


def select_all() -> List[Author]:
    return [
        Author(
            name=row['name'],
            id=row['id']
        ) for row in query(
            sql="SELECT * FROM authors"
        )
    ]


def save(author: Author) -> None:
    results = query(
        sql="\
            INSERT INTO authors(name) \
            VALUES (%s) RETURNING *;",
        values=[author.name]
    )
    
    author.id = results[0]['id']