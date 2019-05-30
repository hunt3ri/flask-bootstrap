from app.models.dtos.user_dto import UserDTO
from tests.integration.helpers import generate_valid_user


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
        user = generate_valid_user()

        # Act
        response = client.post("/api/v1/user/register", json=user.to_primitive())

        registered_user = UserDTO(response.json)

        # Assert
        assert response.status_code == 201
        assert registered_user.id > 0
