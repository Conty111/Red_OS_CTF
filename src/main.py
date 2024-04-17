import sys
from dotenv import load_dotenv
import os
import json

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QStackedWidget, QVBoxLayout

from config import Config
from flags import generate_flags

from hello.hello import HelloWidget
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
            self.answers = file.readlines()

        self.resize(cfg.DEFAULT_WINDOW_WIDTH, cfg.DEFAULT_WINDOW_HEIGHT)
        self.setWindowTitle("РЕД ОС тренер")
        self.setMinimumSize(*cfg.MINIMUM_WINDOW_SIZE)
        self.setWindowIcon(QIcon(QPixmap("img/background1.png")))

        background_image = QPixmap("img/background.jpg")  # Замените "background.jpg" на путь к вашему изображению
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, background_image.width(), background_image.height())
        background_label.setStyleSheet("background-repeat: no-repeat; background-position: center;")

        # Добавляем цветовой слой для затемнения фона
        dark_overlay = QLabel(self)
        dark_overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.3);")
        dark_overlay.setGeometry(0, 0, background_image.width(), background_image.height())

        # Вот эти 2 виджета
        self.stacked_widget = QStackedWidget(self)
        self.task_window = TaskWindow(cfg=self.cfg, parent=self, tasks=self.tasksList.tasks, answers=self.answers)
        self.hello = HelloWidget(parent=self, next_func=self.start)

        self.stacked_widget.addWidget(self.hello)
        self.stacked_widget.addWidget(self.task_window)

        self.m_layout = QVBoxLayout(self)
        self.m_layout.addWidget(self.stacked_widget)
        self.setLayout(self.m_layout)
    
    def start(self):
        self.stacked_widget.setCurrentWidget(self.task_window)
        self.task_window.show_question()

    def closeEvent(self, event):
        self.task_window.closeEvent(event=event)
        os.remove(sys.argv[2])
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tasks_path = sys.argv[1]
    answers = sys.argv[2]
    load_dotenv('.env')
    generate_flags(tasks_path, answers, os.environ.get('SECRET_KEY'))
    window = MainWindow(Config(), tasks_path, answers)
    window.show()
    sys.exit(app.exec_())
