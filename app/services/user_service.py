from werkzeug.security import generate_password_hash

from app.models.dtos.user_dto import UserDTO


class UserService:

    def register_user(self, dto: UserDTO) -> UserDTO:
        """ Register a new user """
        user = dto.map_to_db_model()
        user.password_hash = generate_password_hash(dto.password)
        user.insert()
        return dto.map_from_db_model(user)
