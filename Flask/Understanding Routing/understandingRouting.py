# HW to import flask
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/Dojo!')
def hello():
    return 'Dojo!!'



@app.route('/say/<flask>')
def hi_Flask(flask):
    return 'Hi'+ ' ' + flask


@app.route('/say/<michael>')
def hi_Michael(Michael):
    return 'Hi'+ ' ' + Michael


@app.route('/say/<John>')
def hi_John(John):
    return 'Hi'+ ' ' + John


@app.route('/test/<text>/<int:num>')
def repeat(text,num):
    word=""
    for i in range(0,num):
        word+=f'hello,{text} <br>'
    return word



@app.route('/repeat/<path:path>')
def repeat_word(path):

    return 'sorry no file no path!'






if __name__=="__main__":
    app.run(debug=True)