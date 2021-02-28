from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel


class Label(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setSize(self, size: int):
        font = self.font()
        font.setPointSize(size)
        self.setFont(font)
        return self

    def setCenter(self):
        self.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        return self
