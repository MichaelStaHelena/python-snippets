import dataclasses
import uuid
from dataclasses import dataclass, field

from example import Person


def generate_id():
    return str(uuid.uuid4())


@dataclass(kw_only=True, slots=True, order=True)
class Subject:
    name: str
    code: str
    credits: int
    id: str = field(init=False, default_factory=generate_id)


@dataclass(kw_only=True, slots=True, order=True)
class Student(Person):
    course: str
    start_year: int
    subjects: list[Subject] = field(default_factory=list)


if __name__ == "__main__":
    one_student = Student(
        first_name="John",
        last_name="Doe",
        age=30,
        course="Computer Science",
        start_year=2019,
    )
    one_student.subjects.append(Subject(name="Math", code="MATH101", credits=4))
    one_student.subjects.append(Subject(name="English", code="ENG101", credits=4))
    one_student.subjects.append(Subject(name="Physics", code="PHY101", credits=4))
    print(one_student)
