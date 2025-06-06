from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

from src.widgets.CloseButton import CloseButton
from src.widgets.ScriptList import ScriptList


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sticky Script Runner")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setGeometry(50, 50, 300, 400)
        self.layout = QVBoxLayout()

        self.layout.addWidget(CloseButton(self))
        self.layout.addWidget(ScriptList())
        self.setLayout(self.layout)

        self._drag_pos = None  # To track the position when dragging starts

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_pos is not None and event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self._drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_pos = None