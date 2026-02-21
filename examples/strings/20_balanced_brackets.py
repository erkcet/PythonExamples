"""Check if brackets in an expression are balanced, ignoring other characters."""


def is_balanced(expr):
    """Return True if all bracket types in the expression are balanced."""
    stack = []
    openers = set("({[")
    closers = {')': '(', '}': '{', ']': '['}
    for ch in expr:
        if ch in openers:
            stack.append(ch)
        elif ch in closers:
            if not stack or stack[-1] != closers[ch]:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    expressions = [
        "func(a[0], {b: c})",
        "arr[i + (j * k)]",
        "((missing closing)",
        "{[()]}{[()]}",
    ]
    for expr in expressions:
        print(f"'{expr}' -> balanced: {is_balanced(expr)}")
