from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# User data
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username not in users or users[username] != password:
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Protect a route with jwt_required, which will kick out requests without a valid JWT present
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == '__main__':
    app.run(debug=True)