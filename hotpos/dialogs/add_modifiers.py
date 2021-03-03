from functools import partial

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QDialog, QDialogButtonBox, QPushButton, QGroupBox, QCheckBox, QTextEdit

from ..config import SIZE_C
from ..widgets.label import LabelWidget


class AddModifiersDialog(QDialog):

    def __init__(self, cookie, parent=None):
        super().__init__(parent=parent)

        self.cookie = cookie

        self.setWindowTitle("Add Modifiers")

        root_layout = QVBoxLayout(self)

        layout = QHBoxLayout()
        root_layout.addLayout(layout)
        button_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'CE']
        for v in button_values:
            button = QPushButton(str(v))
            button.clicked.connect(partial(self.onQuantityNumpadClick, v))
            layout.addWidget(button)
            if v == 'CE':
                button.setProperty('class', 'danger')

        self.quantity = 0

        gb = QGroupBox("Quantity")
        root_layout.addWidget(gb)
        layout = QHBoxLayout()
        gb.setLayout(layout)
        self.quantity_label = LabelWidget(str(self.quantity))
        layout.addWidget(self.quantity_label)
        layout.addStretch()

        gb = QGroupBox("Modifiers")
        root_layout.addWidget(gb)
        layout = QVBoxLayout()
        gb.setLayout(layout)
        modifier_list = self.cookie['modifier_list']
        for modifier in modifier_list:
            checkbox = QCheckBox(modifier)
            layout.addWidget(checkbox)

        gb = QGroupBox("")
        gb.setMinimumHeight(SIZE_C)
        gb.setMaximumHeight(SIZE_C * 2)
        root_layout.addWidget(gb)

        gb = QGroupBox("Kitchen Note")
        root_layout.addWidget(gb)
        layout = QVBoxLayout()
        gb.setLayout(layout)
        self.kitchen_note_edit = QTextEdit()
        layout.addWidget(self.kitchen_note_edit)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel | QDialogButtonBox.Apply
        buttonBox = QDialogButtonBox(QBtn)
        root_layout.addWidget(buttonBox)

    def onQuantityNumpadClick(self, v):
        if v == 'CE':
            self.quantity = 0
        elif len(str(self.quantity)) >= 2:
            pass
        elif v == 0 and self.quantity == 0:
            pass
        else:
            self.quantity = int(str(self.quantity) + str(v))
        self.quantity_label.setText(str(self.quantity))
