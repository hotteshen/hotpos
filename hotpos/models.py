from typing import Any, List, Union

from pydantic import BaseModel
from pydantic.typing import NoneType


class User(BaseModel):

    username: str
    name: str
    branch_id: int
    # ext: int
    # iat: int
    iss: str
    jti: str
    nbf: int
    # role: None
    sub: int


class Customer(BaseModel):

    id: int
    first_name: str
    last_name: str
    country_id: int
    district_id: int
    city_id: int
    phone_number: str
    address1: str
    address2: str


class CookieModifier(BaseModel):

    modifier: str
    price: float


class CookieModifierCollection(BaseModel):

    quantity: int
    modifier_list: List[CookieModifier]


class Cookie(BaseModel):

    appliedModifiers: List[CookieModifier]
    branch_id: int
    category_id: int
    company_id: int
    cost_center_id: int
    created_at: str
    display_order: int
    hasModifiers: bool
    hasPromos: bool
    id: int
    image: str
    imagePath: str
    is_publish: int
    modifiers: List[CookieModifier]
    name: str
    price: float
    promos: List
    qty: int
    recipe_id: Union[NoneType, int]
    selectedPromos: List
    updated_at: str


class CookieOrder(BaseModel):

    cookie: Cookie
    quantity: int
    modifier_collection_list: List[CookieModifierCollection]
    custom_price: float
    note: str


class Customer(BaseModel):

    id: int
    first_name: str
    last_name: str
    country_id: int
    district_id: int
    city_id: int
    phone_number: str
    address1: str
    address2: str


class OrderCollection(BaseModel):

    cookie_order_list: List[CookieOrder]
    tax: float
    discount: float
    discount_percentage: float
    customer: Union[Customer, NoneType]
