from base64 import b64encode

from app.models.dtos.user_dto import UserDTO
from app.services.user_service import UserService
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

    def test_user_can_login(self, app, client):
        with app.app_context():

            # Arrange
            user = generate_valid_user()
            UserService().register_user(user)

            # Set up basic auth header
            auth_details = f'{user.email}:{user.password}'.encode('utf-8')
            base64string = b64encode(auth_details)
            auth_header = f"Basic {base64string.decode('utf-8')}"

            # Act
            response = client.put("/api/v1/user/login", headers={"Authorization": auth_header})

            # Assert
            assert response.status_code == 200