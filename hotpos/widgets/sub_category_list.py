from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QListWidget, QListWidgetItem

from ..config import SUB_CAT_LIST_HEIGHT


class _ListWidget(QListWidget):

    def sizeHint(self):
        size = QSize()
        size.setHeight(SUB_CAT_LIST_HEIGHT)
        size.setWidth(super(_ListWidget, self).sizeHint().width())
        return size


class SubCategoryListWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QVBoxLayout(self)
        self.list_view = _ListWidget()
        self.list_view.setFlow(QListWidget.LeftToRight)
        root_layout.addWidget(self.list_view)

        self.itemClicked = self.list_view.itemClicked
        self.setCurrentRow = self.list_view.setCurrentRow
        self.currentRow = self.list_view.currentRow
        self.clear = self.list_view.clear

    def addItem(self, name: str):
        item_widget = QListWidgetItem(name)
        self.list_view.addItem(item_widget)
