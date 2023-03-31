from abc import ABCMeta, abstractmethod
from nrslib_sample.use_cases.user_create_output_data import UserCreateOutputData


class InterfaceUserCreatePresenter(metaclass=ABCMeta):
    """"""

    @abstractmethod
    def complete(self, output_data: UserCreateOutputData) -> None:
        raise NotImplementedError
