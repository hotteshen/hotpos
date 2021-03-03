from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from .pages.login import LoginPage
from .pages.home import HomePage
from .pages.take_away import TakeAwayPage
from .widgets.navigation import NavigationWidget
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

        self.navigation = NavigationWidget()
        root_layout.addWidget(self.navigation, 0)

        self.login_page = LoginPage()
        root_layout.addWidget(self.login_page, 1)
        self.home_page = HomePage()
        root_layout.addWidget(self.home_page, 1)
        self.take_away_page = TakeAwayPage()
        root_layout.addWidget(self.take_away_page, 1)

        self.showPage('take_away')

    def showPage(self, page_name: str):
        self.navigation.hide()
        self.login_page.hide()
        self.home_page.hide()
        self.take_away_page.hide()
        if page_name == 'login':
            self.login_page.show()
        elif page_name == 'home':
            self.navigation.show()
            self.navigation.setCurrentTab(page_name)
            self.home_page.show()
        elif page_name == 'take_away':
            self.navigation.show()
            self.navigation.setCurrentTab(page_name)
            self.take_away_page.show()
