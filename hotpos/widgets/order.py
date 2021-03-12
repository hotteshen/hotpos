from typing import Callable, List

from PyQt5.QtGui import QIcon, QMouseEvent
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QSizePolicy, QGroupBox

from ..config import RES_PATH, SIZE_A, SIZE_B
from ..dialogs.add_customer import AddCustomerDialog
from ..dialogs.add_discount import AddDiscountDialog
from ..dialogs.add_modifiers import AddModifiersDialog
from ..dialogs.edit_price import EditPriceDialog
from ..models import Cookie, CookieModifier, CookieOrder, CookieModifierCollection, Customer, OrderCollection, Country
from .group_box import GroupBoxWidget
from .horizontal_spinbox import HorizontalSpinBox
from .label import LabelWidget


class ModifierCollectionWidget(QGroupBox):

    def __init__(self, modifier_collection: CookieModifierCollection, cookie_order: CookieOrder, parent: QWidget = None):
        super().__init__(parent=parent)

        self.modifier_collection = modifier_collection
        self.cookie_order = cookie_order

        root_layout = QHBoxLayout(self)

        name_label = LabelWidget("Quantity: %d" % self.modifier_collection.quantity)
        root_layout.addWidget(name_label, 1)

        modifiers_string = ", ".join([m.modifier for m in self.modifier_collection.modifier_list])
        modifier_label = LabelWidget(modifiers_string)
        root_layout.addWidget(modifier_label, 1)

        delete_button = QPushButton("")
        delete_button.setFixedHeight(SIZE_A)
        delete_button.setFixedWidth(SIZE_A)
        delete_button.setIcon(QIcon(str(RES_PATH / 'icon-delete.png')))
        delete_button.clicked.connect(self.delete)
        delete_button.setFixedWidth(SIZE_B)
        root_layout.addWidget(delete_button, 0)

    def delete(self):
        self.setParent(None)
        self.cookie_order.modifier_collection_list.remove(self.modifier_collection)


class OrderedCookieWidget(QGroupBox):

    def __init__(self, cookie_order: CookieOrder, order_collection: OrderCollection, calculate: Callable, parent=None):
        super().__init__(parent=parent)

        self.cookie_order = cookie_order
        self.order_collection = order_collection
        self.calculate = calculate

        root_layout = QVBoxLayout(self)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        header = QHBoxLayout()
        root_layout.addLayout(header)

        name_label = LabelWidget(self.cookie_order.cookie.name)
        header.addWidget(name_label, 1)

        delete_button = QPushButton("")
        delete_button.setFixedHeight(SIZE_A)
        delete_button.setFixedWidth(SIZE_A)
        delete_button.setIcon(QIcon(str(RES_PATH / 'icon-delete.png')))
        delete_button.clicked.connect(self.delete)
        delete_button.setFixedWidth(SIZE_B)
        header.addWidget(delete_button, 0)

        body = QHBoxLayout()
        root_layout.addLayout(body)

        self.quantity_spinbox = HorizontalSpinBox()
        self.quantity_spinbox.setRange(1, 100)
        self.quantity_spinbox.setValue(self.cookie_order.quantity)
        self.quantity_spinbox.valueChanged.connect(self.onQuantityChange)
        body.addWidget(self.quantity_spinbox)

        self.price_label = LabelWidget(str(self.cookie_order.custom_price)).setCenter()
        body.addWidget(self.price_label)

        button = QPushButton("+M")
        button.setFixedWidth(SIZE_B)
        if len(self.cookie_order.cookie.modifiers) == 0:
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

        footer = QWidget()
        root_layout.addWidget(footer)
        self.modifier_collection_container = QVBoxLayout(footer)

    def delete(self):
        self.setParent(None)
        self.order_collection.cookie_order_list.remove(self.cookie_order)
        self.calculate()

    def onQuantityChange(self):
        self.cookie_order.quantity = self.quantity_spinbox.value()
        self.price_label.setText(str(self.cookie_order.custom_price * self.cookie_order.quantity))
        self.calculate()

    def renderModifierCollectionList(self):
        for i in reversed(range(self.modifier_collection_container.count())):
            widget = self.modifier_collection_container.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        for modifier_collection in self.cookie_order.modifier_collection_list:
            modifier_item_widget = ModifierCollectionWidget(modifier_collection, self.cookie_order)
            self.modifier_collection_container.addWidget(modifier_item_widget)

    def openAddModifiersDialog(self):
        dialog = AddModifiersDialog(self.cookie_order)
        if dialog.exec_():
            self.renderModifierCollectionList()
            self.calculate()

    def openEditPriceDialog(self):
        dialog = EditPriceDialog(self.cookie_order.custom_price)
        if dialog.exec_():
            self.cookie_order.custom_price = dialog.getPrice()
            self.price_label.setText(str(self.cookie_order.custom_price * self.cookie_order.quantity))
            self.calculate()


