from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from .pages.login import Login
from .pages.home import Home
from .config import WINDOW_MIN_SIZE, APP_NAME, RES_PATH


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle(APP_NAME)
        self.setWindowFlags( Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint )
        self.setWindowIcon(QIcon(str(RES_PATH / 'icon.png')))
        self.setMinimumSize(*WINDOW_MIN_SIZE)

        root_layout = QVBoxLayout()
        self.setLayout(root_layout)

        self.login_page = Login()
        root_layout.addWidget(self.login_page)
        self.home_page = Home()
        root_layout.addWidget(self.home_page)

        self.showPage('login')

    def showPage(self, page: str):
        self.login_page.hide()
        self.home_page.hide()
        if page == 'login':
            self.login_page.show()
        elif page == 'home':
            self.home_page.show()
