from PyQt5.QtWidgets import QHBoxLayout, QWidget, QLabel, QListWidget, QListWidgetItem

from ..widgets.group_box import GroupBoxWidget
from ..widgets.main_category_list import MainCategoryListWidget, MainCategory


class TakeAwayPage(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QHBoxLayout()
        self.setLayout(root_layout)

        self.main_category_list_widget = MainCategoryListWidget()
        root_layout.addWidget(self.main_category_list_widget, 0)

        gb = GroupBoxWidget()
        root_layout.addWidget(gb, 1)
        gb_root = gb.getRootLayout()
        self.sub_category_list_widget = QListWidget()
        self.sub_category_list_widget.setFlow(QListWidget.LeftToRight)
        gb_root.addWidget(self.sub_category_list_widget, 0)
        self.item_list_widget = QListWidget()
        gb_root.addWidget(self.item_list_widget, 1)

        gb = GroupBoxWidget(title='Order ID: #18')
        root_layout.addWidget(gb, 1)
        gb_root = gb.getRootLayout()

        self.category_data = [
            {
                'name': 'Food',
                'image': 'main-category-food.png',
                'sub_category_list': [
                    {
                        'name': 'All',
                        'image': None,
                        'item_list': [
                            {'name': 'Burger', 'image': None},
                            {'name': 'Chicken Wings', 'image': None},
                        ],
                    },
                ],
            },
            {
                'name': 'Drinks',
                'image': 'main-category-drink.png',
                'sub_categorie_list': [],
            },
        ]
        self.showMainCategory(main_cat=0)

    def showMainCategory(self, main_cat=-1):
        self.main_category_list_widget.clear()
        for cat in self.category_data:
            cat_obj = MainCategory(cat['name'], cat['image'])
            self.main_category_list_widget.addItem(cat_obj)
            if main_cat >= 0:
                self.showSubCategory(main_cat=main_cat, sub_cat=0)

    def showSubCategory(self, main_cat=-1, sub_cat=-1):
        if main_cat < 0:
            return
        self.main_category_list_widget.setCurrentRow(main_cat)
        self.sub_category_list_widget.clear()
        for cat in self.category_data[main_cat]['sub_category_list']:
            list_item = QListWidgetItem(cat['name'])
            self.sub_category_list_widget.addItem(list_item)
            if sub_cat >= 0:
                self.showItem(main_cat=main_cat, sub_cat=sub_cat)

    def showItem(self, main_cat=-1, sub_cat=-1, item=-1):
        if main_cat < 0 or sub_cat < 0:
            return
        self.sub_category_list_widget.setCurrentRow(sub_cat)
        self.item_list_widget.clear()
        for it in self.category_data[main_cat]['sub_category_list'][sub_cat]['item_list']:
            list_item = QListWidgetItem(it['name'])
            self.item_list_widget.addItem(list_item)
            if item >= 0:
                self.item_list_widget.setCurrentRow(item)
