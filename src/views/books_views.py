from flask import render_template, redirect, request
from flask import Blueprint
from models.book import Book
from repositories import book_repository, author_repository, publisher_repository
from views.utils import get_title

books_blueprint = Blueprint("books", __name__)

_title = get_title(__file__)

@books_blueprint.route("/books", methods=['GET', 'POST'])
def books_index():
    books=book_repository.select_all()

    if request.method == 'GET':
        if request.args:
            key=list(request.args.keys())[0]
            value=request.args.get(key)
            books=book_repository.filter(key, value)
            
        return render_template(
            "/books/index.html",
            books=books,
            publishers=publisher_repository.select_all(),
            authors=author_repository.select_all(),
            genres=book_repository.get_genres(),
            title=_title
        )
    if request.method == 'POST':
        rf = request.form
        
        book_repository.save(
            Book(
                isbn=rf['isbn'],
                title=rf['title'],
                genre=rf['genre'],
                author=author_repository.select(rf['author_id']),
                illustrator=author_repository.select(rf['illustrator_id']),
                publisher=publisher_repository.select(rf['publisher_id']),
                edition=rf['edition'],
                cost=rf['cost'],
                price=rf['price'],
                stock=rf['stock']
            )
        )
        return redirect("/books")        


@books_blueprint.route("/books/new", methods=['GET'])
def books_new():
    authors=author_repository.select_all()
    
    return render_template(
        "/books/new.html",
        authors=authors,
        illustrators=authors,
        publishers=publisher_repository.select_all(),
        title=_title,
    )


@books_blueprint.route("/books/<int:id>", methods=['GET', 'POST'])
def books_id(id):
    if request.method == 'GET':
        book=book_repository.select(id)
        
        return render_template(
            "/books/show.html",
            book=book,
            author_books=author_repository.get_books_by_author(book.author),
            publisher_books=publisher_repository.get_books_by_publisher(book.publisher),
            title=_title,
        )
    if request.method == 'POST':
        rf = request.form

        book_repository.update(
            Book(
                isbn=rf['isbn'],
                title=rf['title'],
                genre=rf['genre'],
                author=author_repository.select(rf['author_id']),
                illustrator=author_repository.select(rf['illustrator_id']),
                publisher=publisher_repository.select(rf['publisher_id']),
                edition=rf['edition'],
                cost=rf['cost'],
                price=rf['price'],
                stock=rf['stock'],
                id=id
            )
        )
        return redirect("/books")


@books_blueprint.route("/books/<int:id>/edit", methods=['GET'])
def books_edit(id):
    authors = author_repository.select_all()
    
    return render_template(
        "/books/edit.html",
        book=book_repository.select(id),
        authors=authors,
        illustrators=authors,
        publishers=publisher_repository.select_all(),
        title=_title,
    )


@books_blueprint.route("/books/<int:id>/delete", methods=['POST'])
def books_delete(id):
    book_repository.delete(id)
    return redirect('/books')