class OrderWidget(GroupBoxWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QApplication.instance()
        self.order_collection = OrderCollection(
                cookie_order_list=[],
                sub_total=0.0,
                total=0.0,
                tax=0.0,
                discount=0.0,
                discount_percentage=0.0,
                customer=None
        )
        self.customer_list: List[Customer] = []
        self.country_list: List[Country] = []
        self.initUI()

    def addCookieItem(self, main_cat: int, sub_cat: int, cookie_item: int):
        _cookie = self.app.backend().getCategoryData()[main_cat]['sub_category_list'][sub_cat]['item_list'][cookie_item]
        modifier_list = []
        for m in _cookie['modifiers']:
            modifier_list.append(CookieModifier(**m))
        # cookie = Cookie(_cookie['id'], _cookie['name'], _cookie['price'], modifier_list)
        cookie = Cookie(**_cookie)
        cookie_order = CookieOrder(cookie=cookie, quantity=1, modifier_collection_list=[], custom_price=cookie.price, note='')
        self.order_collection.cookie_order_list.append(cookie_order)
        cookie_widget = OrderedCookieWidget(cookie_order, self.order_collection, self.calculate)
        self.cookie_list_layout.insertWidget(self.cookie_list_layout.count() - 1, cookie_widget)
        self.calculate()

    def loadRemoteData(self):
        self.customer_list = self.app.backend().getCustomerList()
        self.order_collection.tax = self.app.backend().companyTax()
        self.country_list = self.app.backend().getCountryList()

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
        self.sub_total_label = LabelWidget(str(self.order_collection.sub_total))
        layout.addWidget(self.sub_total_label, 0)

        widget = QWidget()
        layout = QHBoxLayout(widget)
        row_layout.addWidget(widget)
        layout.addWidget(LabelWidget('Tax'), 1)
        self.tax_label = LabelWidget(str(self.order_collection.tax))
        layout.addWidget(self.tax_label, 0)

        row_layout = QHBoxLayout()
        root_layout.addLayout(row_layout, 0)

        widget = QWidget()
        layout = QHBoxLayout(widget)
        row_layout.addWidget(widget)
        layout.addWidget(LabelWidget('Discount'), 1)
        self.discount_button = LabelWidget("+")
        self.discount_button.mousePressEvent = self.openAddDiscountDialog
        layout.addWidget(self.discount_button, 0)

        widget = QWidget()
        layout = QHBoxLayout(widget)
        row_layout.addWidget(widget)
        layout.addWidget(LabelWidget('Customer'), 1)
        self.customer_button = LabelWidget("+")
        self.customer_button.mousePressEvent = self.openAddCustomerDialog
        layout.addWidget(self.customer_button, 0)

        row = QWidget()
        row_layout = QHBoxLayout(row)
        root_layout.addWidget(row)

        layout = QHBoxLayout()
        row_layout.addLayout(layout)
        layout.addWidget(LabelWidget('Total'), 1)
        self.total_label = LabelWidget(str(self.order_collection.total))
        layout.addWidget(self.total_label, 0)

        row_layout = QHBoxLayout()
        root_layout.addLayout(row_layout, 0)
        row_layout.addWidget(LabelWidget(), 1)
        button = QPushButton("CHECKOUT")
        row_layout.addWidget(button, 1)

    def openAddDiscountDialog(self, e: QMouseEvent):
        dialog = AddDiscountDialog(self.order_collection)
        if dialog.exec_():
            self.calculate()

    def calculate(self):
        self.order_collection.calculate()
        self.sub_total_label.setText(str(self.order_collection.sub_total))
        self.total_label.setText(str(self.order_collection.total))
        if self.order_collection.discount != 0:
            self.discount_button.setText(str(self.order_collection.discount))
        elif self.order_collection.discount_percentage != 0:
            self.discount_button.setText(str(self.order_collection.discount_percentage) + "%")
        else:
            self.discount_button.setText("+")

    def openAddCustomerDialog(self, e: QMouseEvent):
        dialog = AddCustomerDialog(self.order_collection, self.customer_list, self.country_list)
        if dialog.exec_():
            self.customer_button.setText(self.order_collection.customer.first_name)
        else:
            print("Cancel")
