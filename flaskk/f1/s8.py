# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для каждой отдельной страницы. 
# Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.
# Cоздать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is Karma'

@app.route('/main/')
def main():
    context = {
        'title': 'Main page',
    }
    return render_template('main.html', **context)

@app.route('/about/')
def about():
    info = [
            {'year': '2020', 'info': 'We open our shop and sell clothes.'},
            {'year': '2021', 'info': 'We add shoes.'},
            {'year': '2022', 'info': 'We add coats.'},
            {'year': '2023', 'info': 'We are going to add hoodies.'},
            ]
    return render_template('about.html', data=info)

@app.route('/contacts/')
def contacts():
    _contacts = [{'name' : 'Никанор', 
               'mail' : 'nik@mail.ru', 
               'phone' : '+7-987-654-32-10', 
               }, 
               {'name' : 'Феофан', 
                'mail' : 'feo@mail.ru', 
                'phone' : '+7-987-444-33-22', 
                }, 
                {'name' : 'Оверран', 
                 'mail' : 'forest@mail.ru', 
                 'phone' : '+7-903-333-33-33', 
                 },
                 ]
    context = {'contacts' : _contacts,
               'title': 'Our contacts'}
    
    return render_template('contacts.html', **context)

@app.route('/clothes/')
def clothes():
    _items = [{'id' : '001', 
                'name' : 'Шляпа', 
                'description' : 'широкополая', 
                }, 
                {'id' : '002', 
                'name' : 'Шапка', 
                'description' : 'ушанка', 
                }, 
                {'id' : '003', 
                'name' : 'Кепка', 
                'description' : 'модная', 
                }, 
                ]
    context = {'clothes' : _items,
               'title': 'Our clothes'}
    
    return render_template('clothes.html', **context)

@app.route('/shoes/')
def shoes():
    _items = [{'id' : '011', 
                'name' : 'Кроссовки', 
                'description' : 'Puma', 
                }, 
                {'id' : '012', 
                'name' : 'Ботинки', 
                'description' : 'лакированные', 
                },
                ]
    context = {'shoes' : _items,
               'title': 'Our shoes'}
    
    return render_template('shoes.html', **context)

@app.route('/coats/')
def coats():
    _items = [{'id' : '111', 
                'name' : 'Пальто', 
                'description' : 'конское', 
                }, 
                {'id' : '112', 
                'name' : 'Шуба', 
                'description' : 'дуба', 
                },
                ]
    context = {'coats' : _items,
               'title': 'Our coats'}
    
    return render_template('coats.html', **context)

if __name__ == '__main__':
    app.run()
