import uuid

from app.models.dtos.user_dto import UserDTO


def generate_valid_user() -> UserDTO:
    """ Helper to generate a valid user """
    unique_name = str(uuid.uuid4())

    dto = UserDTO()
    dto.first_name = "Iain"
    dto.last_name = "Hunter"
    dto.email = f"{unique_name}@test.com"
    dto.password = "secret"
    return dto
