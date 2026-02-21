"""Strategy pattern: select an algorithm at runtime."""


def sort_by_name(items):
    """Sort items alphabetically by name."""
    return sorted(items, key=lambda x: x["name"])


def sort_by_price(items):
    """Sort items by price ascending."""
    return sorted(items, key=lambda x: x["price"])


def sort_by_rating(items):
    """Sort items by rating descending."""
    return sorted(items, key=lambda x: x["rating"], reverse=True)


def display(items, strategy):
    """Display items sorted using the given strategy function."""
    print(f"Strategy: {strategy.__name__}")
    for item in strategy(items):
        print(f"  {item['name']:>10} | ${item['price']:.2f} | {item['rating']}*")
    print()


if __name__ == "__main__":
    products = [
        {"name": "Widget", "price": 9.99, "rating": 4},
        {"name": "Gadget", "price": 24.99, "rating": 5},
        {"name": "Doohickey", "price": 4.50, "rating": 3},
    ]
    for strat in (sort_by_name, sort_by_price, sort_by_rating):
        display(products, strat)
