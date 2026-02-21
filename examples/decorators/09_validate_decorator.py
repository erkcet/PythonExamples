"""Input validation decorator for function arguments."""

from functools import wraps


def validate_types(**type_hints):
    """Decorator factory: validate argument types at runtime."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            code = func.__code__
            names = code.co_varnames[:code.co_argcount]
            all_args = dict(zip(names, args))
            all_args.update(kwargs)
            for name, expected in type_hints.items():
                if name in all_args and not isinstance(all_args[name], expected):
                    raise TypeError(
                        f"'{name}' must be {expected.__name__}, "
                        f"got {type(all_args[name]).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_types(name=str, age=int)
def create_user(name, age):
    """Create a user dict with validated inputs."""
    return {"name": name, "age": age}


if __name__ == "__main__":
    print(create_user("Alice", 30))
    try:
        create_user("Bob", "not_a_number")
    except TypeError as e:
        print(f"Validation error: {e}")
    try:
        create_user(123, 25)
    except TypeError as e:
        print(f"Validation error: {e}")
