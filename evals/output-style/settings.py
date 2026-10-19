import os


def retry_settings():
    # Load retry settings from environment variables.
    attempts = int(os.environ.get("RETRY_ATTEMPTS", "3"))
    delay = float(os.environ.get("RETRY_DELAY", "1"))
    return attempts, delay
