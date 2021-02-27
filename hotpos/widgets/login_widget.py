from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from ..config import APP_NAME
from . import CenteredLabel


class LoginWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QVBoxLayout()
        self.setLayout(root_layout)

        logo = CenteredLabel(APP_NAME).setRelativeFontSize(30)
        root_layout.addWidget(logo)
