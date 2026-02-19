class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

    @classmethod
    def total_users(cls):
        return cls.count

    @staticmethod
    def is_valid_name(name):
        return len(name) >= 2

User("Ava")
User("Noah")
print(User.total_users(), User.is_valid_name("Li"))
