from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')

    current_time = datetime.now().strftime('%H:%M')
    print(day_of_week)
    return render_template('index.html' , day=day_of_week, time=current_time)


if __name__ == '__main__':
    app.run(debug=True)