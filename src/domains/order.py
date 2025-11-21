from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from src.domains.base import DomainBase
from enum import Enum
from src.domains.customer import Customer

class OrderStatusName(str, Enum):
    ACCOMPLISHED = 'realizado'
    IN_PREPARATION = 'em preparação'
    SENT = 'enviado'
    DELIVERED = 'entregue'
    FINISHED = 'finalizado'

class OrderStatus(DomainBase):
    name:OrderStatusName =Field(default = OrderStatusName.ACCOMPLISHED)

class OrderItem(DomainBase):
    product_id: UUID
    price: float
    quantity: int


class Order(DomainBase):
    customer: Customer 
    status: list[OrderStatus] = Field(default_factory=list)
    items: list[OrderItem] = Field(default_factory=list)

    def add_status(self, status: OrderStatus):
        self.status.append(status)

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def total(self):
        return sum([item.price * item.quantity for item in self.items])