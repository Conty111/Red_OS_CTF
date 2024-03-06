import sys

from PyQt5.QtCore import QPropertyAnimation, QAbstractAnimation
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QApplication, \
    QWidget, QHBoxLayout, QPushButton, \
    QLineEdit, \
    QVBoxLayout, QLabel

from config import Config


class TaskWindow(QWidget):
    def __init__(self, parent: QWidget, cfg: Config):
        super().__init__(parent=parent)

        
        # Создаем вертикальный layout
        self.main_layout = QVBoxLayout(self)

        # Создаем горизонтальный layout для текста и формы ввода
        text_input_layout = QVBoxLayout()
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(
            cfg.MARGIN_BOTTOM_WIDGET, 
            cfg.MARGIN_BOTTOM_WIDGET, 
            cfg.MARGIN_BOTTOM_WIDGET, 
            cfg.MARGIN_BOTTOM_WIDGET
            )

        bottom_widget = QWidget(self)
        bottom_widget.setMaximumWidth(int(self.width() * 80 / 100))
        bottom_widget.setFixedHeight(cfg.BOTTOM_WIDGET_HEIGHT)

        
        
        
        # Добавляем текст в левую половину
        text_label = QLabel("Это текст в левой половине.")
        text_input_layout.addWidget(text_label)

        self.main_layout.addLayout(text_input_layout)

        # Создаем форму ввода в левом нижнем углу с отступами
        self.input_field = QLineEdit(self)
        # self.input_field.setStyleSheet("background-color: lightgreen;")
        self.input_field.setPlaceholderText("Вводите флаг сюда!")
        self.input_field.setBaseSize(cfg.INPUT_FIELD_MAX_WIDTH, cfg.INPUT_FIELD_HEIGHT)
        self.input_field.setMaximumSize(cfg.INPUT_FIELD_MAX_WIDTH, cfg.INPUT_FIELD_HEIGHT)
        self.input_field.setMinimumSize(cfg.INPUT_FIELD_MIN_WIDTH, cfg.INPUT_FIELD_HEIGHT)

        bottom_layout.addWidget(self.input_field)
        bottom_layout.addStretch()
        bottom_layout.setSpacing(100)

        # Создаем кнопку "Проверить" в правом нижнем углу с отступами
        check_button = QPushButton("ПРОВЕРИТЬ", self)
        with open(cfg.CHECK_BUTTON_STYLES_URL) as styles:
            check_button.setStyleSheet(styles.read())

        check_button.clicked.connect(self.check_button_clicked)
        check_button.setFixedSize(int(cfg.INPUT_FIELD_WIDTH * 50 / 100), cfg.INPUT_FIELD_HEIGHT)
        check_button.setContentsMargins(cfg.MARGIN_BOTTOM_WIDGET, cfg.MARGIN_BOTTOM_WIDGET, cfg.MARGIN_BOTTOM_WIDGET, cfg.MARGIN_BOTTOM_WIDGET)
        bottom_layout.addWidget(check_button)

        # Добавляем layout с кнопкой "Проверить" в основной layout
        self.main_layout.addLayout(bottom_layout)
        bottom_widget.setLayout(bottom_layout)
        self.main_layout.addChildWidget(bottom_widget)

    def check_button_clicked(self):
        # Обработка события при нажатии кнопки "Проверить"
        input_text = self.input_field.text()
        print(f"Текст для проверки: {input_text}")

        self.input_field.clear()

