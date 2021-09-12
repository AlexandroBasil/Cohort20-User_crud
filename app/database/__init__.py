from flask import g
import sqlite3


DATABASE = "user.db"


def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def output_formatter(results: tuple):
    out = []
    for result in results:
        result_dict = {}
        result_dict["id"] = result[0]
        result_dict["first_name"] = result[1]
        result_dict["last_name"] = result[2]
        result_dict["hobbies"] = result[3]
        result_dict["active"] = result[4]
        out.append(result_dict)
    return out


def scan():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def read(user_id):
    cursor = get_db().execute(
        "SELECT * FROM user WHERE id=?", (user_id,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(first_name, last_name, hobbies):
    cursor = get_db()
    last_row_id = cursor.execute(
        """INSERT INTO user (
        first_name,
        last_name,
        hobbies
        ) VALUES (
        ?,
        ?,
        ?
        )
        """
    ), (first_name, last_name, hobbies).lastrowid
    cursor.commit()
    cursor.close()
    return last_row_id


def update(fn, ln, h, pk):
    cursor = get_db().execute(
        "UPDATE user SET first_name = ?, last_name = ?, hobbies = ? WHERE id = ?", (
            fn, ln, h, pk)
    )
    cursor.commit()
    cursor.close()
    return output_formatter(results)
