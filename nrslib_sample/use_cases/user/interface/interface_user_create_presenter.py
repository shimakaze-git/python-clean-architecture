from abc import ABCMeta, abstractmethod
from nrslib_sample.use_cases.user.user_create_output_data import UserCreateOutputData


class InterfaceUserCreateUseCase(ABCMeta):
    """"""

    @abstractmethod
    def handle(self, output_data: UserCreateOutputData) -> None:
        raise NotImplementedError
