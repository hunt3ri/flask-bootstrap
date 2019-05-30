from app.services.utils import get_logged_in_user
from tests.integration.helpers import generate_valid_user
from app.services.auth_service import UserService, verify_credentials


class TestAuthService:

    def test_user_can_login(self, app):
        # Arrange
        with app.app_context():
            dto = generate_valid_user()
            test_user = UserService().register_user(dto)

            is_verified = verify_credentials(dto.email, dto.password)
            logged_in_user = get_logged_in_user()

            assert is_verified is True
            assert logged_in_user.id == test_user.id, "Should have set logged in user in flask global session"
