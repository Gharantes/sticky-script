import os
import subprocess

from PyQt5.QtWidgets import QListWidget, QMessageBox


class ScriptList(QListWidget):
    def __init__(self):
        super().__init__()
        self.FOLDER_PATH = os.getenv("FOLDER_PATH")
        # self.widget = QListWidget()
        self.load_files()

    def load_files(self):
        if not os.path.exists(self.FOLDER_PATH):
            QMessageBox.critical(self, "Error", f"Folder not found:\n{self.FOLDER_PATH}")
            return
        files = [f for f in os.listdir(self.FOLDER_PATH) if f.endswith(".sh")]
        self.clear()
        self.addItems(files)
        self.itemClicked.connect(self.run_script)

    def run_script(self, item):
        filepath = os.path.join(self.FOLDER_PATH, item.text())
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