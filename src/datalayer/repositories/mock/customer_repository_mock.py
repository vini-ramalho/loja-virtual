from uuid import UUID
from src.datalayer.interfaces.customer_repository_interface import CustomerRepositoryInterface
from src.domains.customer import Customer, CustomerRegistration

from src.datalayer.repositories.mock.memdb import CUSTOMER_DB
from src.services.exceptions.order_exceptions import CustomerNotFound

class CustomerRepositoryMock(CustomerRepositoryInterface):
    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        customer: Customer = Customer(**customer_registration.model_dump())
        CUSTOMER_DB.append(customer)
        return customer


    async def email_already_exists(self, email: str)-> bool:
        email_exists = list(filter(lambda c: c.email == email, CUSTOMER_DB))
        return True if len(email_exists) > 0 else False
    
    async def get_customer_by_id(self, id: UUID)-> Customer:
        for customer in CUSTOMER_DB:
            if customer.id == id:
                return customer
        raise CustomerNotFound()
            