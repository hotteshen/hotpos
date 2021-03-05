from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QSizePolicy

from ..config import SIZE_C, SUB_CAT_LIST_HEIGHT
from .label import LabelWidget


class SubCategoryItemWidget(QWidget):
    def __init__(self, name: str, parent: QWidget = None):
        super(SubCategoryItemWidget, self).__init__(parent=parent)

        root_layout = QVBoxLayout(self)

        name = LabelWidget(name).setCenter()
        name.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        name.setFixedWidth(SIZE_C)
        root_layout.addWidget(name)


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
        item_widget = QListWidgetItem()
        self.addItem(item_widget)
        custom_item_widget = SubCategoryItemWidget(name)
        item_widget.setSizeHint(custom_item_widget.sizeHint())
        self.setItemWidget(item_widget, custom_item_widget)
