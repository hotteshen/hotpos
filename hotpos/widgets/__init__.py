from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


class CenteredLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

    def setRelativeFontSize(self, size: int):
        font = self.font()
        font.setPointSize(14)
        self.setFont(font)
        return self
