from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QSizePolicy, QGroupBox

from ..config import RES_PATH, SIZE_A, SIZE_B
from ..dialogs.add_discount import AddDiscountDialog
from ..dialogs.add_modifiers import AddModifiersDialog
from ..dialogs.edit_price import EditPriceDialog
from ..models import Cookie, CookieModifier, CookieOrder, CookieModifierCollection, OrderCollection
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

        modifiers_string = ", ".join([m.name for m in self.modifier_collection.modifier_list])
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

    def __init__(self, cookie_order: CookieOrder, parent=None):
        super().__init__(parent=parent)

        self.cookie_order = cookie_order

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
        delete_button.clicked.connect(lambda: self.setParent(None))
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
        if len(self.cookie_order.cookie.modifier_list) == 0:
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

    def onQuantityChange(self):
        self.cookie_order.quantity = self.quantity_spinbox.value()
        self.price_label.setText(str(self.cookie_order.custom_price * self.cookie_order.quantity))

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

    def openEditPriceDialog(self):
        dialog = EditPriceDialog(self.cookie_order.custom_price)
        if dialog.exec_():
            self.cookie_order.custom_price = dialog.getPrice()
            self.price_label.setText(str(self.cookie_order.custom_price * self.quantity))


class OrderWidget(GroupBoxWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QApplication.instance()
        self.order_collection = OrderCollection([], 0.0, 0.0, 0.0, None)
        self.initUI()

    def addCookieItem(self, main_cat: int, sub_cat: int, cookie_item: int):
        _cookie = self.app.backend().getCategoryData()[main_cat]['sub_category_list'][sub_cat]['item_list'][cookie_item]
        modifier_list = []
        for m in _cookie['modifiers']:
            modifier_list.append(CookieModifier(m['modifier'], m['price']))
        cookie = Cookie(_cookie['id'], _cookie['name'], _cookie['price'], modifier_list)
        cookie_order = CookieOrder(cookie, 1, [], cookie.price, '')
        cookie_widget = OrderedCookieWidget(cookie_order)
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
        button.clicked.connect(self.openAddDiscountDialog)
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
        layout.addWidget(LabelWidget('Total'), 1)
        self.sub_total_label = LabelWidget('0.00')
        layout.addWidget(self.sub_total_label, 0)

        row_layout = QHBoxLayout()
        root_layout.addLayout(row_layout, 0)
        row_layout.addWidget(LabelWidget(), 1)
        button = QPushButton("CHECKOUT")
        row_layout.addWidget(button, 1)

    def openAddDiscountDialog(self):
        dialog = AddDiscountDialog(0.0)
        if dialog.exec_():
            print("Ok")
        else:
            print("Cancel")
