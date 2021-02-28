from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from ..widgets.group_box import GroupBox
from ..widgets.label import Label


class Home(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QHBoxLayout()
        self.setLayout(root_layout)

        left_layout = QVBoxLayout()
        root_layout.addLayout(left_layout)
        right_layout = QVBoxLayout()
        root_layout.addLayout(right_layout)

        gb = GroupBox()
        left_layout.addWidget(gb)
        gb_root = gb.getRootLayout()
        gb_root.addWidget(Label('List of late orders').setSize(24))
