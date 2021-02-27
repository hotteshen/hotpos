from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from ..config import APP_NAME
from . import CenteredLabel


class ClockWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QVBoxLayout()
        self.setLayout(root_layout)

        logo = CenteredLabel('Clock').setRelativeFontSize(20)
        root_layout.addWidget(logo)
