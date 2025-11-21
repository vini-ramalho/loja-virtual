from src.datalayer.interfaces.product_repository_interface import ProductRepositoryInterface
from src.domains.product import Product, ProductRegistration

from src.datalayer.repositories.mock.memdb import PRODUCT_DB

class ProductRepositoryMock(ProductRepositoryInterface):
    '''Método que realiza o registro do product, recebe sua própria instancia e um product_registration, deve retornar um product'''
    async def register(self, product_registration: ProductRegistration) -> Product:
        #product com type hint de Product, onde vai receber um Product que foi desempacotado (**) do model_dump (método do Pydantic que transforma um modelo em um dicionário Python) de product
        product: Product = Product(**product_registration.model_dump())
        PRODUCT_DB.append(product)        
        return product
    
    '''Método que verifica se o produto já existe através de seu name, recebe sua própria instancia e o name, deve retornar um boolean'''
    async def product_already_exists(self, name: str)-> bool:
        #product_already_exists cria uma lista e faz um filtro, recebendo uma função anonima (lambda que faz papel de função verdade, true ou false) e comparando de o name existe dentro de PRODUCT_DB. Se encontrar adiciona a lista e retorna True, impedindo o cadastro.
        product_already_exists = list(filter(lambda c: c.name==name, PRODUCT_DB))
        return True if len(product_already_exists) > 0 else False