from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QSizePolicy, QLineEdit

from ..config import APP_NAME
from ..widgets.clock import ClockWidget
from ..widgets.label import LabelWidget


class LoginPage(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = QApplication.instance()
        self.code = ''

        info_layout = QVBoxLayout()
        info_layout.addWidget(QWidget(), 1)
        logo = LabelWidget(APP_NAME).setSize(30).setCenter()
        info_layout.addWidget(logo, 0)
        clock = ClockWidget()
        info_layout.addWidget(clock, 0)
        info_layout.addWidget(QWidget(), 1)

        display_layout = QHBoxLayout()
        self.code_inputs = [QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit()]
        for code_input in self.code_inputs:
            code_input.setAlignment(Qt.AlignCenter)
            code_input.setEchoMode(QLineEdit.Password)
            code_input.setStyleSheet('QLineEdit { font-size: %dpx; border: none; }' %  30)
            code_input.setReadOnly(True)
            display_layout.addWidget(code_input)

        button_layout = QGridLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        key_codes = [
            1, 2, 3,
            4, 5, 6,
            7, 8, 9,
            'DEL', 0, 'OK',
        ]
        positions = [(i, j) for i in range(4) for j in range(3)]
        for position, code in zip(positions, key_codes):
            button = QPushButton(str(code))
            if code == 'DEL':
                button.setProperty('class', 'danger')
            button.clicked.connect(partial(self.buttonPress, code))
            button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            button_layout.addWidget(button, *position)

        code_layout = QVBoxLayout()
        code_layout.addWidget(QWidget(), 1)
        code_layout.addLayout(display_layout, 0)
        code_layout.addLayout(button_layout, 0)
        code_layout.addWidget(QWidget(), 1)

        root_layout = QHBoxLayout()
        root_layout.addLayout(info_layout, 1)
        root_layout.addLayout(code_layout, 1)
        self.setLayout(root_layout)

    def buttonPress(self, code):
        if code in range(10):
            if len(self.code) < 4:
                self.code_inputs[len(self.code)].setText(str(code))
                self.code += str(code)
        elif code == 'DEL':
            for code_input in self.code_inputs:
                code_input.setText('')
            self.code = ''
        elif code == 'OK':
            if len(self.code) == 4:
                result = self.app.backend().logIn(self.code)
                if result:
                    self.app.main_window.showPage('home')
                else:
                    self.code = ''
                for code_input in self.code_inputs:
                    code_input.setText('')
