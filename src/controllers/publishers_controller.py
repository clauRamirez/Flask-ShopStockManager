from flask import render_template, redirect, request
from flask import Blueprint
from repositories import publisher_repository

publishers_blueprint = Blueprint("publishers", __name__)

@publishers_blueprint.route("/publishers", methods=['GET'])
def index():
    return render_template("/publishers/index.html")