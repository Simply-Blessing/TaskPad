import taskpad_func 
import os
import pytest 
import tempfile 
import datetime

@pytest.fixture(autouse=True)
def temp_tasks_file(monkeypatch):
    #create a temporary file to handle JSON
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        fake_file = tmp.name
    #replace tasks_file in taskpad with the fake file so nothing gets overriden
    monkeypatch.setattr(taskpad_func,"TASKS_FILE",fake_file)

    yield

    #cleaup after test
    if os.path.exists(fake_file):
        os.remove(fake_file)

def test_add_task():
    result = taskpad_func.add_task("Finish homework")
    tasks = taskpad_func.load_tasks()

    assert len(tasks) == 1 
    assert tasks[0]["description"] == "Finish homework"
    assert tasks[0]["status"] == "Todo"
    assert "Finish homework" in result

def test_update_track():
    taskpad_func.add_task("Buy flowers")
    result = taskpad_func.update_task(1,"Buy 2 flower bouquets")
    tasks = taskpad_func.load_tasks()
    
    assert tasks[0]["description"] == "Buy 2 flower bouquets"
    assert "Buy 2 flower bouquets" in result

def test_mark_in_progress():
    taskpad_func.add_task("Pack for university")
    result = taskpad_func.mark_in_progress(1)
    tasks = taskpad_func.load_tasks()

    assert tasks[0]["status"] == "In-Progress"
    assert "Pack for university" in result

def test_mark_done():
    taskpad_func.add_task("Stargazing on friday")
    result = taskpad_func.mark_done(1)
    tasks = taskpad_func.load_tasks()

    assert tasks[0]["status"] == "Done"
    assert "Stargazing on friday" in result

def test_delete():
    taskpad_func.add_task("Task to delete")
    result = taskpad_func.delete_task(1)
    tasks = taskpad_func.load_tasks()

    assert len(tasks) == 0
    assert "has been removed" in result


def test_list_task():
    tasks=[
        "Buy Strawberries",
        "Buy Melon",
        "Buy Shoes",
        "Buy Sandals",
        "Buy Salad"
    ]
    taskpad_func.add_task(tasks[0])
    taskpad_func.add_task(tasks[1])
    taskpad_func.mark_in_progress(2)
    taskpad_func.add_task(tasks[2])
    taskpad_func.mark_in_progress(3)
    taskpad_func.add_task(tasks[3])
    taskpad_func.mark_done(4)
    taskpad_func.add_task(tasks[4])
    taskpad_func.mark_done(5)
    
    result = taskpad_func.list_tasks()

    for task in tasks:
        assert task in result

    assert "ID" in result
    assert "Task" in result

def test_list_task_status():
    tasks=[
        "Buy Strawberries",
        "Buy Melon",
        "Buy Shoes",
        "Buy Sandals",
        "Buy Salad"
    ]
    taskpad_func.add_task(tasks[0])
    taskpad_func.add_task(tasks[1])
    taskpad_func.mark_in_progress(2)
    taskpad_func.add_task(tasks[2])
    taskpad_func.mark_in_progress(3)
    taskpad_func.add_task(tasks[3])
    taskpad_func.mark_done(4)
    taskpad_func.add_task(tasks[4])
    taskpad_func.mark_done(5)
    
    result = taskpad_func.list_tasks(status="Done")
    done_tasks = [tasks[3],tasks[4]]
    for task in done_tasks:
        assert task in result

    assert "ID" in result
    assert "Task" in result

def test_list_task_by_date():
    taskpad_func.save_tasks([])
    # Add tasks and manual createdAt dates
    tasks = [
        {"desc": "Go to the library", "created": "2021-10-15"},
        {"desc": "Fly to Spain", "created": "2023-07-29"},
        {"desc": "Watch Merlin", "created": "2025-06-25"},
    ]

    for i, task in enumerate(tasks):
        taskpad_func.add_task(task["desc"])
        # Manually overwrite createdAt for testing
        all_tasks = taskpad_func.load_tasks()
        all_tasks[i]["createdAt"] = task["created"]
        taskpad_func.save_tasks(all_tasks)

    # Filter by year 2024
    result = taskpad_func.list_tasks(created="2025-06-25")
    assert "Watch Merlin" in result
    assert "Fly to Spain" not in result
    assert "Go to the library" not in result

def test_list_task_by_year():
    taskpad_func.save_tasks([])
    # Add tasks and manual createdAt dates
    tasks = [
        {"desc": "Buy Strawberries", "created": "2023-05-01"},
        {"desc": "Buy Melon", "created": "2024-06-15"},
        {"desc": "Buy Shoes", "created": "2025-07-20"},
    ]

    for i, task in enumerate(tasks):
        taskpad_func.add_task(task["desc"])
        # Manually overwrite createdAt for testing
        all_tasks = taskpad_func.load_tasks()
        all_tasks[i]["createdAt"] = task["created"]
        taskpad_func.save_tasks(all_tasks)

    # Filter by year 2024
    result = taskpad_func.list_tasks(created="2024")
    assert "Buy Melon" in result
    assert "Buy Strawberries" not in result
    assert "Buy Shoes" not in result