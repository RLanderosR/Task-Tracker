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
        data = json.load(f)["tasks"]

        # loading the last id in the dict
        latest_id: int = utils.initial_id(data)

    ## Match case to the different arguments
    match sys.argv[1]:
        # Adding a new task to the list
        case "add":
            try:
                latest_id, _task = func.add_task(latest_id, sys.argv[2])
                data.update(_task)
                print(
                    f"Task added: {_task[latest_id]['description']}, with an ID of {latest_id}"
                )
                save_tasks(data)
            except IndexError:
                utils.exit_program(2)

        # Updating the description of the task based on an ID
        case "update":
            try:
                # Get the task Id and creating a temp task
                _search_id = sys.argv[2]
                _temp_task = data.get(_search_id)
                # updating the dict items
                _temp_task["description"], _temp_task["updatedAt"] = func.update_task(
                    sys.argv[3]
                )
                # returning the modified items to the original dict
                data.update({_search_id: _temp_task})
                print(f'Task updated: {_temp_task["description"]}')
                save_tasks(data)
            except TypeError:
                utils.exit_program(1)
            except IndexError:
                utils.exit_program(3)

        # Deleting the task with the specified Id
        case "delete":
            try:
                _search_id = sys.argv[2]
                # Delete the task with the specified id
                data.pop(_search_id)
                print(f"Task deleted")
                save_tasks(data)
            except KeyError:
                utils.exit_program(1)

        # Updating the status
        case "mark-in-progress" | "mark-done":
            try:
                # Get the task Id and creating a temp task
                _search_id = sys.argv[2]
                _temp_task = data.get(_search_id)
                # Update the status of the task and the updated at
                if sys.argv[1] == "mark-in-progress":
                    _temp_task["status"] = constants.TASK_STATUS[
                        1
                    ]  # resolves to "in-progress" status
                elif sys.argv[1] == "mark-done":
                    _temp_task["status"] = constants.TASK_STATUS[
                        2
                    ]  # resolves to "done" status
                _temp_task["updatedAt"] = utils.updatedTime()
                # returning the modified items to the original dict
                data.update({_search_id: _temp_task})
                print(
                    f'Task with ID: {_search_id}, status updated to: {_temp_task["status"]}'
                )
                save_tasks(data)
            except TypeError:
                utils.exit_program(1)

        # bringing a list of tasks depending on the filter
        case "list":
            _to_print = [["ID", "Description", "Status", "Created At", "Updated At"]]
            try:
                # retrieving status
                _search_status = sys.argv[2]

                # run a valid check on the task
                if _search_status in constants.TASK_STATUS:
                    pass
                else:
                    utils.exit_program(4)

                # loop and filter the list based on the status
                for key, task in data.items():
                    if sys.argv[2] == task["status"]:
                        _to_print.append(
                            [
                                key,
                                task["description"],
                                task["status"],
                                task["createdAt"],
                                task["updatedAt"],
                            ]
                        )

            except IndexError:
                for key, task in data.items():
                    _to_print.append(
                        [
                            key,
                            task["description"],
                            task["status"],
                            task["createdAt"],
                            task["updatedAt"],
                        ]
                    )

            # printing the tasks
            for row in _to_print:
                print("| {:3} | {:<50} | {:<11} | {:<21} | {:<21} |".format(*row))

        case _:
            utils.exit_program(5)


def save_tasks(tasks: dict) -> None:
    # Writing back to task json
    with open(constants.FILE_PATH, "w") as f:
        json.dump({"tasks": tasks}, f)
        utils.exit_program(0)


# sys args
if __name__ == "__main__":
    main()
