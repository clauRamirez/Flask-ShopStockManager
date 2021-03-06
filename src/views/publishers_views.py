from flask import render_template, redirect, request
from flask import Blueprint
from models.publisher import Publisher
from repositories import publisher_repository
from views.utils import get_title

publishers_blueprint = Blueprint("publishers", __name__)

_title = get_title(__file__)

@publishers_blueprint.route("/publishers", methods=['GET', 'POST'])
def publishers_index():
    if request.method == 'GET':
        return render_template(
            "/publishers/index.html",
            publishers=publisher_repository.select_all(),
            title=_title
        )
        
    if request.method == 'POST':
        rf = request.form

        if rf['salesperson'] == '':
            publisher_repository.save(
                Publisher(
                    name=rf['name'],
                    website=rf['website']
                )
            )
        else:
            publisher_repository.save(
                Publisher(
                    name=rf['name'],
                    website=rf['website'],
                    salesperson=rf['salesperson'],
                    contact=rf['contact']
                )
            )
        return redirect("/publishers")


@publishers_blueprint.route("/publishers/new", methods=['GET'])
def publishers_new():
    return render_template(
        "/publishers/new.html",
    )

@publishers_blueprint.route("/publishers/<int:id>", methods=['GET', 'POST'])
def publishers_id(id):
    if request.method == 'GET':
        return render_template(
            "/publishers/show.html",
            publisher=publisher_repository.select(id),
            books=publisher_repository.get_books_by_publisher(publisher_repository.select(id)),
            title=_title
        ) 
    if request.method == 'POST':
        rf = request.form
        publisher_repository.update(
            Publisher(
                name=rf['name'],
                website=rf['website'],
                salesperson=rf['salesperson'],
                contact=rf['contact'],
                id=id
            )
        )
        return redirect("/publishers")


@publishers_blueprint.route("/publishers/<int:id>/edit", methods=['GET'])
def publishers_edit(id):
    return render_template(
        "/publishers/edit.html",
        publisher=publisher_repository.select(id),
        title=_title
    )


@publishers_blueprint.route("/publishers/<int:id>/delete", methods=['POST'])
def publishers_delete(id):
    publisher_repository.delete(id)
    return redirect('/publishers')
