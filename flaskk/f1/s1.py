from flask import Flask

app = Flask(__name__)

@app.route('/hi/')
def hi():
    return 'Hi'

@app.route('/about/')
def about():
    context = {'title': 'My page',
               'name': 'Karma',
               }
    return 'About'
    # return render_template('about.html', **context)

@app.route('/contacts/')
def contacts():
    # context = {'title': 'My page',
    #            'name': 'Karma',
    #            }
    return 'Contacts: karmusha@gmail.com'
    # return render_template('about.html', **context)

@app.route('/sum/<int:a>+<int:b>/')
def sum(a, b):
    return f'{a} + {b} = {a + b}'

@app.route('/str/<text>/')
def str_length(text):
    return f'Строка: "{text}". Длина строки = {len(text)}'

@app.route('/html/')
def html():
    s = '''<h1>My first page</h1><p>Hello World!</p>'''
    return s

if __name__ == '__main__':
    app.run()