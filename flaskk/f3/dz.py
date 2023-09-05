# Создать форму для регистрации пользователей на сайте. 
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". 
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, redirect, render_template, request, url_for
from flask_wtf import CSRFProtect
from flaskk.f3.modelss import db, User
from flaskk.f3.formss import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""
app.config['SECRET_KEY'] = b'e87aca28a5d32fd1c5ec6108723b905809cea3e88a7f5d12a07e07a5b817aba3'

db.init_app(app)
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/data/')
def data():
    return 'Your data!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка формы
        name = form.name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        add_user(name, last_name, email, password)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')

def add_user(name, last_name, email, password):
    user = User(name, last_name, email, password) 
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
