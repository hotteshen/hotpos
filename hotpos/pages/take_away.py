from PyQt5.QtWidgets import QHBoxLayout, QWidget, QLabel, QListWidget, QListWidgetItem

from ..widgets.group_box import GroupBoxWidget


class TakeAwayPage(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = QHBoxLayout()
        self.setLayout(root_layout)

        self.main_category_list_widget = QListWidget()
        root_layout.addWidget(self.main_category_list_widget, 0)

        gb = GroupBoxWidget()
        root_layout.addWidget(gb, 1)
        gb_root = gb.getRootLayout()
        self.sub_category_list_widget = QListWidget()
        self.sub_category_list_widget.setFlow(QListWidget.LeftToRight)
        gb_root.addWidget(self.sub_category_list_widget, 0)
        gb_root.addWidget(QLabel("Hello"), 1)

        gb = GroupBoxWidget(title='Order ID: #18')
        root_layout.addWidget(gb, 1)
        gb_root = gb.getRootLayout()

        sample_categories = [
            {
                'name': 'Food',
                'image': None,
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
                'image': None,
                'sub_categorie_list': [],
            },
        ]
        self.showCategoryList(sample_categories)

    def showCategoryList(self, categories, main_cat=0, sub_cat=0, item=0):
        for cat in categories:
            list_item = QListWidgetItem(cat['name'])
            self.main_category_list_widget.addItem(list_item)
            self.main_category_list_widget.setCurrentRow(main_cat)
        for cat in categories[main_cat]['sub_category_list']:
            list_item = QListWidgetItem(cat['name'])
            self.sub_category_list_widget.addItem(list_item)
            self.sub_category_list_widget.setCurrentRow(sub_cat)
