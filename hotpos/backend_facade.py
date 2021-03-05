from datetime import timedelta
from datetime import date as Date
import requests
from urllib import request

from cachier import cachier
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QPixmap

from .config import API_URL, BASE_URL, RES_PATH, SETTING_NAME, SETTING_VERSION


KEY_API_TOKEN = 'token'


class BackendFacade():

    def __init__(self) -> None:
        self.settings = QSettings(SETTING_NAME, SETTING_VERSION)
        self.access_token = ''
        self.category_data = None

    def checkToken(self) -> bool:
        token = self.settings.value(KEY_API_TOKEN)
        if token is None:
            return False
        payload={'Authorization': 'Bearer ' + token}
        response = requests.request('GET', API_URL + '/categories', data=payload)
        if response.status_code != 200:
            self.settings.setValue(KEY_API_TOKEN, '')
            return False
        self.access_token = token
        return True

    def logIn(self, code: str) -> bool:
        url = API_URL + '/login'
        payload={'pincode': code}
        response = requests.request('POST', url, data=payload)
        if response.status_code != 200:
            return False
        self.access_token = response.json()['access_token']
        self.settings.setValue(KEY_API_TOKEN, self.access_token)
        return True

    def logOut(self):
        self.access_token = ''
        self.settings.setValue(KEY_API_TOKEN, '')

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

    def getImage(self, url: str) -> QPixmap:
        try:
            url = BASE_URL + url
            data = _getImageData(url)
            image_map = QPixmap()
            image_map.loadFromData(data)
        except:
            image_map = QPixmap(str(RES_PATH / 'icon.png'))
        return image_map

    def getCategoryData(self):
        if self.category_data != None:
            return self.category_data

        main_category_list = []

        payload={'Authorization': 'Bearer ' + self.access_token}

        response = requests.request('GET', API_URL + '/categories', data=payload)
        if response.status_code != 200:
            self.category_data = []
        category_list = response.json()

        for category in category_list:
            if category['parent_id'] == 1:
                main_category_list.append(category)
        for main_category in main_category_list:
            main_category['sub_category_list'] = []
            main_category['sub_category_list'].append({
                'name': 'All',
                'item_list': [],
            })
            for category in category_list:
                if category['parent_id'] == main_category['id']:
                    category['item_list'] = []
                    main_category['sub_category_list'].append(category)

        response = requests.request('GET', API_URL + '/items', data=payload)
        if response.status_code != 200:
            self.category_data = main_category_list
        item_list = response.json()

        for item in item_list:
            item['image'] = item['image']['image']
            item['price'] = float(item['price'])
            for main_category in main_category_list:
                if item['category_id'] == main_category['id']:
                    main_category['sub_category_list'][0]['item_list'].append(item)
                else:
                    for sub_category in main_category['sub_category_list']:
                        if 'id' in sub_category.keys():
                            if item['category_id'] == sub_category['id']:
                                main_category['sub_category_list'][0]['item_list'].append(item)
                                sub_category['item_list'].append(item)

        self.category_data = main_category_list
        return self.category_data

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


@cachier(stale_after=timedelta(days=3))
def _getImageData(url: str) -> str:
    return request.urlopen(url).read()
