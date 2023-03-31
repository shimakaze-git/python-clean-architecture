import uuid
from datetime import datetime

from nrslib_sample.interface_adapters.presenters.user_create_presenter import UserCreatePresenter
from nrslib_sample.interface_adapters.user_create_subject import UserCreateSubject

from nrslib_sample.use_cases.user_create_output_data import UserCreateOutputData


def test_startup():
    subject: UserCreateSubject = UserCreateSubject()
    presenter: UserCreatePresenter = UserCreatePresenter(subject)

    user_id: str = str(uuid.uuid4())
    now: datetime = datetime.now()

    user_create_output_data: UserCreateOutputData = UserCreateOutputData(user_id, now)
    presenter.complete(output_data=user_create_output_data)

    assert presenter.subject.view_model.create_date == now.strftime("%Y/%m/%d")
    assert presenter.subject.view_model.user_id == user_id
