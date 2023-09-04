from datetime import datetime, timedelta
from flask import Flask, jsonify, render_template, request
from flask_wtf import CSRFProtect
from flaskk.f3.models import db, User, Post, Comment
from flaskk.f3.forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = b'acacac546561a65c16a5c6a51c6a51'
db.init_app(app)
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/data/')
def data():
    return 'Your data!'

@app.route('/form/', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return 'No CSRF protection!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка формы
        pass
    return render_template('login.html', form=form)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка формы
        email = form.email.data
        password = form.password.data
        print(email, password)
        pass
    return render_template('register.html', form=form)

@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)

@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)

@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error':'Posts not found'}), 404
    
@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow()-timedelta(days=7)
    posts = Post.query.filter(Post.created_at>=date).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error':'Posts not found'}), 404
    

@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')

@app.cli.command("add-john") 
def add_user(): 
    user = User(username='john', email='john@example.com') 
    db.session.add(user) 
    db.session.commit() 
    print('John add in DB!')

@app.cli.command("edit-john") 
def edit_user(): 
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@example.com' 
    db.session.commit() 
    print('Edit John mail in DB!')

@app.cli.command("del-john") 
def del_user(): 
    user = User.query.filter_by(username='john').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete John from DB!')

@app.cli.command("fill-db")
def fill_tables():
    count = 5 
    # Добавляем пользователей 
    for user in range(1, count+1): 
        new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
        db.session.add(new_user)
    db.session.commit()
        
    # Добавляем статьи
    for post in range(1, count**2):
        author = User.query.filter_by(username=f'user{post% count+1}').first()
        new_post = Post(title=f'Posttitle{post}', content=f'Postcontent{post}', author=author)
        db.session.add(new_post)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
