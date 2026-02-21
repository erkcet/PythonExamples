"""Demonstrate DEBUG, INFO, WARNING, ERROR, CRITICAL levels."""

import logging


def demonstrate_levels(logger):
    """Log at every standard level."""
    logger.debug("Detailed diagnostic info for developers")
    logger.info("General operational information")
    logger.warning("Something unexpected but not critical")
    logger.error("An error occurred, operation may have failed")
    logger.critical("System is in a critical state")


def filter_by_level():
    """Show how level filtering works."""
    for level in [logging.DEBUG, logging.WARNING, logging.ERROR]:
        name = logging.getLevelName(level)
        logger = logging.getLogger(f"filter_{name}")
        logger.setLevel(level)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(f"[{name} filter] %(levelname)s: %(message)s"))
        logger.addHandler(handler)
        logger.propagate = False
        print(f"\n--- Filter at {name} ---")
        demonstrate_levels(logger)


if __name__ == "__main__":
    print("=== All levels ===")
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)-8s: %(message)s", force=True)
    demonstrate_levels(logging.getLogger("all"))
    filter_by_level()
