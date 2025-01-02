from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'car_wash.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL,
                Phone_number REAL NOT NULL,
                car_type TEXT NOT NULL,
                washing_price REAL NOT NULL,
                estimation_time INTEGER NOT NULL
            )
        ''')
        conn.commit()

@app.route('/')
def home():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        # Calculate totals
        total_cost = sum(task[3] for task in tasks)
        total_time = sum(task[4] for task in tasks)

    return render_template('index.html', tasks=tasks, total_cost=total_cost, total_time=total_time)

@app.route('/add', methods=['POST'])
def add_task():
    user_name = request.form.get('user_name')
    Phone_number = request.form.get('phone_type')
    car_type = request.form.get('car_type')
    washing_price = request.form.get('washing_price')
    estimation_time = request.form.get('estimation_time')

    if user_name and phone_number and car_type and washing_price and estimation_time:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO tasks (user_name, phone_number, car_type, washing_price, estimation_time)
                VALUES (?, ?, ?, ?)
            ''', (user_name, car_type, flot(phone_number), float(washing_price), int(estimation_time)))
            conn.commit()
    return redirect(url_for('home'))

@app.route('/task-list')
def task_list():
    tasks = Task.query.all()
    return render_template('task_list.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    init_db()
    app.run(debug=True)
