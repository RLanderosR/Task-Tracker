def initial_id(tasks: list) -> int:
    """
    Returns the initial _id value for a new task.

    The initial _id is determined by either:
    1. Taking the last task's _id and adding 1, or
    2. Returning an id of 1 if the list is empty.

    :param tasks: A list of tasks.
    :return: An integer representing the initial _id for a new task.
    """
    # setting the task _id to the last task + 1
    try:
        _id = tasks[-1]["id"]
        return _id

    # list is empty (new list), so return an id of 1
    except IndexError:
        return 1
