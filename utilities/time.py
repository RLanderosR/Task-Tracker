from datetime import datetime


def updatedTime() -> str:
    """Returns the current datetime in the format YYYY-MM-DD HH:MM:SS."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
