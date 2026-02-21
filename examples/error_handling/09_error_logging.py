"""Logging exceptions properly."""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def fetch_data(source):
    """Simulate fetching data that may fail."""
    if source == "bad":
        raise ConnectionError(f"Cannot connect to {source}")
    return [1, 2, 3]


def process_with_logging(source):
    """Process data with proper error logging."""
    logger.info("Starting processing for source=%s", source)
    try:
        data = fetch_data(source)
    except ConnectionError:
        logger.exception("Failed to fetch data from %s", source)
        return []
    logger.info("Fetched %d items", len(data))
    return data


def risky_operation():
    """Demonstrate logging vs re-raising."""
    try:
        result = 1 / 0
    except ZeroDivisionError:
        logger.error("Division by zero occurred", exc_info=True)
        return None


if __name__ == "__main__":
    print(f"Good source: {process_with_logging('good')}")
    print(f"Bad source: {process_with_logging('bad')}")
    risky_operation()
