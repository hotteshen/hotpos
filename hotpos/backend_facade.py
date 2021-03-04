from datetime import date as Date
import requests

from PyQt5.QtCore import QSettings

from .config import API_URL, SETTING_NAME, SETTING_VERSION


KEY_API_TOKEN = 'token'


class BackendFacade():

    def __init__(self) -> None:
        # self.settings = QSettings(SETTING_NAME, SETTING_VERSION)
        self.access_token = ''

    def checkToken(self) -> bool:
        if self.settings.getValue(KEY_API_TOKEN) is None:
            return False

    def login(self, code: str) -> bool:
        url = API_URL + '/login'
        payload={'pincode': code}
        response = requests.request("POST", url, data=payload)
        if response.status_code != 200:
            return False
        self.access_token = response.json()['access_token']
        return True

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
                            {'name': 'Wine', 'image': 'item-wine.jpg', 'price': 1500.0, 'modifier_list': []},
                            {'name': 'Banana Salad', 'image': 'item-banana-salad.jpg', 'price': 1500.0, 'modifier_list': ['BBQ', 'Buffalo',]},
                            {'name': 'Sandwitch', 'image': 'item-sandwitch.jpg', 'price': 1500.0, 'modifier_list': ['BBQ', 'Buffalo', 'Spicy BBQ', 'Honey Mustard',]},
                            {'name': 'Chicken', 'image': 'item-chicken.jpg', 'price': 1500.0, 'modifier_list': ['BBQ', 'Buffalo', 'Spicy BBQ', 'Honey Mustard',]},
                            {'name': 'Instant Noodle', 'image': 'item-instant-noodle.jpg', 'price': 1500.0, 'modifier_list': []},
                        ],
                    },
                    {
                        'name': 'In Stock',
                        'image': None,
                        'item_list': [
                            {'name': 'Chicken', 'image': 'item-chicken.jpg', 'price': 1500.0, 'modifier_list': ['BBQ', 'Buffalo', 'Spicy BBQ', 'Honey Mustard',]},
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
                            {'name': 'Sandwitch', 'image': 'item-sandwitch.jpg', 'price': 1500.0, 'modifier_list': []},
                            {'name': 'Instant Noodle', 'image': 'item-instant-noodle.jpg', 'price': 1500.0, 'modifier_list': []},
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
                            {'name': 'Wine', 'image': 'item-wine.jpg', 'price': 1500.0, 'modifier_list': []},
                        ],
                    },
                ]
            },
        ]

    def getTableData(self):
        return [
            {
                'name': '1st floor',
                'table_list': [],
            },
            {
                'name': '2nd floor',
                'table_list': [],
            },
        ]
