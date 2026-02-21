"""Custom log formatters."""

import logging


def make_logger(name, fmt_string):
    """Create a logger with a custom format."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(fmt_string))
    logger.addHandler(handler)
    return logger


def demo_formats():
    """Show various log format styles."""
    formats = {
        "simple": "%(levelname)s: %(message)s",
        "timed": "%(asctime)s %(levelname)s: %(message)s",
        "detailed": "[%(name)s:%(lineno)d] %(levelname)-8s %(message)s",
        "json-like": '{"level":"%(levelname)s","msg":"%(message)s","func":"%(funcName)s"}',
    }
    for name, fmt in formats.items():
        logger = make_logger(name, fmt)
        print(f"\n--- {name} format ---")
        logger.info("User logged in")
        logger.warning("Disk usage at 90%%")
        logger.error("Connection timeout")


if __name__ == "__main__":
    demo_formats()
