from enum import Enum
from pydantic import BaseModel, Field
from src.domains.base import DomainBase


class UnitOfMeasureName(str, Enum):
    UNIT = "un"            
    PACKAGE = "pacote"      
    BOX = "caixa"              
    KILOGRAM = "kg"          
    GRAM = "g"               
    LITER = "l"              
    MILLILITER = "ml"        

class Product(DomainBase):
    name: str
    description: str
    price: float
    unit: UnitOfMeasureName = Field(default= UnitOfMeasureName.UNIT.value)

class ProductRegistration(DomainBase):
    name:str
    description: str
    price: float 
    unit: str
