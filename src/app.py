from flask import Flask
from flask import render_template

app = Flask(__name__)

# import controllers and blueprints below
from controllers.authors_controller import authors_blueprint

app.register_blueprint(authors_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)