import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Устанавливаем основное изображение фона
        background_image = QPixmap("img/background.jpg")  # Замените "background.jpg" на путь к вашему изображению
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, background_image.width(), background_image.height())

        # Создаем вертикальный layout для размещения других объектов
        layout = QVBoxLayout()

        # Добавляем кнопку с фоном
        button_with_background = QPushButton("Button with Background")
        button_with_background.setStyleSheet("background-image: url('img/background.jpg');")  # Замените "button_background.jpg" на путь к вашему изображению
        layout.addWidget(button_with_background)

        # Добавляем еще какие-то объекты с их собственными фонами
        # ...

        # Устанавливаем layout в центральную область основного окна
        central_widget = QLabel(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("PyQt5 GUI с фоновым изображением")
        self.setGeometry(100, 100, background_image.width(), background_image.height())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())