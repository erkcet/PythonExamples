"""Demonstrating *args and **kwargs for flexible function signatures."""


def sum_all(*args):
    """Sum any number of positional numeric arguments."""
    return sum(args)


def build_tag(tag, *children, **attrs):
    """Build an HTML-like tag string with children and attributes."""
    attr_str = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    opening = f"<{tag} {attr_str}>" if attr_str else f"<{tag}>"
    body = "".join(str(c) for c in children)
    return f"{opening}{body}</{tag}>"


def proxy_call(func, *args, **kwargs):
    """Call a function, printing its arguments first."""
    print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
    return func(*args, **kwargs)


if __name__ == "__main__":
    print(sum_all(1, 2, 3, 4, 5))
    print(build_tag("div", "Hello", "World", id="main", role="content"))
    result = proxy_call(sum_all, 10, 20, 30)
    print(f"Result: {result}")
