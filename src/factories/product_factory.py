from src.datalayer.base import RepositoryInterface
from src.datalayer.repositories.mock.product_repository_mock import ProductRepositoryMock
from src.services.base import ServiceBase
from src.services.product_service import ProductService

class ProductFactory:

    @staticmethod
    def create_mock():
        repository: RepositoryInterface = ProductRepositoryMock()
        service: ServiceBase = ProductService(repository=repository)
        return service