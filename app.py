from flask import Flask, escape, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import sys

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)
    # return "Welcome to My WatchList!"
    # return "欢迎来到我的 WatchList！"
    # return "<h1>Hello Totoro</h1><img src='http://helloflask.com/totoro.gif'>"


@app.route("/user/<username>")
def user_page(username):
    return "User: %s" % escape(username)


@app.route("/test")
def test_url_for():
    print(url_for('index'))
    print(url_for('user_page', username='greyli'))
    print(url_for('user_page', username='wangdingbo'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return "Test Page"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


import click


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database')


@app.cli.command()
def forge():
    db.drop_all()
    db.create_all()

    name = "Wang Dingbo"
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'}
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('Generate fake data Done.')


@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)
