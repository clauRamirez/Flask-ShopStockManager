from flask import render_template, redirect, request
from flask import Blueprint
from models.book import Book
from repositories import book_repository, author_repository, publisher_repository

books_blueprint = Blueprint("books", __name__)

_title = "Books"


@books_blueprint.route("/books", methods=['GET', 'POST'])
def books_index():
    _title = "Home"
    if request.method == 'GET':
        return render_template(
            "/books/index.html",
            books=book_repository.select_all(),
            title=_title,
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
        return render_template(
            "/books/show.html",
            book=book_repository.select(id),
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