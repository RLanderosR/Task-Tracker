import sys


def exit_program(exit_status: int) -> None:
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
