from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Ceo%402030@localhost:3306/flask_p"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
CORS(app)  # Enable Cross-Origin Resource Sharing

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

# Ensure database tables are created
with app.app_context():
    db.create_all()

# Home Route (Frontend)
@app.route("/")
def index():
    return render_template("index.html")

# Add User
@app.route("/users", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
        print("Received Data:", data)  # Debugging output

        if not data or "name" not in data or "email" not in data:
            return jsonify({"error": "Name and Email are required"}), 400

        new_user = User(name=data["name"], email=data["email"])
        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        print("Error:", str(e))  # Log the actual error
        return jsonify({"error": str(e)}), 500




# Get All Users
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Get Single User
@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

# Update User
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    try:
        user = User.query.get_or_404(id)
        data = request.get_json()
        
        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        
        db.session.commit()
        return jsonify(user.to_dict())

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Delete User
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    try:
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
