from src.views.publishers_views import publishers_blueprint
from src.views.books_views import books_blueprint
from src.views.authors_views import authors_blueprint
from flask import Flask
from flask import render_template, request, redirect


app = Flask(__name__)
app.url_map.strict_slashes = False


app.register_blueprint(authors_blueprint)
app.register_blueprint(books_blueprint)
app.register_blueprint(publishers_blueprint)


@app.before_request
def clear_trailing():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])


@app.route('/')
def index():
    return render_template("index.html", title="Home")


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404


if __name__ == "__main__":
    app.run()
