from datetime import datetime

from nrslib_sample.use_cases.interfaces.interface_user_create_use_case import InterfaceUserCreateUseCase
from nrslib_sample.use_cases.interfaces.interface_user_create_presenter import InterfaceUserCreatePresenter
from nrslib_sample.use_cases.user_create_input_data import UserCreateInputData
from nrslib_sample.use_cases.user_create_output_data import UserCreateOutputData
from nrslib_sample.domain.interfaces.interface_user_repository import InterfaceUserRepository

from nrslib_sample.domain.entities import User


class UserCreateInteractor(InterfaceUserCreateUseCase):
    """"""

    _user_repository: InterfaceUserRepository
    _presenter: InterfaceUserCreatePresenter

    # def __new__(cls, user_repository: InterfaceUserRepository, presenter: IUserCreatePresenter):
    #     return super().__new__(cls)

    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(cls)

    def __init__(self, user_repository: InterfaceUserRepository, presenter: InterfaceUserCreatePresenter) -> None:

        self._user_repository = user_repository
        self._presenter = presenter

    # def __post_init__(self):
    #     self.full_name = ' '.join([self.first_name, self.last_name])

    def handle(self, input_data: UserCreateInputData) -> None:
        user_name: str = input_data.user_name
        print("user_name", user_name)

        duplicate_user: User = self._user_repository.find_by_user_name(user_name)
        if duplicate_user:
            raise Exception("duplicated")

        user: User = User(name=user_name)
        self._user_repository.save(user)

        output_data: UserCreateOutputData = UserCreateOutputData(user.identifier, datetime.now())
        self._presenter.complete(output_data)
