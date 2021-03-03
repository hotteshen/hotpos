from datetime import date as Date


class BackendFacade():

    def getLateOrderList(self):
        return [
            [1212, 15900, Date.today()],
            [1211, 23700, Date.today()],
            [1210, 26200, Date.today()],
        ]

    def getUpcomingOrderList(self):
        return [
            [1212, 15900, Date.today()],
            [1211, 23700, Date.today()],
            [1210, 26200, Date.today()],
        ]

    def getCategoryData(self):
        return [
            {
                'name': 'Food',
                'image': 'main-category-food.png',
                'sub_category_list': [
                    {
                        'name': 'All',
                        'image': None,
                        'item_list': [
                            {'name': 'Wine', 'image': 'item-wine.jpg'},
                            {'name': 'Banana Salad', 'image': 'item-banana-salad.jpg'},
                            {'name': 'Sandwitch', 'image': 'item-sandwitch.jpg'},
                            {'name': 'Chicken', 'image': 'item-chicken.jpg'},
                            {'name': 'Instant Noodle', 'image': 'item-instant-noodle.jpg'},
                        ],
                    },
                    {
                        'name': 'In Stock',
                        'image': None,
                        'item_list': [
                            {'name': 'Chicken', 'image': 'item-chicken.jpg'},
                        ],
                    },
                ],
            },
            {
                'name': 'Fast Foods',
                'image': 'main-category-fast-food.png',
                'sub_category_list': [
                    {
                        'name': 'All',
                        'image': None,
                        'item_list': [
                            {'name': 'Sandwitch', 'image': 'item-sandwitch.jpg'},
                            {'name': 'Instant Noodle', 'image': 'item-instant-noodle.jpg'},
                        ],
                    },
                ]
            },
            {
                'name': 'Fast Foods',
                'image': 'main-category-drink.png',
                'sub_category_list': [
                    {
                        'name': 'All',
                        'image': None,
                        'item_list': [
                            {'name': 'Wine', 'image': 'item-wine.jpg'},
                        ],
                    },
                ]
            },
        ]
