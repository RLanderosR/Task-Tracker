def initial_id(tasks: dict) -> int:
    """
    Returns the initial _id value for a new task.

    The initial _id is determined by either:
    1. Taking the last task's _id, or
    2. Returning an id of 0 if the list is empty.

    :param tasks: A list of tasks.
    :return: An integer representing the initial _id for a new task.
    """
    # setting the task _id to the last task
    try:
        _id = int(list(tasks.keys())[-1])
        return _id

    # list is empty (new list), so return an id of 0
    except (IndexError, AttributeError):
        return 0
