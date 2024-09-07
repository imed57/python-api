from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required

api = Blueprint('api', __name__)

users = [{"username": "test", "password": "test"}]  # Exemple de base utilisateur

@api.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = next((u for u in users if u['username'] == username and u['password'] == password), None)

    if user:
        token = create_access_token(identity=username)
        return jsonify(access_token=token), 200
    return jsonify({"msg": "Bad credentials"}), 401

@api.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"msg": "You are viewing a protected route!"}), 200
