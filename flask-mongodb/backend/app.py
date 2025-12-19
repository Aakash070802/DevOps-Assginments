import os
from flask import Flask, request, jsonify
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)

db = client.test

collection = db['flask-tutorial']


app = Flask(__name__)

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

@app.route('/view')
def view():
    user = collection.find()
    users_list = []
    for usr in user:
        users_list.append({
            'username': usr['username'],
            'email': usr['email'],
            'password': usr['password']
        })
    return jsonify(users_list)

if __name__ == '__main__':
    app.run(debug=True)