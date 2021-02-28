from PyQt5.QtWidgets import QHBoxLayout, QWidget, QLabel


class TakeAwayPage(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QHBoxLayout()
        self.setLayout(root_layout)

        root_layout.addWidget(QLabel("Hello"))
