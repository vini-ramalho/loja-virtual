import uuid
from src.datalayer.interfaces.order_repository_interface import OrderRepositoryInterface
from src.domains.order import Order, OrderRegistration

from src.datalayer.repositories.mock.memdb import ORDER_DB

class OrderRepositoryMock(OrderRepositoryInterface):
    async def create_order(self, order: Order)-> Order:
        ORDER_DB.append(order)
        return order
    
    async def customer_not_found(self, id: uuid)-> bool:
        customer_not_found = list(filter(lambda c: c.id == id, ORDER_DB))
        return True if len(customer_not_found) > 0 else False