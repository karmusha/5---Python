from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'

@app.route('/index/')
def html_index():
    context = {
        'title': 'Private blog',
        'name': 'Karma',
    }
    return render_template('index2.html', **context)