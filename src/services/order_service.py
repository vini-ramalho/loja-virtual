from dataclasses import dataclass
from uuid import UUID
from src.datalayer.interfaces.customer_repository_interface import CustomerRepositoryInterface
from src.datalayer.interfaces.order_repository_interface import OrderRepositoryInterface
from src.services.base import ServiceBase
from src.domains.order import Order, OrderItem, OrderRegistration, OrderStatus, OrderStatusName
from src.services.exceptions.order_exceptions import CustomerNotFound


@dataclass
class OrderService(ServiceBase):
    repository: OrderRepositoryInterface
    customer_repository: CustomerRepositoryInterface

    async def create_order(self, order_registration: OrderRegistration) -> Order:
        if await self.repository.customer_not_found(order_registration.customer_id):
            raise CustomerNotFound()
        
        customer = await self.customer_repository.get_customer_by_id(order_registration.customer_id)
        
        order_status: list[OrderStatus] = [OrderStatus()]

        order = Order (
            customer= customer,
            status= order_status,
            items= order_registration.items
        )        


        return await self.repository.create_order(order)
    
    async def customer_not_found(self, id: UUID) -> bool:
        return await self.repository.customer_not_found(id)


