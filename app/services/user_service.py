from werkzeug.security import generate_password_hash

from app.models.dtos.user_dto import UserDTO
from app.models.database.user import User


class UserService:
    def register_user(self, dto: UserDTO) -> UserDTO:
        """ Register a new user """
        user = dto.map_to_db_model()
        user.password_hash = generate_password_hash(dto.password)
        user.insert()

        dto.map_from_db_model(user)
        return dto

    def get_user_by_email(self, email: str) -> UserDTO:
        """ Get user matching email address """
        user = User().get_by_email(email)
        dto = UserDTO().map_from_db_model(user)
        return dto
