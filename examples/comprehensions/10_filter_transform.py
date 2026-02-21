"""Complex filter and transform patterns with comprehensions."""


def pipeline(data, *funcs):
    """Apply a pipeline of functions via reduce-style comprehension."""
    from functools import reduce
    return reduce(lambda d, f: [f(x) for x in d], funcs, data)


def multi_filter(data, *predicates):
    """Keep items that satisfy all predicates."""
    return [x for x in data if all(p(x) for p in predicates)]


def group_transform(pairs):
    """Group by first element, transform second elements."""
    groups = {}
    for key, val in pairs:
        groups.setdefault(key, []).append(val)
    return {k: sorted(v) for k, v in groups.items()}


def batch_replace(text, replacements):
    """Apply multiple string replacements using comprehension fold."""
    from functools import reduce
    return reduce(lambda t, kv: t.replace(*kv), replacements.items(), text)


if __name__ == "__main__":
    nums = list(range(-5, 6))
    result = pipeline(nums, abs, lambda x: x * 2)
    print(f"Pipeline |x|*2: {result}")
    positive = lambda x: x > 0
    even = lambda x: x % 2 == 0
    small = lambda x: x < 20
    print(f"Multi-filter: {multi_filter(range(30), positive, even, small)}")
    pairs = [("a", 3), ("b", 1), ("a", 1), ("b", 2)]
    print(f"Grouped: {group_transform(pairs)}")
    text = "the quick brown fox"
    reps = {"quick": "slow", "brown": "white", "fox": "rabbit"}
    print(f"Replaced: {batch_replace(text, reps)}")
