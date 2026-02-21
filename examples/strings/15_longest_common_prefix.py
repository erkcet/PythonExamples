"""Find the longest common prefix among a list of strings."""


def longest_common_prefix(strs):
    """Return the longest prefix shared by all strings."""
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == "__main__":
    groups = [
        ["flower", "flow", "flight"],
        ["interspecies", "interstellar", "interstate"],
        ["dog", "racecar", "car"],
        ["prefix", "preface", "prevent"],
    ]
    for words in groups:
        result = longest_common_prefix(words)
        print(f"{words} -> prefix: '{result}'")
