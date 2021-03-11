from datetime import timedelta
from datetime import date as Date
import requests
from typing import List
from urllib import request

from cachier import cachier
import jwt
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QPixmap

from .config import API_URL, BASE_URL, RES_PATH, SETTING_NAME, SETTING_VERSION
from .models import User, Customer, Country, District, City


KEY_API_TOKEN = 'token'


class BackendFacade():

    def __init__(self) -> None:
        self.settings = QSettings(SETTING_NAME, SETTING_VERSION)
        self.access_token = self.settings.value(KEY_API_TOKEN)
        self.category_data = None
        self.user = None
        self.company_tax = 0.0

    def checkToken(self) -> bool:
        if self.access_token is None or self.access_token == '':
            return False
        payload = {'Authorization': 'Bearer ' + self.access_token}
        response = requests.request(
                'GET', API_URL + '/categories', data=payload)
        if response.status_code != 200:
            self.settings.setValue(KEY_API_TOKEN, '')
            return False

        self.user = self.getUser()
        self.company_tax = self._getTax()
        return True

    def companyTax(self) -> float:
        return self.company_tax

    def _getTax(self) -> float:
        payload = {'Authorization': 'Bearer ' + self.access_token}
        response = requests.request(
                'GET', API_URL + '/branchinfo/%d' % self.user.branch_id, data=payload)
        if response.status_code != 200:
            return 0.0
        return response.json()['company_tax']

    def getUser(self) -> User:
        if self.access_token is None or self.access_token == '':
            return None
        try:
            options = {'verify_signature': False, 'verify_exp': True, 'verify_nbf': False, 'verify_iat': True, 'verify_aud': False}
            data = jwt.decode(self.access_token, algorithms=["HS256"], options=options)
            return User(**data)
        except:
            return None

    def logIn(self, code: str) -> bool:
        url = API_URL + '/login'
        payload = {'pincode': code}
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

    def getCustomerList(self) -> List[Customer]:
        customer_list = []
        payload = {'Authorization': 'Bearer ' + self.access_token}
        response = requests.request(
                'GET', API_URL + '/customers', data=payload)
        if response.status_code != 200:
            return customer_list
        customer_json_list = response.json()
        for customer_json in customer_json_list:
            customer_list.append(Customer(**customer_json))
        return customer_list

    def getCountryList(self) -> List[Country]:
        payload = {'Authorization': 'Bearer ' + self.access_token}
        response = requests.request(
                'GET', API_URL + '/location', data=payload)
        if response.status_code != 200:
            return []
        json_data = response.json()

        city_json_list = json_data['cities']
        city_list: List[City] = []
        for city_json in city_json_list:
            city = City(**city_json)
            city_list.append(city)

        district_json_list = json_data['districts']
        district_list: List[District] = []
        for district_json in district_json_list:
            district = District(**district_json)
            district.city_list = []
            for city in city_list:
                if city.district_id == district.id:
                    district.city_list.append(city)
            district_list.append(district)

        country_json_list = json_data['countries']
        country_list: List[Country] = []
        for country_json in country_json_list:
            country = Country(**country_json)
            country.district_list = []
            for district in district_list:
                if district.country_id == country.id:
                    country.district_list.append(district)
            country_list.append(country)

        return country_list

    def getCategoryData(self):
        if self.category_data is not None:
            return self.category_data

        main_category_list = []

        payload = {'Authorization': 'Bearer ' + self.access_token}

        response = requests.request(
                'GET', API_URL + '/categories', data=payload)
        if response.status_code != 200:
            self.category_data = []
            return
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

        response = requests.request(
                'GET', API_URL + '/items', data=payload)
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
