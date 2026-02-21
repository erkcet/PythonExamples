"""Custom metaclass that modifies class creation."""


class UpperAttrMeta(type):
    """Metaclass that converts all attributes to uppercase."""

    def __new__(mcs, name, bases, namespace):
        upper_attrs = {}
        for key, val in namespace.items():
            if not key.startswith("_"):
                upper_attrs[key.upper()] = val
            else:
                upper_attrs[key] = val
        return super().__new__(mcs, name, bases, upper_attrs)


class LoggedMeta(type):
    """Metaclass that logs class creation and method calls."""

    def __new__(mcs, name, bases, namespace):
        print(f"  Creating class: {name}")
        for key, val in namespace.items():
            if callable(val) and not key.startswith("_"):
                namespace[key] = mcs._wrap(key, val)
        return super().__new__(mcs, name, bases, namespace)

    @staticmethod
    def _wrap(name, method):
        def wrapper(*args, **kwargs):
            print(f"    Calling {name}()")
            return method(*args, **kwargs)
        return wrapper


class MyConfig(metaclass=UpperAttrMeta):
    debug = True
    version = "1.0"


class Service(metaclass=LoggedMeta):
    def process(self):
        return "done"


if __name__ == "__main__":
    print(f"MyConfig.DEBUG: {MyConfig.DEBUG}")
    print(f"MyConfig.VERSION: {MyConfig.VERSION}")
    print(f"Has 'debug': {hasattr(MyConfig, 'debug')}")
    svc = Service()
    svc.process()
