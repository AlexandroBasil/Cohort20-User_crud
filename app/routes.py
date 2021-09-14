from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from app.database import User

@app.route('/')
def home():
    out = {
        "status": "ok",
        "message": "Success",
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return out


@app.route('/users')
def get_all_users():
    out = {
        "status": "ok",
        "message": "Success"
    }
    users = User.query.all()
    out["body"] = []
    for user in users:
        user_dictionary = {}
        user_dictionary["id"] = user.id
        user_dictionary["first_name"] = user.first_name
        user_dictionary["last_name"] = user.last_name
        user_dictionary["hobbies"] = user.hobbies
        user_dictionary["active"] = user.active
        out["body"].append(user_dictionary)

    return out


@app.route('/users/<int:pk>')
def get_single_user(pk):
    out = {
        "status": "ok",
        "message": "Success"
    }
    user = User.query.filter_by(id=pk).first()
    out["body"] = {
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "hobbies": user.hobbies,
            "active": user.active
        }
    }
    return out


# @app.route('/users', methods=["POST"])
# def create_user():
#     out = {
#         "status": "ok",
#         "message": "Success"
#     }
#     user_data = request.json
#     out["user_id"] = insert(
#         user_data.get("first_name"),
#         user_data.get("last_name"),
#         user_data.get("hobbies")
#     )
#     return out, 201


@app.route('/users', methods=["POST"])
def create_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    db.session.add(
        User(
            first_name = user_data.get("first_name"),
            last_name = user_data.get("last_name"),
            hobbies = user_data.get("hobbies")
        )
    )
    db.session.commit()

    return out, 201

@app.route('/users/update')
def update_user():
    out = {
        "status": "ok",
        "message": "Success"
    }

    return out
