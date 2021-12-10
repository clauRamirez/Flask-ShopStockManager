from src.db.run_sql import run_sql as query
from src.models.publisher import Publisher


def delete_all() -> None:
    query(
        sql="DELETE FROM authors"
    )


def select_all() -> list(Publisher):
    return [
        Publisher(
            name=row['name'],
            website=row['website'],
            salesperson=row['salesperson'],
            contact=row['contact'],
            id=row['id']
        ) for row in query(
            sql="SELECT * FROM authors"
        )
    ]


def save(publisher: Publisher) -> None:
    results = query(
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