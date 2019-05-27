from schematics import Model
from schematics.exceptions import DataError
from schematics.types import IntType, StringType

from app.models.database.user import User

data_error = DataError  # Refer to dataerror to make it simpler to import into API


class UserDTO(Model):
    """ Describes a User """
    id = IntType()
    email = StringType(required=True)
    username = StringType(required=True)
    password = StringType()

    def map_to_db_model(self, user: User):
        """ Map DTO to database representation """
        user.email = self.email
        user.username = self.username

    def map_from_db_model(self, user: User):
        """ Map DB representation to DTO """
        self.id = user.id
        self.username = user.username
        self.email = user.email
