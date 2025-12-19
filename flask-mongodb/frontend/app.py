from flask import Flask, render_template
from datetime import datetime

BACKEND_URL = "http://localhost:5000"

app = Flask(__name__)

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')

    current_time = datetime.now().strftime('%H:%M')
    print(day_of_week)
    return render_template('index.html' , day=day_of_week, time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)