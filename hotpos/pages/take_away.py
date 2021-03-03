from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget

from ..widgets.group_box import GroupBoxWidget
from ..widgets.main_category_list import MainCategoryListWidget, MainCategory
from ..widgets.sub_category_list import SubCategoryListWidget
from ..widgets.cookie_item_list import CookieItemListWidget, CookieItem
from ..widgets.order import OrderWidget


class TakeAwayPage(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = QApplication.instance()

        root_layout = QHBoxLayout()
        self.setLayout(root_layout)

        self.main_category_list_widget = MainCategoryListWidget()
        self.main_category_list_widget.itemClicked.connect(self.showSubCategoryList)
        root_layout.addWidget(self.main_category_list_widget, 0)

        gb = GroupBoxWidget()
        root_layout.addWidget(gb, 1)
        gb_root = gb.getRootLayout()

        self.sub_category_list_widget = SubCategoryListWidget()
        self.sub_category_list_widget.itemClicked.connect(self.showCookieItemList)
        gb_root.addWidget(self.sub_category_list_widget, 0)

        self.cookie_item_list_widget = CookieItemListWidget()
        gb_root.addWidget(self.cookie_item_list_widget, 1)

        gb = OrderWidget()
        root_layout.addWidget(gb, 1)
        gb_root = gb.getRootLayout()

        self.category_data = self.app.backend().getCategoryData()
        self.showMainCategoryList()

    def showMainCategoryList(self):
        self.cookie_item_list_widget.clear()
        self.sub_category_list_widget.clear()
        self.main_category_list_widget.clear()
        for cat in self.category_data:
            cat_obj = MainCategory(cat['name'], cat['image'])
            self.main_category_list_widget.addMainCategory(cat_obj)
        if len(self.category_data) > 0:
            self.main_category_list_widget.setCurrentRow(0)
            self.showSubCategoryList()

    def showSubCategoryList(self):
        self.cookie_item_list_widget.clear()
        self.sub_category_list_widget.clear()
        main_cat = self.main_category_list_widget.currentRow()
        for cat in self.category_data[main_cat]['sub_category_list']:
            self.sub_category_list_widget.addSubCategory(cat['name'])
        if len(self.category_data[0]['sub_category_list']) > 0:
            self.sub_category_list_widget.setCurrentRow(0)
            self.showCookieItemList()

    def showCookieItemList(self):
        self.cookie_item_list_widget.clear()
        main_cat = self.main_category_list_widget.currentRow()
        sub_cat = self.sub_category_list_widget.currentRow()
        for it in self.category_data[main_cat]['sub_category_list'][sub_cat]['item_list']:
            cookie_obj = CookieItem(it['name'], it['image'])
            self.cookie_item_list_widget.addCookieItem(cookie_obj)
