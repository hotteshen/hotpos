from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from .pages.login import LoginPage
from .pages.home import HomePage
from .pages.table import TablePage
from .pages.take_away import TakeAwayPage
from .widgets.navigation import NavigationWidget
from .config import WINDOW_MIN_SIZE, APP_NAME, RES_PATH


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QApplication.instance()

        self.setWindowTitle(APP_NAME)
        self.setWindowFlags( Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint )
        self.setWindowIcon(QIcon(str(RES_PATH / 'icon.png')))
        self.setMinimumSize(*WINDOW_MIN_SIZE)

        root_layout = QVBoxLayout()
        self.setLayout(root_layout)

        self.navigation = NavigationWidget()
        root_layout.addWidget(self.navigation, 0)

        body = QVBoxLayout()
        root_layout.addLayout(body, 1)

        self.login_page = LoginPage()
        body.addWidget(self.login_page)
        self.home_page = HomePage()
        body.addWidget(self.home_page)
        self.take_away_page = TakeAwayPage()
        body.addWidget(self.take_away_page)
        self.table_page = TablePage()
        body.addWidget(self.table_page)

        if self.app.backend().checkToken():
            self.showPage('home')
        else:
            self.showPage('login')

    def showPage(self, page_name: str):
        self.navigation.hide()
        self.login_page.hide()
        self.home_page.hide()
        self.take_away_page.hide()
        self.table_page.hide()
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
        elif page_name == 'table':
            self.navigation.show()
            self.navigation.setCurrentTab(page_name)
            self.table_page.show()
