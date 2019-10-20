from datetime import datetime
from typing import Optional
from typing import Tuple

import flask_bcrypt

from app.main.model.user import User
from app.main.util.auth_utils import Auth
from app.main.util.constants import Constants
from app.main.repository.admin_repository import AdminRepository
from app.main.repository.user_repository import UserRepository


class UserService:
    _instance = None

    _admin_repository_instance = None
    _user_repository_instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    def __init__(self):
        self._admin_repository_instance = AdminRepository.get_instance()
        self._user_repository_instance = UserRepository.get_instance()

    def create_auth_token(self, email: str, password: str) -> Tuple[str, Optional[str]]:
        user = self._user_repository_instance.get_user_by_email(email)
        is_admin = False

        if user is None:
            user = self._admin_repository_instance.get_admin_by_email(email)
            is_admin = True

            if user is None:
                return Constants.RESPONSE_MESSAGE_INVALID_CREDENTIALS, None

        try:
            is_password_correct = flask_bcrypt.check_password_hash(user.password, password)
        except ValueError:
            return Constants.RESPONSE_MESSAGE_INVALID_CREDENTIALS, None

        if not is_password_correct:
            return Constants.RESPONSE_MESSAGE_INVALID_CREDENTIALS, None

        token = Auth.encode_auth_token(user.id, is_admin)

        return Constants.RESPONSE_MESSAGE_OK, token

    def create_user(self, username: str, email: str, password: str) -> str:
        if not username or not email or not password:
            return Constants.RESPONSE_MESSAGE_BAD_REQUEST

        if self._user_repository_instance.get_user_by_email_or_username(email, username) is not None:
            return Constants.RESPONSE_MESSAGE_USER_ALREADY_EXISTS

        if self._admin_repository_instance.get_admin_by_email_or_username(email, username) is not None:
            return Constants.RESPONSE_MESSAGE_USER_ALREADY_EXISTS

        password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(
            username=username,
            email=email,
            registered_on=datetime.utcnow(),
            password=password_hash
        )

        if not self._user_repository_instance.save(user):
            return Constants.RESPONSE_MESSAGE_ERROR

        return Constants.RESPONSE_MESSAGE_OK
