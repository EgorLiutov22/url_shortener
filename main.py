import datetime
import random
import string

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

SHORT_LEN = 6

db = SQLAlchemy(app)

def get_short():
        short = ''.join(random.choices(string.ascii_letters + string.ascii_letters, k=SHORT_LEN))
        if URLmodel.query.filter(URLmodel.short == short).first():
            return get_short()
        else:
            return short



class URLmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255))
    short = db.Column(db.String(SHORT_LEN), unique=True)
    visits = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)


with app.context():
    db.create_all()


class URLForm(FlaskForm):
    original_url = StringField('Вставьте ссылку',
                               validators=[DataRequired(message='Ссылка не может быть пустой'),
                                           URL(message='Неверная ссылка')])
    submit = SubmitField('Получить короткую ссылку')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        url = URLmodel()
        url.original_url = form.original_url.data
        url.short = get_short()
        db.sessin.add(url)
        db.session.commit()
    return render_template('index.html')


@app.route('/urls', methods=['GET'])
def urls():
    urls = db.query.all()
    return render_template('urls.html', urls=urls)


@app.route('/<string:short>', methods=['GET'])
def shortener(short):
    link = URLmodel.query.filter(URLmodel.short == short).first()
    if link:
        link.visits += 1
        db.session.add(link)
        db.session.commit()
        return redirect(url_for(link))
