from app.services.utils import get_logged_in_user
from tests.integration.helpers import generate_valid_user
from app.services.auth_service import UserService, verify_credentials, verify_token


class TestAuthService:

    def test_user_can_login(self, app):
        with app.app_context():
            # Arrange
            dto = generate_valid_user()
            test_user = UserService().register_user(dto)

            # Act
            is_verified = verify_credentials(dto.email, dto.password)
            logged_in_user = get_logged_in_user()

            # Assert
            assert is_verified is True
            assert logged_in_user.id == test_user.id, "Should have set logged in user in flask global session"

    def test_token_is_valid(self, app):
        with app.app_context():
            # Arrange
            dto = generate_valid_user()
            UserService().register_user(dto)
            verify_credentials(dto.email, dto.password)
            logged_in_user = get_logged_in_user()

            # Act
            is_valid = verify_token(logged_in_user.session_token)

            # Assert
            assert is_valid is True
