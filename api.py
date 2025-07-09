from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
users = [
    {"id": 1, "name": "akash", "email": "akashkumarshuk805133@gmail.com"},
    {"id": 2, "name": "jagesh", "email": "jageshshukla222@gmail.com"}
]

# GET /user - Get all users
@app.route("/user", methods=["GET"])
def get_users():
    return jsonify(users)

# GET /user/<id> - Get single user
@app.route("/user/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST /user - Create user
@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# DELETE /user/<id> - Delete user
@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
