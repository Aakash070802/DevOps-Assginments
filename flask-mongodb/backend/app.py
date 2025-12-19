import os
from flask import Flask, json, request, jsonify
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)

db = client.test

collection = db['flask-tutorial']


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('cnf-passwrd')

    if password != confirm_password:
        return jsonify({
            'status': 'error',
            'message': 'Password do not match'
        }), 400
    collection.insert_one({
        'username': username,
        'email': email,
        'password': password
    })

    return jsonify({
        'status': 'success',
        'message': 'User registered successfully',
    })

# @app.route('/view')
# def view():
#     user = collection.find()
#     users_list = []
#     for usr in user:
#         users_list.append({
#             'username': usr['username'],
#             'email': usr['email'],
#             'password': usr['password']
#         })
#     return jsonify(users_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)