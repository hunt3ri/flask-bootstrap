from app import db


class User(db.Model):
    """ Models the users table """

    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"
