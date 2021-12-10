from db.run_sql import run_sql
from models.author import Author
from typing import List


def delete_all() -> None:
    run_sql(
        sql="DELETE FROM authors"
    )


def select_all() -> List[Author]:
    return [
        Author(
            name=row['name'],
            id=row['id']
        ) for row in run_sql(
            sql="SELECT * FROM authors"
        )
    ]


def save(author: Author) -> None:
    results = run_sql(
        sql="\
            INSERT INTO authors(name) \
            VALUES (%s) RETURNING *;",
        values=[author.name]
    )
    
    author.id = results[0]['id']