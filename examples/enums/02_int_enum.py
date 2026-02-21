"""IntEnum for enums that behave like integers."""

from enum import IntEnum


class HTTPStatus(IntEnum):
    """HTTP status codes as IntEnum."""
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500

    @property
    def is_success(self):
        return 200 <= self.value < 300

    @property
    def is_error(self):
        return self.value >= 400


class Priority(IntEnum):
    """Task priority levels (comparable and sortable)."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


if __name__ == "__main__":
    status = HTTPStatus.OK
    print(f"Status: {status}, value: {status.value}")
    print(f"Is success: {status.is_success}")
    print(f"Can compare: {HTTPStatus.OK < HTTPStatus.NOT_FOUND}")
    print(f"Math works: {HTTPStatus.OK + 1}")
    tasks = [(Priority.HIGH, "Deploy"), (Priority.LOW, "Docs"), (Priority.CRITICAL, "Fix bug")]
    for p, name in sorted(tasks, reverse=True):
        print(f"  [{p.name}] {name}")
