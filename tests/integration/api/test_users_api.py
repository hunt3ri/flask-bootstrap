from app.models.dtos.user_dto import UserDTO


def test_register_user_api_returns_400_if_mandatory_fields_missing(client):
    # Arrange
    dto = UserDTO()
    dto.first_name = "Iain"

    # Act
    response = client.post("/api/v1/user/register", json=dto.to_primitive())

    # Assert
    assert response.status_code == 400
