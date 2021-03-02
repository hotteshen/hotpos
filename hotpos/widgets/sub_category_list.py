from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from ..config import SUB_CAT_LIST_HEIGHT


class _ListWidget(QListWidget):

    def sizeHint(self):
        size = QSize()
        size.setHeight(SUB_CAT_LIST_HEIGHT)
        size.setWidth(super(_ListWidget, self).sizeHint().width())
        return size


class SubCategoryListWidget(QListWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFlow(QListWidget.LeftToRight)

    def sizeHint(self):
        size = QSize()
        size.setHeight(SUB_CAT_LIST_HEIGHT)
        size.setWidth(super(SubCategoryListWidget, self).sizeHint().width())
        return size

    def addSubCategory(self, name: str):
        item_widget = QListWidgetItem(name)
        self.addItem(item_widget)
