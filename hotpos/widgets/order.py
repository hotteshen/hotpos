from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QSizePolicy

from ..config import RES_PATH, SIZE_A
from .group_box import GroupBoxWidget
from .label import LabelWidget


class OrderedCookieWidget(QWidget):

    def __init__(self, cookie, parent=None):
        super().__init__(parent=parent)

        self.cookie = cookie

        root_layout = QVBoxLayout(self)
        self.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)

        header = QHBoxLayout()
        root_layout.addLayout(header)

        name_label = LabelWidget(self.cookie['name'])
        header.addWidget(name_label, 1)

        delete_button = QPushButton("")
        delete_button.setFixedHeight(SIZE_A)
        delete_button.setFixedWidth(SIZE_A)
        delete_button.setIcon(QIcon(str(RES_PATH / 'icon-delete.png')))
        delete_button.clicked.connect(lambda: self.setParent(None))
        header.addWidget(delete_button, 0)


class OrderWidget(GroupBoxWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QApplication.instance()
        self.initUI()

    def addCookieItem(self, main_cat: int, sub_cat: int, cookie_item: int):
        cookie = self.app.backend().getCategoryData()[main_cat]['sub_category_list'][sub_cat]['item_list'][cookie_item]
        cookie_widget = OrderedCookieWidget(cookie)
        self.cookie_list_layout.insertWidget(self.cookie_list_layout.count() - 1, cookie_widget)

    def initUI(self):
        root_layout = self.getRootLayout()

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(LabelWidget("Order ID:"))
        root_layout.addWidget(widget, 0)

        cookie_list = QWidget()
        self.cookie_list_layout = QVBoxLayout(cookie_list)
        self.cookie_list_layout.addStretch()

        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(cookie_list)
        root_layout.addWidget(scroll)

        row_layout = QHBoxLayout()
        root_layout.addLayout(row_layout, 0)

        widget = QWidget()
        layout = QHBoxLayout(widget)
        row_layout.addWidget(widget)
        layout.addWidget(LabelWidget('Sub Total'), 1)
        self.sub_total_label = LabelWidget('0.00')
        layout.addWidget(self.sub_total_label, 0)

        widget = QWidget()
        layout = QHBoxLayout(widget)
        row_layout.addWidget(widget)
        layout.addWidget(LabelWidget('Tax'), 1)
        self.tax_label = LabelWidget('0.00')
        layout.addWidget(self.tax_label, 0)

        row_layout = QHBoxLayout()
        root_layout.addLayout(row_layout, 0)

        widget = QWidget()
        layout = QHBoxLayout(widget)
        row_layout.addWidget(widget)
        layout.addWidget(LabelWidget('Discount'), 1)
        button = QPushButton("")
        button.setFixedHeight(SIZE_A)
        button.setFixedWidth(SIZE_A)
        button.setIcon(QIcon(str(RES_PATH / 'icon-add.png')))
        layout.addWidget(button, 0)

        widget = QWidget()
        layout = QHBoxLayout(widget)
        row_layout.addWidget(widget)
        layout.addWidget(LabelWidget('Tax'), 1)
        button = QPushButton("")
        button.setFixedHeight(SIZE_A)
        button.setFixedWidth(SIZE_A)
        button.setIcon(QIcon(str(RES_PATH / 'icon-add.png')))
        layout.addWidget(button, 0)

        row = QWidget()
        row_layout = QHBoxLayout(row)
        root_layout.addWidget(row)

        layout = QHBoxLayout()
        row_layout.addLayout(layout)
        layout.addWidget(LabelWidget('Sub Total'), 1)
        self.sub_total_label = LabelWidget('0.00')
        layout.addWidget(self.sub_total_label, 0)

        row_layout = QHBoxLayout()
        root_layout.addLayout(row_layout, 0)
        row_layout.addWidget(LabelWidget(), 1)
        button = QPushButton("CHECKOUT")
        row_layout.addWidget(button, 1)
