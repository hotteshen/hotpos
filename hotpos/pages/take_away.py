from PyQt5.QtWidgets import QHBoxLayout, QWidget, QLabel, QListWidget, QListWidgetItem

from ..widgets.group_box import GroupBoxWidget
from ..widgets.main_category_list import MainCategoryListWidget, MainCategory
from ..widgets.sub_category_list import SubCategoryListWidget


class TakeAwayPage(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QHBoxLayout()
        self.setLayout(root_layout)

        self.main_category_list_widget = MainCategoryListWidget()
        self.main_category_list_widget.itemClicked.connect(self.showSubCategoryList)
        root_layout.addWidget(self.main_category_list_widget, 0)

        gb = GroupBoxWidget()
        root_layout.addWidget(gb, 1)
        gb_root = gb.getRootLayout()

        self.sub_category_list_widget = SubCategoryListWidget()
        self.sub_category_list_widget.itemClicked.connect(self.showItemList)
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
                    {
                        'name': 'In Stock',
                        'image': None,
                        'item_list': [
                            {'name': 'Burger', 'image': None},
                        ],
                    },
                ],
            },
            {
                'name': 'Drinks',
                'image': 'main-category-drink.png',
                'sub_category_list': [],
            },
        ]
        self.showMainCategoryList()

    def showMainCategoryList(self):
        self.item_list_widget.clear()
        self.sub_category_list_widget.clear()
        self.main_category_list_widget.clear()
        for cat in self.category_data:
            cat_obj = MainCategory(cat['name'], cat['image'])
            self.main_category_list_widget.addItem(cat_obj)

    def showSubCategoryList(self):
        self.item_list_widget.clear()
        self.sub_category_list_widget.clear()
        main_cat = self.main_category_list_widget.currentRow()
        for cat in self.category_data[main_cat]['sub_category_list']:
            self.sub_category_list_widget.addItem(cat['name'])

    def showItemList(self):
        self.item_list_widget.clear()
        main_cat = self.main_category_list_widget.currentRow()
        sub_cat = self.sub_category_list_widget.currentRow()
        for it in self.category_data[main_cat]['sub_category_list'][sub_cat]['item_list']:
            list_item = QListWidgetItem(it['name'])
            self.item_list_widget.addItem(list_item)
