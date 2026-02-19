class NegativeAgeError(Exception):
    pass

def set_age(age: int) -> None:
    if age < 0:
        raise NegativeAgeError("age cannot be negative")

set_age(10)
print("age is valid")
