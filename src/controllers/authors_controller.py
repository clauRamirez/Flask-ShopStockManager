from flask import render_template, redirect, request
from flask import Blueprint
from models.author import Author
from repositories import author_repository

authors_blueprint = Blueprint("authors", __name__)

# Title is not appearing in subdirectories i.e: /authors/new etc
_title = "Authors"

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
@authors_blueprint.route("/authors/<int:id>/edit", methods=['GET'])
def authors_edit(id):
    return render_template(
        # this needs to change
        "/authors/edit.html",
        author=author_repository.select(id)
    )


# DELETE -> POST(DELETE) '/authors/<id>'
@authors_blueprint.route("/authors/<id>/delete", methods=['POST'])
def authors_delete(id):
    author_repository.delete(id)
    return redirect('/authors')
