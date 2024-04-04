from flask import Flask, render_template, redirect, url_for
import sqlalchemy

app = Flask(__name__)
app.config['CSRF_token'] = '12345'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/urls')
def urls():
    return render_template('urls.html')

@app.route('/<short:str>')
def shortener(short):
    link = 'example.com'
    return redirect(url_for(link))