from dataclasses import dataclass

@dataclass
class Student:
    name: str
    grade: int

s = Student("Mina", 10)
print(s)
