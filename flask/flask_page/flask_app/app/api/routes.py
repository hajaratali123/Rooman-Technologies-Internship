 
from flask import Blueprint, jsonify
from ..models import User

api = Blueprint('api', __name__)

@api.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])
