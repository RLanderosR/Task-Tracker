import json
import os
import subprocess


def setup_test_file():
    """Setup a clean test file for each test case."""
    if os.path.exists("data/tasks.json"):
        os.remove("data/tasks.json")
    with open("data/tasks.json", "w") as f:
        json.dump({"tasks": {}}, f)


def run_command(cmd):
    """Run a command and return the output."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr


def test_add_task():
    setup_test_file()
    stdout, _ = run_command("python main.py add 'Test Task'")
    assert "Task added" in stdout


def test_update_task():
    setup_test_file()
    run_command("python main.py add 'Test Task'")

    stdout, _ = run_command("python main.py update 1 'Updated Task'")
    assert "Task updated" in stdout


def test_mark_in_progress():
    setup_test_file()
    run_command("python main.py add 'Test Task'")

    stdout, _ = run_command("python main.py mark-in-progress 1")
    assert "status updated to" in stdout


def test_mark_done():
    setup_test_file()
    run_command("python main.py add 'Test Task'")

    stdout, _ = run_command("python main.py mark-done 1")
    assert "status updated to" in stdout


def test_list_tasks():
    setup_test_file()
    run_command("python main.py add 'Test Task'")

    stdout, _ = run_command("python main.py list")
    assert "Test Task" in stdout


def test_delete_task():
    setup_test_file()
    run_command("python main.py add 'Test Task'")

    stdout, _ = run_command("python main.py delete 1")
    assert "Task deleted" in stdout


def test_invalid_command():
    setup_test_file()
    stderr, _ = run_command("python main.py invalid")
    assert "Invalid command" in stderr


if __name__ == "__main__":
    test_add_task()
    test_update_task()
    test_mark_in_progress()
    test_mark_done()
    test_list_tasks()
    test_delete_task()
    test_invalid_command()
    print("All tests passed!")
