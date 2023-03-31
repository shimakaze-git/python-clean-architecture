from abc import ABCMeta, abstractmethod
from use_cases.user.user_create_output_data import UserCreateOutputData


class InterfaceUserCreatePresenter(metaclass=ABCMeta):
    """"""

    @abstractmethod
    def complete(self, output_data: UserCreateOutputData) -> None:
        raise NotImplementedError
