import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import \
    QWidget, QHBoxLayout, QPushButton, \
    QLineEdit, QVBoxLayout, QLabel, QScrollArea, \
    QSizePolicy, QScrollBar

from config import Config


class TaskWindow(QWidget):
    def __init__(self, parent: QWidget, cfg: Config):
        super().__init__(parent=parent)

        # Создаем вертикальный layout
        self.main_layout = QVBoxLayout(self)

        # Добавляем блок текста с полупрозрачным фоном
        text_block = QWidget(self)
        text_block.setStyleSheet(f"background-color: rgba(0, 0, 0, 0.7); border-radius: 10px; padding: 25px; margin: 20%;")
        text_block.setMaximumHeight(int(parent.height()*0.75))

        # Создаем вертикальный layout для текста и формы ввода внутри блока текста
        text_input_layout = QVBoxLayout(text_block)

        # Добавляем заголовок
        title_label = QLabel("Заголовок")
        title_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #FFFFFF; margin: 25%; ba")
        text_input_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignTop)

        # Добавляем три абзаца текста
        for _ in range(3):
            paragraph_label = QLabel("Абзац текста. Это может быть довольно длинным, в зависимости от вашего текста.")
            paragraph_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            paragraph_label.setStyleSheet("font-size: 14px; color: #FFFFFF; background-color: none; margin: 10%;")
            text_input_layout.addWidget(paragraph_label, alignment=Qt.AlignmentFlag.AlignTop)

        # Устанавливаем пропорции для текста
        text_input_layout.setStretchFactor(title_label, 1)
        text_input_layout.setStretchFactor(paragraph_label, 3)

        # Создаем область прокрутки для блока текста
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(text_block)
        scroll_area.setMaximumWidth(int(parent.width() * 0.75))
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setStyleSheet("QScrollArea { background: transparent; } QScrollBar:vertical { border-color: black; background-color: gray; }")
        scroll_area.setMaximumHeight(int(parent.height()*0.7))

        print(scroll_area.maximumHeight())

        self.text_area = scroll_area
        self.main_layout.addWidget(self.text_area, alignment=Qt.AlignmentFlag.AlignTop)
        print(self.text_area.maximumHeight())


        # Нижняя часть
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

