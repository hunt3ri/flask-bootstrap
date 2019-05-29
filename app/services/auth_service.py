from typing import Optional, Tuple

from flask_httpauth import HTTPBasicAuth

from app.models.dtos.user_dto import UserDTO
from app.services.user_service import UserService

basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_credentials(username: str, password: str) -> bool:
    """ Verify username and password are valid """
    authorized, user_dto = AuthService().is_valid_credentials(username, password)
    # if authorized:
    #     user_dto.encrypted_password = None  # Hide password
    #     #set_auth_details(user_dto)
    #     return True
    # else:
    #     return False


class AuthService:

    def is_valid_credentials(self, username: str, password: str) -> Tuple[bool, Optional[UserDTO]]:
        """ Validate user credentials by checking with the database """
        user = UserService().get_user_by_email(username)

        # try:
        #     user_dto = UserService().get_user_dto_by_username(username)
        #     if user_dto is not None:
        #         # Check password against the database
        #         hash1 = md5(password.encode("UTF-8")).hexdigest()
        #         hashed_password = md5((username + hash1).encode("UTF-8")).hexdigest()
        #         if hashed_password == user_dto.encrypted_password:
        #             return True, user_dto
        #         else:
        #             return False, None
        #     else:
        #         return False, None
        # except NotFound:
        #     return False, None