from abc import ABCMeta, abstractmethod
from nrslib_sample.use_cases.user.user_create_input_data import UserCreateInputData


class InterfaceUserCreateUseCase(ABCMeta):
    """"""

    @abstractmethod
    def handle(self, input_data: UserCreateInputData) -> None:
        raise NotImplementedError
