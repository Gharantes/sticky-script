from PyQt5.QtWidgets import QPushButton, QWidget


class CloseButton(QPushButton):
    def __init__(self, window: QWidget):
        super().__init__()
        self.setText("Close")
        self.clicked.connect(window.close)
