from flask import render_template, redirect, request
from flask import Blueprint
from repositories import author_repository

authors_blueprint = Blueprint("authors", __name__)

@authors_blueprint.route("/authors", methods=['GET'])
def index():
    return render_template("/authors/index.html")