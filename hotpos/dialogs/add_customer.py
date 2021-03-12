from typing import List, Union

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QDialog, QDialogButtonBox, QCompleter, QLineEdit, QComboBox
from pydantic.typing import NoneType

from ..config import DIALOG_MIN_SIZE_D
from ..models import Customer, Country, District, City, OrderCollection


class AddCustomerDialog(QDialog):

    def __init__(self, order_collection: OrderCollection, customer_list: List[Customer], country_list: List[Country], parent=None):
        super().__init__(parent=parent)

        self.order_collection = order_collection
        self.customer: Union[Customer, NoneType] = None
        self.customer_list = customer_list
        self.customer_search_string_list = [self.getSearchString(c) for c in self.customer_list]
        self.country_list = country_list
        self.country: Union[Country, NoneType] = None
        self.district: Union[District, NoneType] = None
        self.city: Union[City, NoneType] = None

        self.initUI()

    def initUI(self):
        self.setMinimumSize(*DIALOG_MIN_SIZE_D)
        self.setWindowTitle("Add Customer")

        root_layout = QVBoxLayout(self)

        self.search_edit = QLineEdit()
        self.completer = QCompleter(self.customer_search_string_list)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.search_edit.setCompleter(self.completer)
        self.search_edit.setPlaceholderText("Search Customer")
        self.search_edit.textChanged.connect(self.onSearchTextInput)
        root_layout.addWidget(self.search_edit)

        layout = QHBoxLayout()
        root_layout.addLayout(layout)
        self.first_name_edit = QLineEdit()
        self.first_name_edit.setPlaceholderText("First Name")
        layout.addWidget(self.first_name_edit)
        self.last_name_edit = QLineEdit()
        self.last_name_edit.setPlaceholderText("Last Name")
        layout.addWidget(self.last_name_edit)

        layout = QHBoxLayout()
        root_layout.addLayout(layout)
        self.country_combo = QComboBox()
        layout.addWidget(self.country_combo)
        self.district_combo = QComboBox()
        layout.addWidget(self.district_combo)
        self.city_combo = QComboBox()
        layout.addWidget(self.city_combo)

        self.country_combo.addItems([c.nicename for c in self.country_list])
        if len(self.country_list) > 0:
            self.district_combo.addItems([d.name for d in self.country_list[0].district_list])
            if len(self.country_list[0].district_list):
                self.city_combo.addItems([c.name for c in self.country_list[0].district_list[0].city_list])
        self.country_combo.currentIndexChanged.connect(self.onCountryChange)
        self.district_combo.currentIndexChanged.connect(self.onDistrictChange)
        self.city_combo.currentIndexChanged.connect(self.onCityChange)

        self.phone_number_edit = QLineEdit()
        self.phone_number_edit.setPlaceholderText("Phone Number")
        root_layout.addWidget(self.phone_number_edit)

        self.address_edit = QLineEdit()
        self.address_edit.setPlaceholderText("Address 1")
        root_layout.addWidget(self.address_edit)

        self.address2_edit = QLineEdit()
        self.address2_edit.setPlaceholderText("Address 2")
        root_layout.addWidget(self.address2_edit)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonbox = QDialogButtonBox(QBtn)
        root_layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.onOkClick)
        buttonbox.rejected.connect(self.reject)

    def onOkClick(self):
        self.order_collection.customer = self.customer
        self.accept()

    def onSearchTextInput(self):
        if self.search_edit.text() in self.customer_search_string_list:
            for c in self.customer_list:
                if self.search_edit.text() == self.getSearchString(c):
                    self.customer = c
                    self.showCustomer()
                    break

    def showCustomer(self):
        if self.customer is None:
            return
        self.first_name_edit.setText(self.customer.first_name)
        self.last_name_edit.setText(self.customer.last_name)
        self.phone_number_edit.setText(self.customer.phone_number)
        self.address_edit.setText(self.customer.address1)
        self.address2_edit.setText(self.customer.address2)
        for country_index in range(len(self.country_list)):
            if self.customer.country_id == self.country_list[country_index].id:
                self.country_combo.setCurrentIndex(country_index)
        for district_index in range(len(self.country.district_list)):
            if self.customer.country_id == self.country.district_list[district_index].id:
                self.district_combo.setCurrentIndex(district_index)
        for city_index in range(len(self.district.city_list)):
            if self.customer.country_id == self.district.city_list[city_index].id:
                self.city_combo.setCurrentIndex(city_index)

    def onCountryChange(self):
        self.country = self.country_list[self.country_combo.currentIndex()]
        self.district_combo.clear()
        self.district = None
        self.city_combo.clear()
        self.city = None
        self.district_combo.addItems([d.name for d in self.country.district_list])

    def onDistrictChange(self):
        if len(self.country.district_list) > 0:
            self.district = self.country.district_list[self.district_combo.currentIndex()]
        else:
            self.district = None
        self.city_combo.clear()
        self.city = None
        if self.district is not None:
            self.city_combo.addItems([c.name for c in self.district.city_list])

    def onCityChange(self):
        if self.district is not None:
            if len(self.district.city_list) > 0:
                self.city = self.district.city_list[self.city_combo.currentIndex()]
            else:
                self.city = None
        else:
            self.city = None

    def getSearchString(self, c: Customer):
        return "%s %s -- %s" % (c.first_name, c.last_name, c.phone_number)
