from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton


class NavigationWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QApplication.instance()

        root = QHBoxLayout()
        self.setLayout(root)

        def increaseHeight(btn: QPushButton) -> QPushButton:
            btn.setStyleSheet('height: 64px; margin-bottom: 16px;')

        self.home_button = QPushButton("Home")
        self.home_button.clicked.connect(self.showHomePage)
        increaseHeight(self.home_button)
        root.addWidget(self.home_button)

        self.take_away_button = QPushButton("Take away")
        self.take_away_button.clicked.connect(self.showTakeAwayPage)
        increaseHeight(self.take_away_button)
        root.addWidget(self.take_away_button)

        button = QPushButton("Delivery")
        increaseHeight(button)
        root.addWidget(button)

        button = QPushButton("Table")
        increaseHeight(button)
        root.addWidget(button)

        button = QPushButton("Reservation")
        increaseHeight(button)
        root.addWidget(button)

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
