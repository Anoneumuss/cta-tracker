from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# GET endpoint: return all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST endpoint: add a new user
@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()  # Get JSON data from the request
    new_user = {"id": len(users) + 1, "name": data['name']}
    users.append(new_user)
    return jsonify(new_user), 201  # 201 = Created

if __name__ == '__main__':
    app.run(debug=True)
