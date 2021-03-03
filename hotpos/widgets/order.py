from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QListWidget, QPushButton

from ..config import RES_PATH
from .group_box import GroupBoxWidget
from .label import LabelWidget


class OrderWidget(GroupBoxWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        root_layout = self.getRootLayout()
        cookie_list = QListWidget()
        root_layout.addWidget(cookie_list)

        row_layout = QHBoxLayout()
        root_layout.addLayout(row_layout)

        layout = QHBoxLayout()
        row_layout.addLayout(layout)
        layout.addWidget(LabelWidget('Sub Total'), 1)
        self.sub_total_label = LabelWidget('0.00')
        layout.addWidget(self.sub_total_label, 0)

        layout = QHBoxLayout()
        row_layout.addLayout(layout)
        layout.addWidget(LabelWidget('Tax'), 1)
        self.tax_label = LabelWidget('0.00')
        layout.addWidget(self.tax_label, 0)

        row_layout = QHBoxLayout()
        root_layout.addLayout(row_layout)

        layout = QHBoxLayout()
        row_layout.addLayout(layout)
        layout.addWidget(LabelWidget('Discount'), 1)
        button = QPushButton("")
        button.setIcon(QIcon(str(RES_PATH / 'icon-add.png')))
        layout.addWidget(button, 0)

        layout = QHBoxLayout()
        row_layout.addLayout(layout)
        layout.addWidget(LabelWidget('Tax'), 1)
        button = QPushButton("")
        button.setIcon(QIcon(str(RES_PATH / 'icon-add.png')))
        layout.addWidget(button, 0)

        row_layout = QHBoxLayout()
        root_layout.addLayout(row_layout)

        layout = QHBoxLayout()
        row_layout.addLayout(layout)
        layout.addWidget(LabelWidget('Sub Total'), 1)
        self.sub_total_label = LabelWidget('0.00')
        layout.addWidget(self.sub_total_label, 0)

        row_layout = QHBoxLayout()
        root_layout.addLayout(row_layout)
        button = QPushButton("CHECKOUT")
        row_layout.addWidget(button)
