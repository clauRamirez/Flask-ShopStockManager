from os import name
from flask import render_template, redirect, request
from flask import Blueprint
from repositories import publisher_repository
from models.publisher import Publisher
import repositories.publisher_repository as publisher_repository

publishers_blueprint = Blueprint("publishers", __name__)

# Title is not appearing in subdirectories i.e: /authors/new etc
_title = 'Publishers'

@publishers_blueprint.route("/publishers", methods=['GET', 'POST'])
def publishers_index():
    if request.method == 'GET':
        return render_template(
            "/publishers/index.html",
            title=_title,
            publishers=publisher_repository.select_all()
        )

    if request.method == 'POST':
        # make this block less clunky
        if request.form['salesperson'] == '':
            publisher_repository.save(
                Publisher(
                    name=request.form['name'],
                    website=request.form['website']
                )
            )
        else:
            publisher_repository.save(
                Publisher(
                    name=request.form['name'],
                    website=request.form['website'],
                    salesperson=request.form['salesperson'],
                    contact=request.form['contact']
                )
            )
        return redirect("/publishers")


@publishers_blueprint.route("/publishers/new", methods=['GET'])
def publishers_new():
    return render_template(
        "/publishers/new.html",
    )

'''
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
    '''