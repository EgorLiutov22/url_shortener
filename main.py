from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['CSRF_token'] = '12345'

db = SQLAlchemy(app)

with app.context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/urls', methods=['GET'])
def urls():
    return render_template('urls.html')

@app.route('/<string:short>', methods=['GET'])
def shortener(short):
    link = 'example.com'
    return redirect(url_for(link))