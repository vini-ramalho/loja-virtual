from src.datalayer.base import RepositoryInterface
from src.datalayer.repositories.mock.customer_repository_mock import CustomerRepositoryMock
from src.datalayer.repositories.mock.order_repository_mock import OrderRepositoryMock
from src.services.base import ServiceBase
from src.services.order_service import OrderService

class OrderFactory:

    @staticmethod
    def create_mock():
        repository: RepositoryInterface = OrderRepositoryMock()
        customer_repository: RepositoryInterface = CustomerRepositoryMock()
        service: ServiceBase = OrderService(repository=repository, customer_repository=customer_repository)
        return service