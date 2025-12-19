import os
from flask import Flask, request, render_template, jsonify
from datetime import datetime
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)

db = client.test

collection = db['flask-tutorial']


app = Flask(__name__)

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')

    current_time = datetime.now().strftime('%H:%M')
    print(day_of_week)
    return render_template('index.html' , day=day_of_week, time=current_time)
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['cnf-passwrd']

    if password != confirm_password:
        return jsonify({
            'status': 'error',
            'message': 'Password do not match'
        })
    collection.insert_one({
        'username': username,
        'email': email,
        'password': password
    })

    return jsonify({
        'status': 'success',
        'message': 'User registered successfully',
    })

if __name__ == '__main__':
    app.run(debug=True)