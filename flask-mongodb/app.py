from flask import Flask, request, render_template, jsonify
from datetime import datetime
import pymongo


client = pymongo.MongoClient("mongodb+srv://akkiakash294_db_user:Akkimongo741974@learncluster.nixinic.mongodb.net/?appName=learnCluster")

db = client.test


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
    user_data = {
        'username': username,
        'email': email,
        'password': password
    }
    print(user_data)
    return jsonify({
        'status': 'success',
        'message': 'User registered successfully',
        'data': user_data
    })

if __name__ == '__main__':
    app.run(debug=True)