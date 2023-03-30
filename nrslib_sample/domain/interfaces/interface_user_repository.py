from abc import ABCMeta, abstractmethod

from nrslib_sample.domain.entities.user import User


class InterfaceUserRepository(ABCMeta):
    """"""

    @abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_by_user_name(self, user_name: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> list[User]:
        raise NotImplementedError
