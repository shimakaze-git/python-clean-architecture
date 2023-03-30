from datetime import datetime


class UserCreateOutputData:
    user_name: str
    created: datetime

    def __init__(self, usre_id: int, created: datetime) -> None:
        self.usre_id = usre_id
        self.created = created
