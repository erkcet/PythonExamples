"""Basic logging setup and usage."""

import logging


def setup_logging():
    """Configure basic logging."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )
    return logging.getLogger(__name__)


def process_order(logger, order_id, amount):
    """Simulate processing an order with logging."""
    logger.info("Processing order %s for $%.2f", order_id, amount)
    if amount <= 0:
        logger.error("Invalid amount: %.2f", amount)
        return False
    if amount > 10000:
        logger.warning("Large order detected: $%.2f", amount)
    logger.debug("Order %s validated successfully", order_id)
    logger.info("Order %s completed", order_id)
    return True


if __name__ == "__main__":
    logger = setup_logging()
    logger.info("Application starting")
    process_order(logger, "A001", 150.00)
    process_order(logger, "A002", 25000.00)
    process_order(logger, "A003", -10.00)
    logger.info("Application finished")
