from dotenv import load_dotenv
from os import getenv
from flask import Flask
from flask import render_template, request, redirect

load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False

# import controllers and blueprints below
from controllers.authors_controller import authors_blueprint
from controllers.books_controller import books_blueprint
from controllers.publishers_controller import publishers_blueprint

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
    app.run(debug=getenv('DEBUG_MODE'))