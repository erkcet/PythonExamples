"""Interactive text menu using input() and a dispatch loop."""


def show_menu():
    """Display the menu options."""
    print("\n=== Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Quit")


def get_numbers() -> tuple:
    """Prompt user for two numbers."""
    a = float(input("  First number:  "))
    b = float(input("  Second number: "))
    return a, b


def run_menu():
    """Main menu loop dispatching to operations."""
    actions = {
        "1": ("Add", lambda a, b: a + b),
        "2": ("Subtract", lambda a, b: a - b),
        "3": ("Multiply", lambda a, b: a * b),
    }
    while True:
        show_menu()
        choice = input("Choose [1-4]: ").strip()
        if choice == "4":
            print("Goodbye!")
            break
        if choice in actions:
            name, func = actions[choice]
            a, b = get_numbers()
            print(f"  {name}: {func(a, b)}")
        else:
            print("  Invalid choice, try again.")


if __name__ == "__main__":
    run_menu()
