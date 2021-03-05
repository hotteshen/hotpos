from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QPushButton, QGroupBox

from ..config import RES_PATH


class TableListWidget(QWidget):

    def __init__(self, floor, parent: QWidget = None):
        super(QWidget, self).__init__(parent=parent)

        root_layout = QVBoxLayout(self)
        gb = QGroupBox(floor['name'])
        root_layout.addWidget(gb)


class TablePage(QWidget):

    def __init__(self, parent: QWidget = None):
        super(QWidget, self).__init__(parent=parent)
        self.app = QApplication.instance()

        root_layout = QVBoxLayout(self)

        layout = QHBoxLayout()
        root_layout.addLayout(layout)
        button = QPushButton("Add New Table")
        layout.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        button.setIcon(QIcon(str(RES_PATH / 'icon-add.png')))
        layout.addWidget(button)

        tabs = QTabWidget()
        root_layout.addWidget(tabs)

        table_data = self.app.backend().getTableData()
        for floor in table_data:
            table_list_widget = TableListWidget(floor)
            tabs.addTab(table_list_widget, floor['name'])
