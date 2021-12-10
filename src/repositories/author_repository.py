from src.db.run_sql import run_sql as query
from src.models.author import Author


def delete_all() -> None:
    query(
        sql="DELETE FROM authors"
    )


def select_all() -> list(Author):
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
            INSERT INTO publishers(name) \
            VALUES (%s) RETURNING *;",
        values=[author.name]
    )
    
    author.id = results[0]['id']