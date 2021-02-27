from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from .login_widget import LoginWidget
from ..config import WINDOW_MIN_SIZE, APP_NAME, RES_PATH


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle(APP_NAME)
        self.setWindowFlags( Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint )
        self.setWindowIcon(QIcon(str(RES_PATH / 'icon.png')))
        self.setMinimumSize(*WINDOW_MIN_SIZE)

        root_layout = QVBoxLayout()
        self.setLayout(root_layout)

        self.login_widget = LoginWidget()
        root_layout.addWidget(self.login_widget)
