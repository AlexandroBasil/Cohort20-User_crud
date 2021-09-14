from app.routes import db, User


def create_my_user(first_name, last_name, hobbies):
    db.session.add(
        User(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies
        )
    )
    db.session.commit()


if __name__ == '__main__':
    create_my_user("Alex", "Garcia", "Running")
    create_my_user("Micky", "Jordan", "Baseball")
    create_my_user("Omega", "Speedmaster", "Watch Collecting")
# Example of how to select all user
    users = User.query.all()
    print(users)
# Example of how to select a user by their id:
    user = User.query.filter_by(id=3).first()
    print(user)
