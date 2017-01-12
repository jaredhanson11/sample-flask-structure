from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))

    @staticmethod
    def add_user(username):
        user = User(name=username)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.sessions.rollback()
