# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах. 
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл". 
# Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/students/')
def students():
    data = [
            {'fname': 'Ira', 'lname': 'Kirova', 'age': 20, 'avg_grade': 4.5},
            {'fname': 'Olga', 'lname': 'Elova', 'age': 19, 'avg_grade': 4.0},
            {'fname': 'Igor', 'lname': 'Maslov', 'age': 19, 'avg_grade': 4.2},
            ]
    return render_template('students.html', students=data)

if __name__ == '__main__':
    app.run()