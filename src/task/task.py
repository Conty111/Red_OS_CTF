from typing import List

from PyQt5.QtGui import QTextOption, QTextBlockFormat
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import \
    QWidget, QHBoxLayout, QPushButton, QTextEdit, \
    QLineEdit, QVBoxLayout, QLabel, QScrollArea \

from config import Config
from task.model import TaskModel


class TaskWindow(QWidget):
    def __init__(self, 
                 parent: QWidget, 
                 cfg: Config, 
                 tasks: List[TaskModel],
                 answers: List[str],
                 idx: int = 0):
        
        super().__init__(parent=parent)
        self.config: Config = cfg
        self.tasks: List[TaskModel] = tasks
        self.current_task: int = idx
        self.answers: List[str] = answers

        self.init_ui()
    
    def init_ui(self):
        # Создаем вертикальный layout
        self.main_layout = QVBoxLayout(self)

        # Добавляем блок текста с полупрозрачным фоном
        text_block = QWidget(self)
        text_block.setStyleSheet(f"background-color: rgba(0, 0, 0, 0.7); border-radius: 10px; padding: 25px; margin: 20%;")
        text_block.setMaximumWidth(1100)

        # Создаем вертикальный layout для текста и формы ввода внутри блока текста
        text_input_layout = QVBoxLayout(text_block)

        # Добавляем заголовок
        title_label = QLabel(parent=self)
        title_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        title_label.setStyleSheet("font-size: 26px; font-weight: bold; color: #FFFFFF; margin: 25%;")
        self.title = title_label
        text_input_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignTop, stretch=1)

        # Текст
        text_label = QLabel(parent=self)
        text_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        text_label.setStyleSheet("font-size: 24px; color: white; margin: 0; background-color: transparent; line-height: 24;")
        text_label.setWordWrap(True)
        text_input_layout.addWidget(text_label, alignment=Qt.AlignmentFlag.AlignTop, stretch=3)
        self.text = text_label

        # Подсказка
        hint_label = QLabel(parent=self)
        hint_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        hint_label.setStyleSheet("font-size: 20px; color: white; margin: 0; background-color: transparent; line-height: 24px;")
        hint_label.setWordWrap(True)
        text_input_layout.addWidget(hint_label, alignment=Qt.AlignmentFlag.AlignTop, stretch=2)
        self.hint = hint_label

        # Ссылки
        link_label = QLabel(parent=self)
        link_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        link_label.setStyleSheet("font-size: 20px; color: white; margin: 3%; background-color: transparent; line-height: 24px;")
        link_label.setWordWrap(True)
        text_input_layout.addWidget(link_label, alignment=Qt.AlignmentFlag.AlignTop)
        self.link = link_label

        # Создаем область прокрутки для блока текста
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(text_block)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("QScrollArea { background: transparent; } QScrollBar:vertical { border-color: black; background-color: gray; }")
        scroll_area.setFixedHeight(int(self.parentWidget().height()*0.7))


        self.text_area = scroll_area
        self.main_layout.addWidget(self.text_area, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addStretch(2)


        success_label = QLabel(parent=self)
        self.success = success_label
        self.main_layout.addWidget(self.success, stretch=2)

        # Нижняя часть
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(
            self.config.MARGIN_BOTTOM_WIDGET, 
            self.config.MARGIN_BOTTOM_WIDGET, 
            self.config.MARGIN_BOTTOM_WIDGET, 
            self.config.MARGIN_BOTTOM_WIDGET
            )

        bottom_widget = QWidget(self)
        bottom_widget.setMaximumWidth(int(self.width() * 80 / 100))
        bottom_widget.setFixedHeight(self.config.BOTTOM_WIDGET_HEIGHT)

        back_button = QPushButton(text="Предыдущее", parent=self)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;
                border-radius: 10%;
                padding: 5px;   
            }

            QPushButton:hover {
                background-color: gray;
                border: 1px solid rgb(53, 185, 41);
            }
        """)
        back_button.setFixedSize(int(self.config.INPUT_FIELD_WIDTH * 25 / 100), self.config.INPUT_FIELD_HEIGHT)
        back_button.clicked.connect(self.prev_question)
        self.back_button = back_button

        # Создаем форму ввода в левом нижнем углу с отступами
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Вводите флаг сюда!")
        self.input_field.setBaseSize(self.config.INPUT_FIELD_MAX_WIDTH, self.config.INPUT_FIELD_HEIGHT)
        self.input_field.setMaximumSize(self.config.INPUT_FIELD_MAX_WIDTH, self.config.INPUT_FIELD_HEIGHT)
        self.input_field.setMinimumSize(self.config.INPUT_FIELD_MIN_WIDTH, self.config.INPUT_FIELD_HEIGHT)


        # Создаем кнопку "Проверить" в правом нижнем углу с отступами
        check_button = QPushButton("ПРОВЕРИТЬ", self)
        with open(self.config.CHECK_BUTTON_STYLES_URL) as styles:
            check_button.setStyleSheet(styles.read())

        check_button.clicked.connect(self.check_answer)
        check_button.setFixedSize(int(self.config.INPUT_FIELD_WIDTH * 50 / 100), self.config.INPUT_FIELD_HEIGHT)
        check_button.setContentsMargins(self.config.MARGIN_BOTTOM_WIDGET, self.config.MARGIN_BOTTOM_WIDGET, self.config.MARGIN_BOTTOM_WIDGET, self.config.MARGIN_BOTTOM_WIDGET)
        self.check_button = check_button

        # Создаем кнопку "Проверить" в правом нижнем углу с отступами
        next_button = QPushButton("Следующее", self)
        next_button.clicked.connect(self.next_question)
        next_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(95, 39, 245, 1);
                color: white;
                border-radius: 10%;
                padding: 5px;   
            }

            QPushButton:hover {
                background-color: rgba(141, 98, 255, 1);
                border: 1px solid rgba(163, 129, 254, 1);
            }
        """)
        next_button.setFixedSize(int(self.config.INPUT_FIELD_WIDTH * 25 / 100), self.config.INPUT_FIELD_HEIGHT)
        next_button.setContentsMargins(self.config.MARGIN_BOTTOM_WIDGET, self.config.MARGIN_BOTTOM_WIDGET, self.config.MARGIN_BOTTOM_WIDGET, self.config.MARGIN_BOTTOM_WIDGET)
        self.next_button = next_button

        bottom_layout.addWidget(self.back_button)
        bottom_layout.addSpacing(15)
        bottom_layout.addWidget(self.input_field)
        bottom_layout.addSpacing(50)
        bottom_layout.addWidget(self.check_button)
        bottom_layout.addSpacing(15)
        bottom_layout.addWidget(self.next_button)


        # Добавляем layout с кнопкой "Проверить" в основной layout
        self.main_layout.addLayout(bottom_layout)
        bottom_widget.setLayout(bottom_layout)
        self.main_layout.addChildWidget(bottom_widget)

        self.input_field.clear()


    def show_question(self):
        t = self.tasks[self.current_task]

        self.title.setText(f"Задание {self.current_task+1}. {t.theme}")
        self.text.setText(f"Описание: {t.text}")
        self.hint.setText(f"Подсказки: {t.hint}")
        if t.theory_link:
            self.link.setText(f"{t.theory_link}")
            self.link.show()
        else:
            self.link.hide()

        if not t.is_completed:
            t.setup_system(self.answers[self.current_task])
            self.success.hide()
            self.input_field.show()
            self.check_button.show()
        else:
            self.success.setText("Правильно!")
            self.success.setStyleSheet("font-size: 20px; color: #FFFFFF; background-color: green; margin: 7%; padding: 20%; border-radius: 15%;")
            self.success.show()
            self.input_field.hide()
            self.check_button.hide()
        self.next_button.show()
        self.back_button.show()


    def check_answer(self):
        user_answer = self.input_field.text()
        correct_answer = self.answers[self.current_task][:-1]

        if user_answer == correct_answer:
            self.tasks[self.current_task].is_completed = True
            self.tasks[self.current_task].reset_system()
            self.show_question()
        else:
            self.success.setText("Ответ неверный")
            self.success.setStyleSheet("font-size: 20px; color: #FFFFFF; background-color: red; margin: 7%; padding: 20%; border-radius: 15%;")
            self.success.show()
    
    def next_question(self):
        if self.current_task < len(self.tasks) - 1:
            if not self.tasks[self.current_task].is_completed:
                self.tasks[self.current_task].reset_system()
            self.current_task += 1
            self.show_question()
        else:
            self.success.setText("Это самое последнее задание")
            self.success.setStyleSheet("font-size: 20px; color: #FFFFFF; background-color: red; margin: 7%; padding: 20%; border-radius: 15%;")
            self.success.show()

    def prev_question(self):
        if self.current_task > 0:
            if not self.tasks[self.current_task].is_completed:
                self.tasks[self.current_task].reset_system()
            self.current_task -= 1
            self.show_question()
        else:
            self.success.setText("Это самое первое задание")
            self.success.setStyleSheet("font-size: 20px; color: #FFFFFF; background-color: red; margin: 7%; padding: 20%; border-radius: 15%;")
            self.success.show()
    
    def closeEvent(self, event):
        if not self.tasks[self.current_task].is_completed:
                self.tasks[self.current_task].reset_system()
        event.accept()

