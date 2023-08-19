from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>/')
def hello(name='Unknown'):
    return f'Hello {name.capitalize()}!'

@app.route('/file/<path:file>')
def set_path(file):
    return f'File path: "{file}"'

@app.route('/numbers/<float:num>')
def set_number(num):
    print(type(num))
    return f'You input number: {num}'

if __name__ == '__main__':
    app.run()
