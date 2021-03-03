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
                            {'name': 'Wine', 'image': 'item-wine.jpg', 'modifier_list': []},
                            {'name': 'Banana Salad', 'image': 'item-banana-salad.jpg', 'modifier_list': ['BBQ', 'Buffalo',]},
                            {'name': 'Sandwitch', 'image': 'item-sandwitch.jpg', 'modifier_list': ['BBQ', 'Buffalo', 'Spicy BBQ', 'Honey Mustard',]},
                            {'name': 'Chicken', 'image': 'item-chicken.jpg', 'modifier_list': ['BBQ', 'Buffalo', 'Spicy BBQ', 'Honey Mustard',]},
                            {'name': 'Instant Noodle', 'image': 'item-instant-noodle.jpg', 'modifier_list': []},
                        ],
                    },
                    {
                        'name': 'In Stock',
                        'image': None,
                        'item_list': [
                            {'name': 'Chicken', 'image': 'item-chicken.jpg', 'modifier_list': ['BBQ', 'Buffalo', 'Spicy BBQ', 'Honey Mustard',]},
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
                            {'name': 'Instant Noodle', 'image': 'item-instant-noodle.jpg', 'modifier_list': []},
                        ],
                    },
                ]
            },
            {
                'name': 'Drink',
                'image': 'main-category-drink.png',
                'sub_category_list': [
                    {
                        'name': 'All',
                        'image': None,
                        'item_list': [
                            {'name': 'Wine', 'image': 'item-wine.jpg', 'modifier_list': []},
                        ],
                    },
                ]
            },
        ]
