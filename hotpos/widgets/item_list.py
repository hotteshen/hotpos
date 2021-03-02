from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap

from ..config import RES_PATH, ITEM_ICON_SIZE, MAIN_CAT_LIST_WIDTH
from .label import LabelWidget


class Item:

    def __init__(self, name: str, image: str):
        self.name = name
        self.image = image


class ItemWidget(QWidget):

    def __init__(self, item: Item, parent=None):
        super(ItemWidget, self).__init__(parent)

        root_layout = QVBoxLayout(self)

        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)
        image_map = QPixmap(str(RES_PATH / 'category_images' / item.image))
        image_map = image_map.scaled(QSize(*ITEM_ICON_SIZE), Qt.KeepAspectRatio)
        image_label.setPixmap(image_map)
        root_layout.addWidget(image_label)

        name = LabelWidget(item.name).setCenter()
        name.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        root_layout.addWidget(name)


class _ListWidget(QListWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFlow(QListWidget.LeftToRight)
        self.setGridSize(QSize(ITEM_ICON_SIZE[0], ITEM_ICON_SIZE[1] + 24))
        self.setResizeMode(QListWidget.Adjust)
        self.setViewMode(QListWidget.IconMode)

    def sizeHint(self):
        size = QSize()
        size.setHeight(super(_ListWidget, self).sizeHint().height())
        size.setWidth(MAIN_CAT_LIST_WIDTH)
        return size


class ItemListWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QVBoxLayout(self)
        self.list_view = _ListWidget()
        root_layout.addWidget(self.list_view)

        self.itemClicked = self.list_view.itemClicked
        self.setCurrentRow = self.list_view.setCurrentRow
        self.currentRow = self.list_view.currentRow
        self.clear = self.list_view.clear

    def addItem(self, item: Item):
        item_widget = QListWidgetItem(self.list_view)
        self.list_view.addItem(item_widget)
        custom_item_widget = ItemWidget(item)
        item_widget.setSizeHint(custom_item_widget.sizeHint())
        self.list_view.setItemWidget(item_widget, custom_item_widget)
