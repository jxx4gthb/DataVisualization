import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/mypage2')
def mypage():
    return flask.send_from_directory('static', 'mypage.html')

@app.route('/dtsdt')
def dtsdt():
    return flask.send_from_directory('static','动态散点图简单版.html')

@app.route('/path_example')
def path_example():
    return flask.send_from_directory('static','path_example.html')

@app.route('/final')
def cqmap():
    return flask.send_from_directory('static','oop_try.html')

@app.route('/b3test')
def b3test():
    return flask.send_from_directory('static','barcharttest.html')

if __name__ == '__main__':
    app.run(debug=True)
