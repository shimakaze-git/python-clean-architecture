from domain.interfaces.interface_user_repository import InterfaceUserRepository
from domain.entities.user import User


class InMemoryUserRepository(InterfaceUserRepository):
    """"""

    _data: dict[str, User] = {}

    def save(self, user: User) -> None:
        """"""
        self._data[user.identifier] = self.clone_user(user)

    def find_by_user_name(self, user_name: str) -> User:
        """"""
        user_name_list: list[str] = list(map(lambda user: user.name, self.find_all()))

        index_key: int = user_name_list.index(user_name)
        return self.find_all()[index_key]

    def find_all(self) -> list[User]:
        """"""
        return list(self._data.values())

    def clone_user(self, user: User) -> User:
        """"""
        return User(user.identifier, user.name)
