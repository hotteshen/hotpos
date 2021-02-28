import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, QDate

from .label import Label

class Clock(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(250, 150)

        root_layout = QVBoxLayout()
        self.setLayout(root_layout)

        self.time_label = Label().setSize(24).setCenter()
        root_layout.addWidget(self.time_label)
        self.date_label = Label().setSize(18).setCenter()
        root_layout.addWidget(self.date_label)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000) # update every second
        self.showTime()

    def showTime(self):
        self.time_label.setText(
            QTime.currentTime().toString('hh:mm:ss')
        )
        self.date_label.setText(
            QDate.currentDate().toString()
        )
