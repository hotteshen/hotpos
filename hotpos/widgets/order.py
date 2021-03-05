from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QSizePolicy, QGroupBox

from ..config import RES_PATH, SIZE_A, SIZE_B, SIZE_C
from ..dialogs.add_modifiers import AddModifiersDialog
from ..dialogs.edit_price import EditPriceDialog
from .group_box import GroupBoxWidget
from .horizontal_spinbox import HorizontalSpinBox
from .label import LabelWidget


class OrderedCookieWidget(QGroupBox):

    def __init__(self, cookie, parent=None):
        super().__init__(parent=parent)

        self.cookie = cookie
        self.price_per_cookie = self.cookie['price']
        self.quantity = 1

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
        delete_button.setFixedWidth(SIZE_B)
        header.addWidget(delete_button, 0)

        body = QHBoxLayout()
        root_layout.addLayout(body)

        self.quantity_spinbox = HorizontalSpinBox()
        self.quantity_spinbox.setRange(1, 100)
        self.quantity_spinbox.setValue(1)
        self.quantity_spinbox.valueChanged.connect(self.onQuantityChange)
        body.addWidget(self.quantity_spinbox)

        self.price_label = LabelWidget(str(self.price_per_cookie)).setCenter()
        body.addWidget(self.price_label)

        button = QPushButton("+M")
        button.setFixedWidth(SIZE_B)
        if len(self.cookie['modifiers']) == 0:
            button.setEnabled(False)
        else:
            button.clicked.connect(self.openAddModifiersDialog)
        body.addWidget(button)

        button = QPushButton("+P")
        button.setEnabled(False)
        button.setFixedWidth(SIZE_B)
        body.addWidget(button)

        button = QPushButton("Edit")
        button.setFixedWidth(SIZE_B)
        button.clicked.connect(self.openEditPriceDialog)
        body.addWidget(button)

    def onQuantityChange(self):
        self.quantity = self.quantity_spinbox.value()
        self.price_label.setText(str(self.price_per_cookie * self.quantity))

    def openAddModifiersDialog(self):
        dialog = AddModifiersDialog(self.cookie)
        if dialog.exec_():
            print("Ok")
        else:
            print("Cancel")

    def openEditPriceDialog(self):
        dialog = EditPriceDialog(self.price_per_cookie)
        if dialog.exec_():
            self.price_per_cookie = dialog.getPrice()
            self.price_label.setText(str(self.price_per_cookie * self.quantity))
        else:
            pass


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
        button.setFixedWidth(SIZE_B)
        button.setIcon(QIcon(str(RES_PATH / 'icon-add.png')))
        layout.addWidget(button, 0)

        widget = QWidget()
        layout = QHBoxLayout(widget)
        row_layout.addWidget(widget)
        layout.addWidget(LabelWidget('Tax'), 1)
        button = QPushButton("")
        button.setFixedWidth(SIZE_B)
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
