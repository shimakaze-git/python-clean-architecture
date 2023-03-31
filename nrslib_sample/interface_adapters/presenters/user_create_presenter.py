from datetime import datetime

from nrslib_sample.interface_adapters.user_create_view_model import UserCreateViewModel
from nrslib_sample.use_cases.interfaces.interface_user_create_presenter import InterfaceUserCreatePresenter
from nrslib_sample.use_cases.user_create_output_data import UserCreateOutputData

from nrslib_sample.interface_adapters.user_create_subject import UserCreateSubject


class UserCreatePresenter(InterfaceUserCreatePresenter):
    """"""

    subject: UserCreateSubject

    def __init__(self, subject: UserCreateSubject) -> None:
        self.subject = subject

    def complete(self, output_data: UserCreateOutputData) -> None:
        """"""

        user_id: str = output_data.user_id
        created_date: datetime = output_data.created

        created_date_text: str = created_date.strftime("%Y/%m/%d")

        model: UserCreateViewModel = UserCreateViewModel(user_id, created_date_text)
        self.subject.view_model = model
