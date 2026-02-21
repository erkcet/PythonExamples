"""Basic argparse usage for command-line argument parsing."""

import argparse


def create_parser() -> argparse.ArgumentParser:
    """Build and return the argument parser."""
    parser = argparse.ArgumentParser(description="Greet a user")
    parser.add_argument("name", help="Name of the person to greet")
    parser.add_argument("-c", "--count", type=int, default=1,
                        help="Number of times to greet (default: 1)")
    parser.add_argument("-u", "--uppercase", action="store_true",
                        help="Print greeting in uppercase")
    return parser


def greet(name: str, count: int, uppercase: bool):
    """Print a greeting the specified number of times."""
    msg = f"Hello, {name}!"
    if uppercase:
        msg = msg.upper()
    for _ in range(count):
        print(msg)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    greet(args.name, args.count, args.uppercase)
