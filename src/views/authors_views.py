from flask import render_template, redirect, request
from flask import Blueprint
from models.author import Author
from repositories import author_repository
from views.utils import get_title

authors_blueprint = Blueprint("authors", __name__)

_title = get_title(__file__)

@authors_blueprint.route("/authors", methods=['GET', 'POST'])
def authors_index():
    if request.method == 'GET':
        return render_template(
            "/authors/index.html",
            title=_title,
            authors=author_repository.select_all()
        )
    if request.method == 'POST':
        author_repository.save(
            Author(name=request.form['name'])
        )
        return redirect("/authors")        


@authors_blueprint.route("/authors/new", methods=['GET'])
def authors_new():
    return render_template(
        "/authors/new.html",
        title=_title,
    )


@authors_blueprint.route("/authors/<int:id>", methods=['GET', 'POST'])
def authors_id(id):
    if request.method == 'GET':
        authors, illustrators = author_repository.filter_authors(id)

        return render_template(
            "/authors/show.html",
            author=author_repository.select(id),
            books_by_author=authors,
            books_by_illustrator=illustrators,
            title=_title
        ) 
    if request.method == 'POST':
        author_repository.update(
            Author(
                name=request.form['name'],
                id=id
            )
        )
        return redirect("/authors")


@authors_blueprint.route("/authors/<int:id>/edit", methods=['GET'])
def authors_edit(id):
    return render_template(
        "/authors/edit.html",
        author=author_repository.select(id),
        title=_title,
    )


@authors_blueprint.route("/authors/<int:id>/delete", methods=['POST'])
def authors_delete(id):
    author_repository.delete(id)
    return redirect('/authors')
