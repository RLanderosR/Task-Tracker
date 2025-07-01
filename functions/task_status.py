import constants
import utilities


def update_task_status(status):
    """
    Updates the task status based on the given status parameter.

    The status parameter can be one of the following values: "add", "update", or "delete".
    If the status parameter is not one of these values, an error message will be printed and the function will return None.

    Returns:
        - (status, updated_time) if the status parameter is valid
        - None if the status parameter is invalid
    """
    if status in constants.TASK_STATUS:
        return status, utilities.updatedTime()
    else:
        print(f"Invalid Status ({constants.TASK_STATUS})")
