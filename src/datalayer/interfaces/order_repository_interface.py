from src.domains.order import Order, OrderRegistration
from uuid import UUID
from src.datalayer.base import RepositoryInterface


class OrderRepositoryInterface (RepositoryInterface):

    async def create_order(self, order_registration: OrderRegistration) -> Order:
        raise NotImplementedError
    