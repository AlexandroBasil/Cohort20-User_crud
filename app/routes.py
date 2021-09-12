from datetime import datetime
from flask import Flask, request

from app.database import scan, read, insert, update

app = Flask(__name__)


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
    out["body"] = scan()
    return out


@app.route('/users/<int:pk>')
def get_single_user(pk):
    out = {
        "status": "ok",
        "message": "Success"
    }
    out["body"] = read(pk)
    return out


@app.route('/users', method=["POST"])
def create_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    out["user_id"] = insert(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
    return out, 201


@app.route('/users', method=["PUT"])
def view_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    out["user_id"] = update(
        user_data.get("id"),
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
    return out
