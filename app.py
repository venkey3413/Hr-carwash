from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock data storage for demo purposes
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    user_name = request.form.get('user_name')
    car_type = request.form.get('car_type')
    washing_price = request.form.get('washing_price')
    estimation_time = request.form.get('estimation_time')

    if user_name and car_type and washing_price and estimation_time:
        task = {
            'user_name': user_name,
            'car_type': car_type,
            'washing_price': float(washing_price),
            'estimation_time': int(estimation_time)
        }
        tasks.append(task)
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
