from flask import render_template, redirect, request
from flask import Blueprint
from repositories import books_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books", methods=['GET'])
def index():
    return render_template("/books/index.html")