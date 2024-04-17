from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QColor, QTextBlockFormat, QTextCursor, QCursor
from PyQt5.QtCore import Qt

class HelloWidget(QWidget):
    def __init__(self, next_func, parent: QWidget | None = None):
        super().__init__(parent=parent)

        self.nextFunc = next_func
        self.my_parent = parent

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_widget = QWidget(self)

        # Устанавливаем цвет фона и делаем его полупрозрачным
        main_widget.setStyleSheet(f"background-color: rgba(0, 0, 0, 0.85); border-radius: 25%; border: 2px solid black; color: red; margin: 55%; padding: 25%;")
        
        
        # Добавляем заголовок
        title_label = QLabel("Welcome to the club, buddy!", self)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        title_label.setStyleSheet("background-color: none; border: none; color: white; font-size: 28px; font-weight: bold; margin-top: 20%; margin-bottom: 0;")

        # Добавляем текст
        text_label = QLabel("Это десктопное приложение под Linux позволит поиграть в познавательную игру 'ЧТО ТАКОЕ РЕД ОС?'. \n\nСейчас доступно 10 заданий для выполнения по 4 различным темам. Задания достаточно простые (за исключением последних двух) и можно выполнять в любом порядке. Результат после перезапуска приложения не сохраняется. \n\nДля проверки выполнения задания нужно ввести 'флаг', который в задании нужно каким-либо образом достать. \nФлаги имеют вид 'FLAG-[cb47f5c036]'.\n\nУдачи!", self)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        text_label.setWordWrap(True)
        text_label.setStyleSheet("line-height: 30px; font-size: 20px; background-color: none; border: none; color: white; margin-top: 0; margin-bottom: 0;")


        # Добавляем кнопку
        start_button = QPushButton("НАЧАТЬ", self)
        start_button.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                font-size: 20px;
                background-color: red;
                color: white;
                border: none;
                border-radius: 15%;
                padding: 10px;
                margin-top: 0;
            }

            QPushButton:hover {
                background-color: rgba(255, 58, 58, 0.8);
            }
        """)
        start_button.setFixedSize(300, 125)
        start_button.clicked.connect(self.nextFunc)

        # Добавляем виджеты на основной виджет
        central_layout = QVBoxLayout(main_widget)
        central_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)
        central_layout.addWidget(text_label, alignment=Qt.AlignmentFlag.AlignTop)
        central_layout.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        # Создаем главный макет для центрирования
        main_widget.setLayout(central_layout)
        main_layout.addWidget(main_widget)
        self.setLayout(main_layout)
