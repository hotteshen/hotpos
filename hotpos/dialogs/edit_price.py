from PyQt5.QtWidgets import QVBoxLayout, QDialog, QDialogButtonBox, QLineEdit

from ..widgets.numberpad import NumberPadWidget


class EditPriceDialog(QDialog):

    def __init__(self, price_per_cookie: float, parent=None):
        super().__init__(parent=parent)

        self.price_per_cookie = price_per_cookie

        # self.setMinimumSize(*DIALOG_MIN_SIZE_A)
        self.setWindowTitle("Edit Price")

        root_layout = QVBoxLayout(self)

        price_label = QLineEdit()
        price_label.setText(str(self.price_per_cookie))
        price_label.setReadOnly(True)
        root_layout.addWidget(price_label)

        def onChangeValue(value: str):
            price_label.setText(value)
            self.price_per_cookie = float(value)

        numberpad = NumberPadWidget(self.price_per_cookie)
        numberpad.setOnChangeValueListener(onChangeValue)
        root_layout.addWidget(numberpad)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonbox = QDialogButtonBox(QBtn)
        root_layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

    def getPrice(self) -> float:
        return self.price_per_cookie
