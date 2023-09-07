import dataclasses
import uuid
from dataclasses import dataclass, field


def generate_id():
    return str(uuid.uuid4())


@dataclass(kw_only=True, slots=True, order=True)
class Person:
    first_name: str
    last_name: str
    age: int
    active: bool = True
    hobbies: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _full_name: str = field(init=False, repr=False)

    @property
    def full_name(self):
        return self._full_name

    def __post_init__(self):
        self._full_name = f"{self.first_name} {self.last_name}"

    def __str__(self):
        return dataclasses.asdict(self).__str__()


if __name__ == "__main__":
    one_person = Person(first_name="John", last_name="Doe", age=30)
    one_person.hobbies.append("reading")
    print(one_person)

    other_person = Person(
        first_name="Jane", last_name="Doe", age=28, active=False, hobbies=["swimming"]
    )
    print(other_person)
