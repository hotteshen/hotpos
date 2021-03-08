from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QDialog, QDialogButtonBox, QCompleter, QLineEdit, QComboBox

from ..config import DIALOG_MIN_SIZE_D


class AddCustomerDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setMinimumSize(*DIALOG_MIN_SIZE_D)
        self.setWindowTitle("Add Customer")

        root_layout = QVBoxLayout(self)

        self.search_edit = QLineEdit()
        completer = QCompleter(["dog", "rabbit", "cock",])
        self.search_edit.setCompleter(completer)
        self.search_edit.setPlaceholderText("Search Customer")
        root_layout.addWidget(self.search_edit)

        layout = QHBoxLayout()
        root_layout.addLayout(layout)
        self.first_name_edit = QLineEdit()
        self.first_name_edit.setPlaceholderText("First Name")
        layout.addWidget(self.first_name_edit)
        self.last_name_edit = QLineEdit()
        self.last_name_edit.setPlaceholderText("Last Name")
        layout.addWidget(self.last_name_edit)

        layout = QHBoxLayout()
        root_layout.addLayout(layout)
        self.country_combo = QComboBox()
        layout.addWidget(self.country_combo)
        self.district_combo = QComboBox()
        layout.addWidget(self.district_combo)
        self.city_combo = QComboBox()
        layout.addWidget(self.city_combo)

        self.phone_number_edit = QLineEdit()
        self.phone_number_edit.setPlaceholderText("Phone Number")
        root_layout.addWidget(self.phone_number_edit)

        self.address_edit = QLineEdit()
        self.address_edit.setPlaceholderText("Address 1")
        root_layout.addWidget(self.address_edit)

        self.address2_edit = QLineEdit()
        self.address2_edit.setPlaceholderText("Address 2")
        root_layout.addWidget(self.address2_edit)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonbox = QDialogButtonBox(QBtn)
        root_layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)
