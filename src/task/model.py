from typing import List
from pydantic import BaseModel, HttpUrl, ConfigDict

import os

class TaskModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    text: str
    theme: str
    hint: str
    theory_link: HttpUrl | None = None
    setup_commands: List[str]
    reset_commands: List[str]
    is_completed: bool = False

    def setup_system(self):
        for command in self.setup_commands:
            os.system(command)

    def reset_system(self):
        for command in self.reset_commands:
            os.system(command)


class TasksList(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tasks: List[TaskModel]
