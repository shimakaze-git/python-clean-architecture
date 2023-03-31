from dataclasses import dataclass


@dataclass
class UserCreateViewModel:
    """
    あえて文字列型のcreate_dateを入れることで、入力部や出力部では文字列型として扱うことを意味する。
    """

    user_id: str
    create_date: str
