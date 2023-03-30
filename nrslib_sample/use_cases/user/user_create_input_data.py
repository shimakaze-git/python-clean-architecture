class UserCreateInputData:
    user_name: str

    def __init__(self, user_name: str) -> None:
        """ DTO (Data Transfer Object) """
        self.user_name = user_name
