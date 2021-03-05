from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QDialog, QDialogButtonBox, QTabWidget, QSpinBox

from ..config import DIALOG_MIN_SIZE_C
from ..widgets.label import LabelWidget


class AddDiscountDialog(QDialog):

    def __init__(self, price_per_cookie: float, parent=None):
        super().__init__(parent=parent)

        self.price_per_cookie = price_per_cookie

        self.setMinimumSize(*DIALOG_MIN_SIZE_C)
        self.setWindowTitle("Add Discount")

        root_layout = QVBoxLayout(self)

        tabs = QTabWidget()
        root_layout.addWidget(tabs)

        percentage_tab = QWidget()
        layout = QHBoxLayout(percentage_tab)
        percentage_spinbox = QSpinBox()
        percentage_spinbox.setRange(1, 100)
        layout.addWidget(percentage_spinbox, 1)
        layout.addWidget(LabelWidget("%"), 0)
        tabs.addTab(percentage_tab, "Percentage")

        amount_tab = QWidget()
        layout = QHBoxLayout(amount_tab)
        amount_spinbox = QSpinBox()
        amount_spinbox.setRange(1, 100)
        layout.addWidget(amount_spinbox, 1)
        layout.addWidget(LabelWidget("LBP"), 0)
        tabs.addTab(amount_tab, "Amount")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonbox = QDialogButtonBox(QBtn)
        root_layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)
