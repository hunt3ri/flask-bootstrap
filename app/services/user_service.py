from app.models.dtos.user_dto import UserDTO
from app.models.database.user import User


class UserService:

    def register_user(self, dto: UserDTO) -> UserDTO:
        """ Register a new user """
        user = dto.map_to_db_model()
        user.password_hash = get_password_hash(dto.password)
        user.insert()

        dto.map_from_db_model(user)
        return dto

    def get_user_by_email(self, email: str) -> User:
        """ Get user matching email address """
        return User().get_by_email(email)

    def get_user_by_id(self, user_id: int) -> UserDTO:
        """ Get user matching id """
        user = User().get_by_id(user_id)
        dto = UserDTO().map_from_db_model(user)
        return dto


from app.services.auth_service import get_password_hash  # noqa  avoid circular reference
