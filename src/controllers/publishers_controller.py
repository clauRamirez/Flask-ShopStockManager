from flask import render_template, redirect, request
from flask import Blueprint
from models.publisher import Publisher
from repositories import publisher_repository

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

# SHOW   -> GET '/books/<id>'
# UPDATE -> POST(PUT) '/books/<id>'
@publishers_blueprint.route("/publishers/<int:id>", methods=['GET', 'POST'])
def publishers_id(id):
    if request.method == 'GET':
        return render_template(
            "/publishers/show.html",
            publisher=publisher_repository.select(id)
        ) 
    if request.method == 'POST':
        publisher_repository.update(
            Publisher(
                name=request.form['name'],
                website=request.form['website'],
                salesperson=request.form['salesperson'],
                contact=request.form['contact'],
                id=id
            )
        )
        return redirect("/publishers")



# EDIT -> GET '/books/<id>/edit'
@publishers_blueprint.route("/publishers/<int:id>/edit", methods=['GET'])
def publishers_edit(id):
    return render_template(
        # this needs to change
        "/publishers/edit.html",
        publisher=publisher_repository.select(id)
    )


# DELETE -> POST(DELETE) '/publishers/<id>'
@publishers_blueprint.route("/publishers/<id>/delete", methods=['POST'])
def publishers_delete(id):
    publisher_repository.delete(id)
    return redirect('/publishers')
