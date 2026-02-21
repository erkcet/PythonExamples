"""File and stream logging handlers."""

import logging
import tempfile
import os


def setup_multi_handler_logger(log_file):
    """Create logger with both file and stream handlers."""
    logger = logging.getLogger("multi")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    stream_h = logging.StreamHandler()
    stream_h.setLevel(logging.WARNING)
    stream_h.setFormatter(logging.Formatter("CONSOLE %(levelname)s: %(message)s"))

    file_h = logging.FileHandler(log_file)
    file_h.setLevel(logging.DEBUG)
    file_h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))

    logger.addHandler(stream_h)
    logger.addHandler(file_h)
    return logger


if __name__ == "__main__":
    log_path = os.path.join(tempfile.gettempdir(), "demo_app.log")
    logger = setup_multi_handler_logger(log_path)

    logger.debug("Debug detail - file only")
    logger.info("Info message - file only")
    logger.warning("Warning - both console and file")
    logger.error("Error - both console and file")

    print(f"\n--- File contents ({log_path}) ---")
    with open(log_path) as f:
        print(f.read())
    os.remove(log_path)
