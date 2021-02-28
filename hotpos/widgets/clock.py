from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from .label import Label

class Clock(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QVBoxLayout()
        self.setLayout(root_layout)

        logo = Label('Clock').setSize(20).setCenter()
        root_layout.addWidget(logo)
