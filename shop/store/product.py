from dataclasses import dataclass
from enum import Enum


class ProductCategory(Enum):
    FOOD = "Food"
    OTHER = 'Other'
    TOOL = "Tool"


@dataclass
class Product:
    name: str
    category: ProductCategory
    unit_price: float
    identifier: int

    def __str__(self):
        return f"Name: {self.name} | Category: {self.category.value} | Price: {self.unit_price}"


@dataclass
class ExpiringProduct(Product):
    production_year: int
    validity_years: int

    def does_expire(self, current_year):
        return current_year > self.production_year + self.validity_years
