import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
import subprocess

FOLDER_PATH = "/home/guilherme/FuncionalKeys"

class StickyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sticky Script Runner")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setGeometry(50, 50, 300, 400)  # Adjust size and position here
        
        self.layout = QVBoxLayout()
        self.close_button()
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)
        self.setLayout(self.layout)
        
        self.load_files()
        
        self.list_widget.itemClicked.connect(self.run_script)

    def load_files(self):
        if not os.path.exists(FOLDER_PATH):
            QMessageBox.critical(self, "Error", f"Folder not found:\n{FOLDER_PATH}")
            return
        files = [f for f in os.listdir(FOLDER_PATH) if f.endswith(".sh")]
        self.list_widget.clear()
        self.list_widget.addItems(files)

    def run_script(self, item):
        filepath = os.path.join(FOLDER_PATH, item.text())
        # Confirm before running
        reply = QMessageBox.question(self, "Run script?",
                                     f"Run {item.text()} with sudo?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                # Run the script with sudo, this will prompt for password in terminal
                subprocess.run(['sudo', 'sh', filepath], check=True)
            except subprocess.CalledProcessError as e:
                QMessageBox.warning(self, "Error", f"Failed to run script:\n{e}")

    def close_button(self):
        btn = QPushButton("close")
        btn.clicked.connect(self.close)
        self.layout.addWidget(btn)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StickyWindow()
    window.show()
    sys.exit(app.exec_())
