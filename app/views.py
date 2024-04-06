

from flask import Flask, render_template, redirect, url_for

from . import app, db
from .forms import URLForm
from .models import URLmodel
from .get_short import get_short






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