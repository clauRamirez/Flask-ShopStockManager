from db.run_sql import run_sql
from models.book import Book
from repositories import author_repository, publisher_repository
from typing import List, Any


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
    book.id = results[0]['id']


def select(id: int) -> Book:
    results = run_sql(
        sql="SELECT * FROM books WHERE id = %s;",
        values=[id]
    )
    if results[0] is not None:
        res = results[0]
        return Book(
            isbn=res['isbn'],
            title=res['title'],
            genre=res['genre'],
            author=author_repository.select(res['author_id']),
            illustrator=author_repository.select(res['illustrator_id']),
            publisher=publisher_repository.select(res['publisher_id']),
            edition=res['edition'],
            cost=res['cost'],
            price=res['price'],
            stock=res['stock'],
            id=res['id']
        )


def delete(id: int) -> None:
    run_sql(
        sql="DELETE FROM books WHERE id = %s;",
        values=[id]
    )


def update(book: Book) -> None:
    run_sql(
        sql="\
            UPDATE books SET(isbn, title, genre, author_id, illustrator_id, publisher_id, edition, cost, price, stock) \
            = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) \
            WHERE id = %s;",
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
            book.stock,
            book.id
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
            sql="SELECT * FROM books ORDER BY title;"
        )
    ]


def filter(filter: str, search_param: Any) -> List[Book]:
    '''@filter: 'author', 'publisher' OR 'genre'
    @search_param: INT or String if @filter == 'genre'
    
    @return List of Book objects filtered by @filter
    '''
    
    try:
        if filter == 'genre':
            sql = f"\
                SELECT * FROM books WHERE {filter}=%s ORDER BY title"
            search_param = search_param.capitalize()
        else:
            sql = f"\
                SELECT * FROM books WHERE {filter}_id=%s ORDER BY title"
    except ValueError('Wrong filter argument') as error:
        print(error)
    finally:
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
                sql=sql,
                values=[search_param]
            )
        ]


def get_genres() -> List[str]:
    lst = []

    for row in select_all():
        lst.append(row.genre)

    return sorted(list(set(lst)))
