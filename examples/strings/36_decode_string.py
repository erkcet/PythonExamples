"""Decode an encoded string like '3[a2[c]]' -> 'accaccacc'."""


def decode_string(s):
    """Decode a string with nested repeat patterns like k[encoded]."""
    stack = []
    current_str = ""
    current_num = 0
    for ch in s:
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        elif ch == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif ch == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += ch
    return current_str


if __name__ == "__main__":
    tests = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef", "10[a]"]
    for t in tests:
        print(f"'{t}' -> '{decode_string(t)}'")
