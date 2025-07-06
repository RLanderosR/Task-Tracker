import sys


def exit_program(exit_status: int) -> None:
    """
    Exit the program with a status code and print an appropriate message.

    Args:
        exit_status (int): The status code to use when exiting the program. Valid codes are:
            - 0: Task list updated.
            - 1: Task does not exist, please check the ID.
            - 2: Please add the description you want to add.
            - 3: Please add the description you want to change.
            - 4: Status is not recognized, please check status.
            - 5: Invalid command please use (add/update/delete/mark-in-progress/mark-done).

    The function matches the exit status to a predefined message, prints it,
    and then exits the program using sys.exit(). If the exit_status does not match
    any of the expected values, the message will be "Unknown error number".
    """
    match exit_status:
        case 0:
            message = "Task list updated."
        case 1:
            message = "Task does not exist, please check the ID."
        case 2:
            message = "Please add the description you want to add."
        case 3:
            message = "Please add the description you want to change."
        case 4:
            message = "Status is not recognized, please check status."
        case 5:
            message = "Invalid command please use (add/update/delete/mark-in-progress/mark-done)."
        case _:
            message = "Unknown error number"
    print(message)
    print("Exiting the program...")
    sys.exit(exit_status)
