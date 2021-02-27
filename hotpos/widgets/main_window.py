from PyQt5.QtWidgets import QWidget, QVBoxLayout

from .login_widget import LoginWidget


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QVBoxLayout()
        self.setLayout(root_layout)

        self.login_widget = LoginWidget()
        root_layout.addWidget(self.login_widget)
