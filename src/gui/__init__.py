import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class App(QWidget):
    def __init__(self, text, x, y, screen_resolution):
        super().__init__()

        label = QLabel(text)
        label.setStyleSheet("color:white")

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)
        self.setWindowFlags(Qt.ToolTip)
        self.setStyleSheet("background:rgb(66,74,88);font-size:16px;")
        self.setWindowFlags(Qt.ToolTip)

        screen_width, screen_height = screen_resolution.width(), screen_resolution.height()
        window_size = self.sizeHint()
        window_width, window_height = window_size.width(), window_size.height()

        x = min(x, screen_width - window_width)
        y = min(y, screen_height - window_height)

        self.move(x, y)

    def mousePressEvent(self, _event):
        self.close()
        sys.exit(0)


def show_tip(text, x, y, time):
    app = QApplication([])

    def operate():
        app.exit()

    timer = QTimer()
    timer.timeout.connect(operate)
    timer.start(time)

    window = App(text, x, y, app.desktop().screenGeometry())
    window.show()

    app.exec_()
