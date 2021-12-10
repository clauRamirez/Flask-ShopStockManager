from db.run_sql import run_sql
from models.publisher import Publisher
from typing import List

def delete_all() -> None:
    run_sql(
        sql="DELETE FROM publishers"
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
            sql="SELECT * FROM publishers"
        )
    ]


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