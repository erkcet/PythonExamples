"""Using bit fields as flags for permission management."""

# Define permission flags
READ = 1 << 0    # 0001
WRITE = 1 << 1   # 0010
EXECUTE = 1 << 2 # 0100
ADMIN = 1 << 3   # 1000

FLAG_NAMES = {READ: "READ", WRITE: "WRITE", EXECUTE: "EXECUTE", ADMIN: "ADMIN"}


def has_permission(flags: int, perm: int) -> bool:
    """Check if a permission is set."""
    return bool(flags & perm)


def add_permission(flags: int, perm: int) -> int:
    """Add a permission flag."""
    return flags | perm


def remove_permission(flags: int, perm: int) -> int:
    """Remove a permission flag."""
    return flags & ~perm


def describe_permissions(flags: int) -> list[str]:
    """Return list of active permission names."""
    return [name for flag, name in FLAG_NAMES.items() if flags & flag]


if __name__ == "__main__":
    perms = READ | WRITE
    print(f"Initial: {describe_permissions(perms)} ({perms:04b})")
    perms = add_permission(perms, EXECUTE)
    print(f"+ EXEC:  {describe_permissions(perms)} ({perms:04b})")
    perms = remove_permission(perms, WRITE)
    print(f"- WRITE: {describe_permissions(perms)} ({perms:04b})")
    print(f"\nHas READ?  {has_permission(perms, READ)}")
    print(f"Has ADMIN? {has_permission(perms, ADMIN)}")
