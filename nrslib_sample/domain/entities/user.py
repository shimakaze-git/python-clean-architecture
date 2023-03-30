import uuid

from dataclasses import dataclass


# (frozen=True, eq=True)
@dataclass
class User:
    identifier: str | None = None
    name: str = ""

    def __init__(self, identifier: str | None = None, name: str = "") -> None:
        if (not identifier) and (name):
            self.identifier = str(uuid.uuid4())
            self.name = name

        if identifier and name:
            self.identifier = identifier
            self.name = name
