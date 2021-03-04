from functools import partial

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QSizePolicy


class NumberPadWidget(QWidget):

    def __init__(self, value: float, parent=None):
        super().__init__(parent=None)
        self.value = str(value)

        button_layout = QGridLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        key_codes = [
            1, 2, 3,
            4, 5, 6,
            7, 8, 9,
            'CE', 0, '.',
        ]
        positions = [(i, j) for i in range(4) for j in range(3)]
        for position, code in zip(positions, key_codes):
            button = QPushButton(str(code))
            button.clicked.connect(partial(self.buttonPress, code))
            button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            if code == 'CE':
                button.setProperty('class', 'danger')
            button_layout.addWidget(button, *position)

        root_layout = QVBoxLayout(self)
        root_layout.addLayout(button_layout)

        self.onChangeValue = None

    def buttonPress(self, code):
        if code in range(10):
            if len(self.value) < 12 and '.' in self.value:
                self.value += str(code)
            elif len(self.value) < 11:
                if self.value == '0':
                    self.value = str(code)
                else:
                    self.value += str(code)
        elif code == '.':
            if '.' not in self.value:
                self.value += str(code)
        elif code == 'CE':
            self.value = '0'
        if self.onChangeValue:
            self.onChangeValue(self.value)

    def setOnChangeValueListener(self, func):
        self.onChangeValue = func
