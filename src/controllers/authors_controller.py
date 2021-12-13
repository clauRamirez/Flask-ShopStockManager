from flask import render_template, redirect, request
from flask import Blueprint
from repositories import author_repository
from models.author import Author
import repositories.author_repository as author_repository

authors_blueprint = Blueprint("authors", __name__)


_title = "Authors"

@authors_blueprint.route("/authors", methods=['GET'])
def authors_index():
    if request.method == 'GET':
        return render_template(
            "/authors/index.html",
            title=_title,
            authors=author_repository.select_all()
        )
    if request.method == 'POST':
        # CREATE (POST) RESTful method here
        # return redirect("/authors") -> redirects to same route but with GET method
        pass


# NEW -> POST '/books/new'
@authors_blueprint.route("/authors/new", methods=['GET'])
def authors_new():
    return render_template(
        "/authors/new.html",
        authors=author_repository.select_all()
    )


# SHOW   -> GET '/books/<id>'
# UPDATE -> POST(PUT) '/books/<id>'
@authors_blueprint.route("/authors/<int:id>", methods=['GET', 'POST'])
def authors_id(id):
    if request.method == 'GET':
        return render_template(
            "/authors/show.html",
            author=author_repository.select(id)
        )
        
    if request.method == 'POST':
        author_repository.update(
            Author(
                name=request.form['name'],
                id=id
            )
        )
        return redirect("/authors")


# EDIT -> GET '/books/<id>/edit'
@authors_blueprint.route("/authors/<id>/edit", methods=['GET'])
def authors_edit(id):
    return render_template(
        # this needs to change
        "/authors/edit.html",
        book=author_repository.select(id),
        authors=author_repository.select_all()
    )


# DELETE -> POST(DELETE) '/authors/<id>'
@authors_blueprint.route("/authors/<id>/delete", methods=['POST'])
def authors_delete(id):
    # this needs to be checeked
    author_repository.delete(id)
    return redirect('/authors')
