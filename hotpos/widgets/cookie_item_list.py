from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QLabel, QSizePolicy

from ..config import ITEM_ICON_SIZE, MAIN_CAT_LIST_WIDTH
from .label import LabelWidget


class CookieItem:

    def __init__(self, name: str, image: str):
        self.name = name
        self.image = image


class ItemWidget(QWidget):

    def __init__(self, item: CookieItem, parent=None):
        super(ItemWidget, self).__init__(parent)
        self.app = QApplication.instance()

        root_layout = QVBoxLayout(self)

        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)
        image_map = self.app.backend().getImage(item.image)
        image_map = image_map.scaled(QSize(*ITEM_ICON_SIZE), Qt.KeepAspectRatio)
        image_label.setPixmap(image_map)
        root_layout.addWidget(image_label)

        name = LabelWidget(item.name).setCenter()
        name.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        root_layout.addWidget(name)


class CookieItemListWidget(QListWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFlow(QListWidget.LeftToRight)
        self.setGridSize(QSize(ITEM_ICON_SIZE[0], ITEM_ICON_SIZE[1] + 24))
        self.setResizeMode(QListWidget.Adjust)
        self.setViewMode(QListWidget.IconMode)

    def sizeHint(self):
        size = QSize()
        size.setHeight(super(CookieItemListWidget, self).sizeHint().height())
        size.setWidth(MAIN_CAT_LIST_WIDTH)
        return size

    def addCookieItem(self, item: CookieItem):
        item_widget = QListWidgetItem(self)
        self.addItem(item_widget)
        custom_item_widget = ItemWidget(item)
        item_widget.setSizeHint(custom_item_widget.sizeHint())
        self.setItemWidget(item_widget, custom_item_widget)
