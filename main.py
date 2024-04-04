import datetime

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

SHORT_LEN = 6

db = SQLAlchemy(app)

class URLmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255))
    short = db.Column(db.String(SHORT_LEN), unique=True)
    visits = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)




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