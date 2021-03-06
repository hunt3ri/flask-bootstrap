from sqlalchemy import exc

from app import db
from app.services.utils import FlaskBootstrapError


class User(db.Model):
    """ Models the users table """

    __tablename__ = "users"

    id = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def insert(self):
        """ Insert a new record """
        db.session.add(self)
        self.update()

    def update(self):
        """ Update record in scope """
        try:
            db.session.commit()
        except exc.IntegrityError as e:
            db.session.rollback()  # After error MUST rollback session avoid session flush errors
            raise FlaskBootstrapError(
                f"Integrity error saving user: {self}, error {str(e)}"
            )

    def get_by_email(self, email: str) -> "User":
        """ Return user matching email or raise 404 """
        user = User.query.filter_by(email=email).first_or_404()
        return user

    def get_by_id(self, id: int) -> "User":
        """ Return user matching id or raise 404 """
        user = User.query.filter_by(id=id).first_or_404()
        return user

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"
