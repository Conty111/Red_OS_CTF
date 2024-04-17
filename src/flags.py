import json
import hashlib
import hmac

from task.model import TasksList


def generate_flags(tasks_path: str, answers_path: str, key: str):
    with open(file=tasks_path, mode='+r') as file:
            tasks_data = json.load(file)
            tasksList: TasksList = TasksList.model_validate(tasks_data)

    with open(file=answers_path, mode='w') as file:
        answers = [0] * len(tasksList.tasks)
        for i in range(len(tasksList.tasks)):
            answers[i] = hmac.new(key.encode('utf-8'), tasksList.tasks[i].text.encode('utf-8'), hashlib.sha256).hexdigest()[2:12]
            file.write(f"FLAG-[{answers[i]}]\n")
