# pylint: disable=no-self-use
from sqlalchemy import and_

from app.main.model.user_group import UserGroup
from app.main.model.user_group_member import user_group_member


class UserGroupRepository:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    def get_user_group_by_user_id_and_executive_device_device_key(self, user_id: str, device_key: str) -> UserGroup:
        return UserGroup.query.filter(
            and_(
                UserGroup.users.any(id=user_id),
                UserGroup.executive_devices.any(device_key=device_key)
            )
        ).first()
