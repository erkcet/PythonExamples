# PythonExamples

A comprehensive collection of **578+ Python examples** covering 45 topic categories — from beginner fundamentals to advanced algorithms and design patterns.

## Repository Structure

### Root Examples (100 files)

The repository root contains 100 standalone Python scripts covering foundational topics:

- 29 original examples (e.g., `factorial.py`, `counter.py`, `even_numbers.py`)
- 71 numbered examples (`example_030_*.py` to `example_100_*.py`) covering strings, comprehensions, functions, OOP, algorithms, stdlib tools, and more

### Categorized Examples (`examples/` directory — 478 files)

The `examples/` directory organizes scripts into 45 topic-based subdirectories:

| Category | Files | Description |
|---|---|---|
| `strings/` | 45 | String manipulation, parsing, encoding, ciphers |
| `text_processing/` | 20 | Word frequency, formatting, translators, diffs |
| `numbers/` | 15 | Primes, Fibonacci, base conversion, digital root |
| `lists/` | 15 | Slicing, rotation, two-pointer, sliding window |
| `dictionaries/` | 15 | defaultdict, Counter, LRU cache, sparse matrix |
| `data_structures/` | 15 | Stack, queue, linked list, BST, trie, heap |
| `classes/` | 15 | Inheritance, MRO, descriptors, magic methods |
| `functions/` | 12 | Closures, higher-order, currying, dispatch |
| `file_operations/` | 12 | Read/write, CSV, JSON, pathlib, temp files |
| `design_patterns/` | 12 | Singleton, factory, observer, strategy, state |
| `itertools_functools/` | 12 | chain, groupby, accumulate, lru_cache, reduce |
| `sorting_algorithms/` | 10 | Bubble, merge, quick, heap, radix, counting |
| `searching_algorithms/` | 8 | Binary, jump, interpolation, rotated array |
| `recursion/` | 10 | Hanoi, N-Queens, flood fill, permutations |
| `dynamic_programming/` | 10 | Knapsack, LCS, coin change, edit distance |
| `graph_algorithms/` | 10 | BFS, DFS, Dijkstra, MST, topological sort |
| `tree_algorithms/` | 8 | Traversals, height, LCA, serialize, invert |
| `bitwise_operations/` | 10 | Bit tricks, flags, Hamming weight, XOR |
| `statistics_random/` | 10 | Mean/median, Monte Carlo, histograms |
| `regex/` | 10 | Matching, groups, lookahead, log parsing |
| `datetime_ops/` | 10 | Formatting, timezones, business days, age calc |
| `collections_module/` | 10 | namedtuple, deque, Counter, ChainMap |
| `comprehensions/` | 10 | List, dict, set, generator, walrus operator |
| `sets_and_tuples/` | 10 | Set ops, frozenset, namedtuple, pair sum |
| `decorators/` | 10 | Timing, retry, memoize, chaining, validation |
| `generators/` | 10 | Yield, send, yield from, pipelines, coroutines |
| `error_handling/` | 10 | Custom exceptions, chaining, suppress, recovery |
| `context_managers/` | 8 | Timer, temp dir, redirect, resource pool |
| `logging_debugging/` | 8 | Logging levels, formatters, profiling, timing |
| `type_hints/` | 8 | Generics, Protocol, TypedDict, Callable |
| `testing/` | 8 | unittest, doctest, mock, parametrize |
| `cli_tools/` | 8 | argparse, menus, progress bars, ANSI color |
| `networking/` | 8 | HTTP, URL parsing, IP addresses, base64 |
| `async_programming/` | 8 | async/await, gather, queues, async generators |
| `os_and_system/` | 8 | Environment, subprocess, platform, os.walk |
| `cryptography/` | 6 | Hashing, HMAC, tokens, UUID, XOR cipher |
| `dataclasses_attrs/` | 6 | Frozen, field options, post_init, slots |
| `database/` | 6 | SQLite CRUD, transactions, aggregation |
| `enums/` | 5 | IntEnum, Flag, auto(), enum methods |
| `metaclasses/` | 5 | Custom metaclass, registry, singleton |
| `json_csv_data/` | 8 | JSON encode/decode, CSV reader, transforms |
| `math_puzzles/` | 8 | FizzBuzz, Pascal's triangle, matrix ops |
| `string_algorithms/` | 8 | KMP, Rabin-Karp, Z-algorithm, wildcards |
| `array_algorithms/` | 8 | Two sum, merge intervals, majority element |
| `useful_snippets/` | 10 | Retry, memoize, rate limiter, event emitter |

## Quick Start

Run any example directly:

```bash
# Root examples
python3 factorial.py
python3 example_033_list_comprehension.py

# Categorized examples
python3 examples/sorting_algorithms/04_merge_sort.py
python3 examples/dynamic_programming/05_coin_change.py
python3 examples/design_patterns/05_observer.py
```

All examples are self-contained, use only the Python standard library, and include a runnable `if __name__ == "__main__"` demo block.
