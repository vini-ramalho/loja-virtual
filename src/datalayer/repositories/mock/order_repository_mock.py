import uuid
from src.datalayer.interfaces.order_repository_interface import OrderRepositoryInterface
from src.domains.order import Order, OrderRegistration

from src.datalayer.repositories.mock.memdb import ORDER_DB, CUSTOMER_DB

class OrderRepositoryMock(OrderRepositoryInterface):
    async def create_order(self, order: Order)-> Order:
        ORDER_DB.append(order)
        return order
