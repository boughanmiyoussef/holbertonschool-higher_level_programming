#!/usr/bin/python3
"""
Simple API using Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    """
    Welcome message for the API.
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """
    Returns a JSON response with a list of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))

@app.route("/status")
def get_status():
    """
    Returns "OK" to indicate that the API is running.
    """
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """
    Returns the full object corresponding to the provided username.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the users dictionary and returns a confirmation message.
    """
    data = request.get_json()
    username = data.get("username")
    if username:
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201
    else:
        return jsonify({"error": "Username not provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
