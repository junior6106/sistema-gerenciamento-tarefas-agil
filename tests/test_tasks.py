from app import create_task

def test_create_task():
    task = create_task("Estudar Engenharia de Software", "Alta")
    assert task["title"] == "Estudar Engenharia de Software"
    assert task["priority"] == "Alta"
    assert task["status"] == "To Do"
