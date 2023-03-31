from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserCreateOutputData:
    """ DTO (Data Transfer Object) """

    user_id: str
    created: datetime
