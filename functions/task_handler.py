import constants
import utilities as utils


# adding a task to the list
def add_task(id, description: str) -> dict:
    """Adds a new task to the list.

    Args:
        description (str): The description of the task.

    Returns: A list with 2 values
        int: New ID incremented by 1 so there are no conflicts
        dict: A dictionary with the following keys:
            id (int): The ID of the task.
            description (str): The description of the task.
            status (str): The current status of the task, resolves to "add" status using @constants.TASK_STATUS[0].
            createdAt (datetime): The date and time the task was created, using @utils.updatedTime().
            updatedAt (datetime): The date and time the task was last updated, using @utils.updatedTime().
    """
    _id = id + 1
    return [
        _id,
        {
            "id": _id,
            "description": description,
            "status": constants.TASK_STATUS[0],  # resolves to "todo" status
            "createdAt": utils.updatedTime(),
            "updatedAt": utils.updatedTime(),
        },
    ]


# update description
def update_task(description):
    """Update the task description and return the updated timestamp."""
    return description, utils.updatedTime()
