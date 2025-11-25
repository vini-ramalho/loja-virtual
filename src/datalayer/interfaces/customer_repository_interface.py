from uuid import UUID
from src.domains.customer import CustomerRegistration, Customer
from src.datalayer.base import RepositoryInterface


class CustomerRepositoryInterface(RepositoryInterface):

    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        raise NotImplementedError

    async def email_already_exists(self, email: str)-> bool:
        raise NotImplementedError
    
    async def get_customer_by_id(self, id: UUID) -> Customer:
        raise NotImplementedError