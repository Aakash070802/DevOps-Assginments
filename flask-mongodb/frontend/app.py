from flask import Flask, render_template, request
from datetime import datetime
import requests

BACKEND_URL = "http://0.0.0.0:5000"

app = Flask(__name__)

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')

    current_time = datetime.now().strftime('%H:%M')
    print(day_of_week)
    return render_template('index.html' , day=day_of_week, time=current_time)
@app.route('/submit', methods=['POST'])
def submit():
    form_data = {
        'username': request.form['username'],
        'email': request.form['email'],
        'password': request.form['password'],
        'cnf-passwrd': request.form['cnf-passwrd']
    }
    response = requests.post(f"{BACKEND_URL}/submit", data=form_data)

    result = response.json()

    if result['status'] == 'success':
        return render_template('success.html', message=result['message'])
    else:
        return result['message'], 400
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)