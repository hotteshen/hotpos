from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QDialog, QDialogButtonBox, QPushButton, QGroupBox, QCheckBox, QTextEdit, QScrollArea, QSizePolicy

from ..config import RES_PATH, SIZE_A, SIZE_B, SIZE_C, DIALOG_MIN_SIZE_A
from ..widgets.label import LabelWidget


class ModifierItemWidget(QWidget):

    def __init__(self, quantity: int, modifier_list: list, parent=None):
        super().__init__(parent=parent)

        root_layout = QVBoxLayout(self)
        self.setFixedWidth(SIZE_C * 2)
        self.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)

        header = QHBoxLayout()
        root_layout.addLayout(header)

        name_label = LabelWidget("Quantity: %d" % quantity)
        header.addWidget(name_label, 1)

        delete_button = QPushButton("")
        delete_button.setFixedHeight(SIZE_A)
        delete_button.setFixedWidth(SIZE_A)
        delete_button.setIcon(QIcon(str(RES_PATH / 'icon-delete.png')))
        delete_button.clicked.connect(lambda: self.setParent(None))
        delete_button.setFixedWidth(SIZE_B)
        header.addWidget(delete_button, 0)

        body = QVBoxLayout()
        root_layout.addLayout(body)
        for modifier in modifier_list:
            body.addWidget(LabelWidget(str(modifier)))
        
        root_layout.addStretch()


class AddModifiersDialog(QDialog):

    def __init__(self, cookie, parent=None):
        super().__init__(parent=parent)

        self.cookie = cookie

        self.setMinimumSize(*DIALOG_MIN_SIZE_A)
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
        gb.setMaximumHeight(SIZE_C * 2)
        root_layout.addWidget(gb)
        gb_root = QVBoxLayout(gb)
        modifier_checklist_widget = QWidget()
        modifier_checklist_layout = QVBoxLayout(modifier_checklist_widget)
        modifier_checklist_layout.addStretch()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(modifier_checklist_widget)
        gb_root.addWidget(scroll)

        self.modifier_checkbox_list = []
        modifier_list = self.cookie['modifiers']
        for modifier in modifier_list:
            checkbox = QCheckBox(modifier['modifier'])
            checkbox.clicked.connect(self.checkApplicable)
            modifier_checklist_layout.addWidget(checkbox)
            self.modifier_checkbox_list.append(checkbox)

        widget = QWidget()
        self.modifier_item_list_container = QHBoxLayout(widget)
        self.modifier_item_list_container.addStretch()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)
        root_layout.addWidget(scroll)

        gb = QGroupBox("Kitchen Note")
        root_layout.addWidget(gb)
        layout = QVBoxLayout()
        gb.setLayout(layout)
        self.kitchen_note_edit = QTextEdit()
        layout.addWidget(self.kitchen_note_edit)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel | QDialogButtonBox.Apply
        buttonbox = QDialogButtonBox(QBtn)
        root_layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)
        self.apply_button = buttonbox.button(QDialogButtonBox.Apply)
        self.apply_button.clicked.connect(self.onApplyClick)

        self.checkApplicable()

    def onApplyClick(self):
        modifier_list = []
        for i in range(len(self.cookie['modifier_list'])):
            if self.modifier_checkbox_list[i].isChecked():
                modifier_list.append(self.cookie['modifier_list'][i])
        print(modifier_list)
        modifier_item_widget = ModifierItemWidget(self.quantity, modifier_list=modifier_list)
        self.modifier_item_list_container.insertWidget(self.modifier_item_list_container.count() - 1, modifier_item_widget)
        self.quantity = 0
        for checkbox in self.modifier_checkbox_list:
            checkbox.setChecked(False)
        self.checkApplicable()

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
        self.checkApplicable()

    def checkApplicable(self):
        if self.quantity == 0 or not any(map(lambda c: c.isChecked(), self.modifier_checkbox_list)):
            self.apply_button.setEnabled(False)
        else:
            self.apply_button.setEnabled(True)
