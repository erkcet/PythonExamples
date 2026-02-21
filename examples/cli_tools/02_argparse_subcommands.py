"""Subcommands with argparse for git-style CLI tools."""

import argparse


def cmd_add(args):
    """Handle the 'add' subcommand."""
    print(f"Adding item: {args.item} (quantity: {args.quantity})")


def cmd_remove(args):
    """Handle the 'remove' subcommand."""
    print(f"Removing item: {args.item}")


def cmd_list(args):
    """Handle the 'list' subcommand."""
    print("Listing all items..." + (" (verbose)" if args.verbose else ""))


def build_parser() -> argparse.ArgumentParser:
    """Build parser with subcommands."""
    parser = argparse.ArgumentParser(description="Inventory manager")
    sub = parser.add_subparsers(dest="command", required=True)

    add_p = sub.add_parser("add", help="Add an item")
    add_p.add_argument("item")
    add_p.add_argument("-q", "--quantity", type=int, default=1)
    add_p.set_defaults(func=cmd_add)

    rm_p = sub.add_parser("remove", help="Remove an item")
    rm_p.add_argument("item")
    rm_p.set_defaults(func=cmd_remove)

    ls_p = sub.add_parser("list", help="List items")
    ls_p.add_argument("-v", "--verbose", action="store_true")
    ls_p.set_defaults(func=cmd_list)
    return parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
