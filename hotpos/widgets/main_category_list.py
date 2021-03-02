from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap

from ..config import RES_PATH, MAIN_CAT_ICON_SIZE, MAIN_CAT_LIST_WIDTH
from .label import LabelWidget


class MainCategory:

    def __init__(self, name: str, image: str):
        self.name = name
        self.image = image


class MainCategoryItemWidget(QWidget):
    def __init__(self, item: MainCategory, parent=None):
        super(MainCategoryItemWidget, self).__init__(parent)

        root_layout = QVBoxLayout(self)

        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)
        image_map = QPixmap(str(RES_PATH / 'category_images' / item.image))
        image_map = image_map.scaled(QSize(*MAIN_CAT_ICON_SIZE), Qt.KeepAspectRatio)
        image_label.setPixmap(image_map)
        root_layout.addWidget(image_label)

        name = LabelWidget(item.name).setCenter()
        name.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        root_layout.addWidget(name)


class MainCategoryListWidget(QListWidget):

    def sizeHint(self):
        size = QSize()
        size.setHeight(super(MainCategoryListWidget, self).sizeHint().height())
        size.setWidth(MAIN_CAT_LIST_WIDTH)
        return size

    def addMainCategory(self, item: MainCategory):
        item_widget = QListWidgetItem(self)
        self.addItem(item_widget)
        custom_item_widget = MainCategoryItemWidget(item)
        item_widget.setSizeHint(custom_item_widget.sizeHint())
        self.setItemWidget(item_widget, custom_item_widget)
