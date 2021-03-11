from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QDialog, QDialogButtonBox, QTabWidget, QSpinBox

from ..config import DIALOG_MIN_SIZE_C
from ..models import OrderCollection
from ..widgets.label import LabelWidget


class AddDiscountDialog(QDialog):

    def __init__(self, order_collection: OrderCollection, parent=None):
        super().__init__(parent=parent)

        self.order_collection = order_collection

        self.setMinimumSize(*DIALOG_MIN_SIZE_C)
        self.setWindowTitle("Add Discount")

        root_layout = QVBoxLayout(self)

        tabs = QTabWidget()
        root_layout.addWidget(tabs)

        percentage_tab = QWidget()
        layout = QHBoxLayout(percentage_tab)
        self.percentage_spinbox = QSpinBox()
        self.percentage_spinbox.setRange(0, 100)
        layout.addWidget(self.percentage_spinbox, 1)
        layout.addWidget(LabelWidget("%"), 0)
        tabs.addTab(percentage_tab, "Percentage")

        amount_tab = QWidget()
        layout = QHBoxLayout(amount_tab)
        self.amount_spinbox = QSpinBox()
        self.amount_spinbox.setRange(0, int(self.order_collection.sub_total))
        layout.addWidget(self.amount_spinbox, 1)
        layout.addWidget(LabelWidget("LBP"), 0)
        tabs.addTab(amount_tab, "Amount")

        self.percentage_spinbox.valueChanged.connect(self.onPercentageChange)
        self.amount_spinbox.valueChanged.connect(self.onAmountChange)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonbox = QDialogButtonBox(QBtn)
        root_layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.onOkClick)
        buttonbox.rejected.connect(self.reject)

    def onOkClick(self):
        self.order_collection.discount = float(self.amount_spinbox.value())
        self.order_collection.discount_percentage = float(self.percentage_spinbox.value())
        self.accept()

    def onPercentageChange(self):
        if self.percentage_spinbox.value() != 0:
            self.amount_spinbox.setValue(0)

    def onAmountChange(self):
        if self.amount_spinbox.value() != 0:
            self.percentage_spinbox.setValue(0)
