from flask import Flask, escape, url_for

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to My WatchList!"
    # return "欢迎来到我的 WatchList！"
    # return "<h1>Hello Totoro</h1><img src='http://helloflask.com/totoro.gif'>"


@app.route("/user/<username>")
def user_page(username):
    return "User: %s" % escape(username)


@app.route("/test")
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', username='greyli'))
    print(url_for('user_page', username='wangdingbo'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return "Test Page"
