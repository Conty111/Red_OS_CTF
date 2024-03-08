from typing import List
from pydantic import BaseModel, HttpUrl, ConfigDict

import os

from config import Config


class TaskModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    text: str
    theme: str
    hint: str
    level: int
    theory_link: HttpUrl | None = None
    task_script_name: str
    is_completed: bool = False

    def setup_system(self, flag: str):
        os.system(f"./{Config.PATH_TO_TASKS_SCRIPTS}/setup/{self.task_script_name} {flag}")

    def reset_system(self):
        os.system(f"./{Config.PATH_TO_TASKS_SCRIPTS}/reset/{self.task_script_name}")


class TasksList(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tasks: List[TaskModel]
