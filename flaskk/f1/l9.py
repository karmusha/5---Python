from flask import Flask, render_template

app = Flask(__name__)

html = """
<h1>Hello, my name is Alex.</h1>
<p>I know Flask.<br>Look!</p>
"""

@app.route('/')
def index():
    return 'Hi'

@app.route('/text/')
def text():
    return html

@app.route('/for/')
def show_for():
    context = {'title':'Cycle',
               'poem': ['Every single one',
                        's got a storry to tell',
                        'From the queen of England',
                        'To the hounds of hell.',
                        ]}
    # txt = '<h1>Guess the song</h1>\n<p>' + '<br>'.join(poem) + '</p>'
    return render_template('show_for.html', **context)

if __name__ == '__main__':
    app.run()
