# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей. 
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации. 
# Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/news/')
def news():
    data = [
            {'fname': 'Ira', 'lname': 'Kirova', 'age': 20, 'avg_grade': 4.5},
            {'fname': 'Olga', 'lname': 'Elova', 'age': 19, 'avg_grade': 4.0},
            {'fname': 'Igor', 'lname': 'Maslov', 'age': 19, 'avg_grade': 4.2},
            ]
    return render_template('news.html', students=data)

if __name__ == '__main__':
    app.run()
