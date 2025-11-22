from dataclasses import dataclass
from src.datalayer.interfaces.product_repository_interface import ProductRepositoryInterface
from src.services.base import ServiceBase
from src.domains.product import ProductRegistration, Product
from src.services.exceptions.product_exceptions import ProductAlreadyExists, ProductUnitDontExists

@dataclass
class ProductService(ServiceBase):
    '''repositório obrigatório (ServiceBase)'''
    repository: ProductRepositoryInterface
    '''Método de registro, recebe a própria instancia e um product_registration, deve retornar um Product'''
    async def register(self, product_registration: ProductRegistration) -> Product:
        #Verifica se o produto existe
        if await self.product_already_exists(product_registration.name):
            #retorna a msg de erro de ProductAlreadyExists
            raise ProductAlreadyExists()
        
        if await self.unit_not_registred(product_registration.unit):
            raise ProductUnitDontExists()
        
        return await self.repository.register(product_registration)
    
    '''Método para verificar se o produto existe, recebe a própria instancia e a string de name, deve retornar um boolean'''
    async def product_already_exists(self, name: str)-> bool:
        #Retorna se o name existe através da consulta do repositório
        return await self.repository.product_already_exists(name)
    
    async def unit_not_registred(self, unit) -> bool:
        return await self.repository.unit_not_registred(unit)