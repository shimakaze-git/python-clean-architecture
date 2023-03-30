from datetime import datetime


class UserCreateOutputData:
    usre_id: str
    created: datetime

    def __init__(self, usre_id: str, created: datetime) -> None:
        self.usre_id = usre_id
        self.created = created
