from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton


class NavigationWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QApplication.instance()

        root = QHBoxLayout()
        self.setLayout(root)

        def increaseHeight(btn: QPushButton) -> QPushButton:
            btn.setStyleSheet('height: 64px; margin-bottom: 16px;')

        button = QPushButton("Home")
        button.clicked.connect(self.showHomePage)
        increaseHeight(button)
        root.addWidget(button)

        button = QPushButton("Take away")
        button.clicked.connect(self.showTakeAwayPage)
        increaseHeight(button)
        root.addWidget(button)

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
