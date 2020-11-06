from flask import Flask, escape, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', name=name, movies=movies)
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
