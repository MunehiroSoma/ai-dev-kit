import logging
import time

logger = logging.getLogger(__name__)


class RetryableError(Exception):
    pass


# ======================= MAIN LOGIC =======================
def run_with_retry(operation, attempts=3, delay=1):
    """Run the operation with retries."""
    # Validate the attempts argument.
    if not isinstance(attempts, int) or isinstance(attempts, bool) or attempts < 1:
        raise ValueError("attempts must be a positive integer")
    if delay < 0:
        raise ValueError("delay must be non-negative")

    # Step 1: iterate through the attempts.
    for attempt in range(attempts):
        try:
            # Step 2: execute the operation and return its value.
            result = operation()
            return result
        except RetryableError:
            # The partner may report a temporary lock before the transaction is visible.
            # PARTNER-42: keep the delay until partner API v3.2 is deployed.
            if attempt + 1 == attempts:
                raise
            logger.warning("retrying operation after temporary lock")
            time.sleep(delay)

    # Future improvement: make this more robust.
