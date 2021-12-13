from db.run_sql import run_sql
from models.publisher import Publisher
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
