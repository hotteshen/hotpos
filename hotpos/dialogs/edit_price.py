from PyQt5.QtWidgets import QVBoxLayout, QDialog, QDialogButtonBox, QLineEdit

from ..config import DIALOG_MIN_SIZE_A
from ..widgets.numberpad import NumberPadWidget


class EditPriceDialog(QDialog):

    def __init__(self, cookie, parent=None):
        super().__init__(parent=parent)

        self.cookie = cookie

        # self.setMinimumSize(*DIALOG_MIN_SIZE_A)
        self.setWindowTitle("Edit Price")

        root_layout = QVBoxLayout(self)

        price_label = QLineEdit()
        price_label.setText(str(cookie['price']))
        price_label.setReadOnly(True)
        root_layout.addWidget(price_label)

        def onChangeValue(value: str):
            price_label.setText(value)

        numberpad = NumberPadWidget(cookie['price'])
        numberpad.setOnChangeValueListener(onChangeValue)
        root_layout.addWidget(numberpad)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonbox = QDialogButtonBox(QBtn)
        root_layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)
