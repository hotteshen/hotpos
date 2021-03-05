from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSpinBox

from ..config import SIZE_C


class HorizontalSpinBox(QSpinBox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet('QSpinBox::up-button  { subcontrol-position: center right; } QSpinBox::down-button  { subcontrol-position: center left; }')
        self.setAlignment(Qt.AlignCenter)
        self.setFixedWidth(SIZE_C)
        self.lineEdit().setReadOnly(True)
