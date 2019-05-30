from schematics import Model
from schematics.exceptions import DataError
from schematics.types import IntType, StringType, FloatType

from app.models.database.user import User

data_error = DataError  # Refer to dataerror to make it simpler to import into API


class JWTSessionUser(Model):
    """ A simplified user object for storing in the session and encoding in the JWT """

    id = IntType()
    first_name = StringType(required=True, serialized_name="firstName")
    session_token = StringType(
        serialized_name="sessionToken", serialize_when_none=False
    )
    exp = FloatType()


class UserDTO(Model):
    """ Describes a User """

    id = IntType()
    first_name = StringType(required=True, serialized_name="firstName")
    last_name = StringType(required=True, serialized_name="lastName")
    email = StringType(required=True)
    password = StringType(serialize_when_none=False)

    def map_to_db_model(self, user: User = None) -> User:
        """ Map DTO to database representation """
        if user is None:
            user = User()
        user.email = self.email
        user.first_name = self.first_name
        user.last_name = self.last_name
        return user

    def map_from_db_model(self, user: User) -> "UserDTO":
        """ Map DB representation to DTO """
        self.id = user.id
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email
        self.password = user.password_hash
        return self

    def __repr__(self):
        return f"<UserDTO {self.first_name} {self.last_name}>"
