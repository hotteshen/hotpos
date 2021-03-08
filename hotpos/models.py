from typing import List


class CookieModifier:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class CookieModifierCollection:

    def __init__(self, quantity: int, modifier_list: List[CookieModifier]):
        self.quantity = quantity
        self.modifier_list = modifier_list


class Cookie:

    def __init__(self, cookie_id: int, name: str, price: float, modifier_list: List[CookieModifier]):
        self.id = cookie_id
        self.name = name
        self.price = price
        self.modifier_list = modifier_list


class CookieOrder:

    def __init__(self, cookie: Cookie, quantity: int, modifier_collection_list: List[CookieModifierCollection], custom_price: float, note: str):
        self.cookie = cookie
        self.quantity = quantity
        self.modifier_collection_list = modifier_collection_list
        self.custom_price = custom_price
        self.note = note


class Customer:

    pass


class OrderCollection:

    def __init__(self, cookie_order_list: List[CookieOrder], tax: float, discount: float, discount_percentage: float, customer: Customer):
        self.cookie_order_list = cookie_order_list
        self.tax = tax
        self.discount = discount
        self.discount_percentager = discount_percentage
        self.customer = customer
