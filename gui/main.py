import sys

from PyQt5.QtGui import QColorConstants, QPixmap
from PyQt5.QtWidgets import QApplication, \
    QWidget, QHBoxLayout, QPushButton, \
    QLineEdit, QGraphicsOpacityEffect, \
    QVBoxLayout, QLabel

from config import Config
from task.task import TaskWindow


class MainWindow(QWidget):
    def __init__(self, cfg: Config):
        super().__init__()

        self.cfg: Config = cfg

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

        self.task_window = TaskWindow(cfg=self.cfg, parent=self)
        self.setLayout(self.task_window.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow(Config())
    window.show()
    sys.exit(app.exec_())
