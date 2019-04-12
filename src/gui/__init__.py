from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


def show_tip(text, x, y):
    app = QApplication([])

    label = QLabel(text)
    label.setStyleSheet("color:white")

    layout = QVBoxLayout()
    layout.addWidget(label)

    def operate():
        app.exit()

    timer = QTimer()
    timer.timeout.connect(operate)
    timer.start(3000)

    window = QWidget()
    window.setWindowFlags(Qt.ToolTip)
    window.setStyleSheet("background:rgb(66,74,88);font-size:16px;")
    window.move(x, y)
    window.setLayout(layout)
    window.show()

    app.exec_()
