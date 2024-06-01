from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user data
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route for home
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Route for getting list of users
@app.route('/data', methods=['GET'])
def get_data():
    if not users:
        return jsonify([]), 200
    return jsonify(list(users.keys())), 200

# Route for status check
@app.route('/status', methods=['GET'])
def status():
    return "OK"

# Route for getting a specific user
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 409
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

# Route for clearing all users (for testing purposes)
@app.route('/clear_users', methods=['POST'])
def clear_users():
    global users
    users = {}
    return jsonify({"message": "All users cleared"}), 200

if __name__ == "__main__":
    app.run(debug=True)
