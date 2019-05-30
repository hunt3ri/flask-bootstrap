import uuid
from app.models.dtos.user_dto import UserDTO


class TestUsersAPI:

    def test_register_user_api_returns_400_if_mandatory_fields_missing(self, client):
        # Arrange
        dto = UserDTO()
        dto.first_name = "Iain"

        # Act
        response = client.post("/api/v1/user/register", json=dto.to_primitive())

        # Assert
        assert response.status_code == 400


    def test_valid_user_is_successfully_registered(self, client):
        # Arrange
        unique_name = str(uuid.uuid4())

        dto = UserDTO()
        dto.first_name = "Iain"
        dto.last_name = "Hunter"
        dto.email = f"{unique_name}@test.com"
        dto.password = "secret"

        # Act
        response = client.post("/api/v1/user/register", json=dto.to_primitive())

        registered_user = UserDTO(response.json)

        # Assert
        assert response.status_code == 201
        assert registered_user.id > 0
