from dataclasses import dataclass


@dataclass
class UserCreateInputData:
    """ DTO (Data Transfer Object) """
    user_name: str
