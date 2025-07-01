import json
import os
import sys

import constants
import functions as func
import utilities as utils


def main() -> None:
    # Checking if the file exists
    if not os.path.exists(constants.FILE_PATH):
        # Create a new JSON file with the specified structure
        with open(constants.FILE_PATH, "w") as f:
            json.dump({"tasks": []}, f)

    # Read the contents of the JSON file
    with open(constants.FILE_PATH, "r") as f:
        data = json.load(f)

        # loading the data into a list
        task_list = [item for item in data["tasks"]]
        _id = utils.initial_id(task_list)

    ## Match case to the different arguments
    match sys.argv[1]:
        # Adding a new task to the list
        case "add":
            _id, _task = func.add_task(_id, sys.argv[2])
            task_list.append(_task)
            print(f"Task added: {_task}")

        # Updating the description of the task based on an ID
        case "update":
            search_id = int(sys.argv[2])
            # Get the task with id
            task = next(filter(lambda t: t["id"] == search_id, task_list))
            # Update the description of the task and the updated at
            task["description"] = sys.argv[3]
            task["updatedAt"] = utils.updatedTime()
            print(f'Task updated {[t for t in task_list if t["id"] == search_id][0]}')

        # Deleting the task with the specified Id
        case "delete":
            search_id = int(sys.argv[2])
            # Get the task with id
            task = next(filter(lambda t: t["id"] == search_id, task_list))
            # Delete the task with the specified id
            for index, value in enumerate(task_list):
                if value == task:
                    del task_list[index]
                    break
            print(f"Task deleted")

        # Updating the status
        case "mark-in-progress" | "mark-done":
            search_id = int(sys.argv[2])
            # Get the task with id
            task = next(filter(lambda t: t["id"] == search_id, task_list))
            # Update the status of the task and the updated at
            if sys.argv[1] == "mark-in-progress":
                task["status"] = constants.TASK_STATUS[
                    1
                ]  # resolves to "in-progress" status
            elif sys.argv[1] == "mark-done":
                task["status"] = constants.TASK_STATUS[2]  # resolves to "done" status
            task["updatedAt"] = utils.updatedTime()
            print(
                f'Task status updated {[t for t in task_list if t["id"] == search_id][0]}'
            )

        # bringing a list of tasks depending on the filter
        case "list":
            try:
                # filter when
                if sys.argv[2] == "in-progress":
                    _to_print = [
                        t for t in task_list if t["status"] == constants.TASK_STATUS[2]
                    ]  # resolves to "in-progress" status
                elif sys.argv[2] == "done":
                    _to_print = [
                        t for t in task_list if t["status"] == constants.TASK_STATUS[2]
                    ]  # resolves to "done" status
                else:
                    _to_print = task_list

            except IndexError:
                _to_print = task_list

            # printing the tasks one by one
            for i in _to_print:
                print(i)

        case _:
            raise ValueError(
                "Invalid command please use (add/update/delete/mark-in-progress/mark-done)"
            )

    ##################################################
    # Writing back to task json
    with open(constants.FILE_PATH, "w") as f:
        json.dump({"tasks": task_list}, f)


# sys args
if __name__ == "__main__":
    main()
