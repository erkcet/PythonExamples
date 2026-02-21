"""Check if a string of parentheses is valid (properly opened and closed)."""


def is_valid(s):
    """Return True if all parentheses are balanced and properly nested."""
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    tests = ["()", "()[]{}", "(]", "([)]", "{[]}", "((()))", ""]
    for t in tests:
        display = t if t else "<empty>"
        print(f"'{display}' -> valid: {is_valid(t)}")
