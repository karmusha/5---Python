from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Unknown'

@app.route('/Ira/')
def ira():
    return 'Hello Ira'

@app.route('/Olga/')
@app.route('/Olya/')
def olga():
    return 'Hello Olga'

if __name__ == '__main__':
    app.run()
