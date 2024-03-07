import sys
from dotenv import load_dotenv
from os import environ
import json

from PyQt5.QtGui import QColorConstants, QPixmap
from PyQt5.QtWidgets import QApplication, \
    QWidget, QHBoxLayout, QPushButton, \
    QLineEdit, QGraphicsOpacityEffect, \
    QVBoxLayout, QLabel

from config import Config
from flags import generate_flags
from task.task import TaskWindow
from task.model import TasksList


class MainWindow(QWidget):
    def __init__(self, cfg: Config, tasks_file_path: str, answers_path: str):
        super().__init__()

        self.cfg: Config = cfg

        with open(file=tasks_file_path, mode='+r') as file:
            tasks_data = json.load(file)
            self.tasksList: TasksList = TasksList.model_validate(tasks_data)
        
        with open(file=answers_path, mode='+r') as file:
            answers = file.readlines()

        self.resize(cfg.DEFAULT_WINDOW_WIDTH, cfg.DEFAULT_WINDOW_HEIGHT)
        self.setWindowTitle("Window Title! Welcome!")
        self.setMinimumSize(*cfg.MINIMUM_WINDOW_SIZE)

        background_image = QPixmap("img/background.jpg")  # Замените "background.jpg" на путь к вашему изображению
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, background_image.width(), background_image.height())
        background_label.setStyleSheet("background-image: black;")

        # Добавляем цветовой слой для затемнения фона
        dark_overlay = QLabel(self)
        dark_overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.3);")
        dark_overlay.setGeometry(0, 0, background_image.width(), background_image.height())

        self.task_window = TaskWindow(cfg=self.cfg, parent=self, tasks=self.tasksList.tasks, answers=answers)
        self.task_window.show_question()
        self.setLayout(self.task_window.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tasks_path = sys.argv[1]
    answers = sys.argv[2]
    load_dotenv('.env')
    generate_flags(tasks_path, answers, environ.get('SECRET_KEY'))
    window = MainWindow(Config(), tasks_path, answers)
    window.show()
    sys.exit(app.exec_())
