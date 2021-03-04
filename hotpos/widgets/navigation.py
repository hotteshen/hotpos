from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QMenu, QAction

from ..config import RES_PATH, SIZE_A, SIZE_B


class NavigationWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QApplication.instance()

        self.root_layout = QHBoxLayout()
        self.setLayout(self.root_layout)

        self.addMenu()

        self.home_button = QPushButton("Home")
        self.home_button.clicked.connect(self.showHomePage)
        _styleButton(self.home_button)
        self.root_layout.addWidget(self.home_button)

        self.take_away_button = QPushButton("Take away")
        self.take_away_button.clicked.connect(self.showTakeAwayPage)
        _styleButton(self.take_away_button)
        self.root_layout.addWidget(self.take_away_button)

        button = QPushButton("Delivery")
        _styleButton(button)
        self.root_layout.addWidget(button)

        button = QPushButton("Table")
        _styleButton(button)
        self.root_layout.addWidget(button)

        button = QPushButton("Reservation")
        _styleButton(button)
        self.root_layout.addWidget(button)

    def addMenu(self):
        menu = QMenu(self)
        button = QPushButton()
        button.setIcon(QIcon(str(RES_PATH / 'icon-menu.png')))
        _styleButton(button)
        button.setFixedWidth(SIZE_B)
        button.setMenu(menu)
        self.root_layout.addWidget(button)

        action = QAction(self)
        action.setText("Home")
        menu.addAction(action)

        action = QAction(self)
        action.setText("Take Away")
        menu.addAction(action)

        action = QAction(self)
        action.setText("Delivery")
        menu.addAction(action)

        action = QAction(self)
        action.setText("Table")
        menu.addAction(action)

        action = QAction(self)
        action.setText("Reservation")
        menu.addAction(action)

        menu.addSeparator()

        action = QAction(self)
        action.setText("Preview Order Sales")
        menu.addAction(action)

        action = QAction(self)
        action.setText("Open Delivery Orders")
        menu.addAction(action)

        action = QAction(self)
        action.setText("Open Tables")
        menu.addAction(action)

        action = QAction(self)
        action.setText("Main Reading")
        menu.addAction(action)

        action = QAction(self)
        action.setText("Open Tables Reading")
        menu.addAction(action)

        menu.addSeparator()

        action = QAction(self)
        action.setText("Transfer Items")
        menu.addAction(action)

        action = QAction(self)
        action.setText("End of Day")
        menu.addAction(action)

        action = QAction(self)
        action.setText("Screen Setup")
        menu.addAction(action)

        menu.addSeparator()

        action = QAction(self)
        action.setText("Log Out")
        menu.addAction(action)

        action = QAction(self)
        action.setText("Exit")
        menu.addAction(action)


    def showHomePage(self):
        self.app.main_window.showPage('home')

    def showTakeAwayPage(self):
        self.app.main_window.showPage('take_away')

    def setCurrentTab(self, page_name: str):
        if page_name == 'home':
            self.take_away_button.setDown(False)
            self.home_button.setDown(True)
        elif page_name == 'take_away':
            self.home_button.setDown(False)
            self.take_away_button.setDown(True)
        else:
            self.home_button.setDown(False)
            self.take_away_button.setDown(False)

def _styleButton(btn: QPushButton) -> QPushButton:
    btn.setStyleSheet('height: 64px; margin-bottom: 16px;')
