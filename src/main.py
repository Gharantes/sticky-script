import sys
from PyQt5.QtWidgets import QApplication
from src.widgets.MainWidget import MainWidget
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()
    sys.exit(app.exec_())
