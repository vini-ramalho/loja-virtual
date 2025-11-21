from domains.product import Product, ProductRegistration
from src.datalayer.base import RepositoryInterface


class ProductRepositoryInterface (RepositoryInterface):
    '''Registra um produto, recebendo a própria instancia e product_registrarion que é um método do domain Product'''
    async def register(self, product_registration: ProductRegistration)-> Product:
        raise NotImplementedError

    '''Verificar se o produto já existe, recebendo a pópria instancia e o name, que é uma string e deve retornar um booleano'''
    async def product_already_exists(self, name: str) -> bool:
        raise NotImplementedError