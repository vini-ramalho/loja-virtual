from dataclasses import dataclass
from uuid import UUID
from src.datalayer.interfaces.customer_repository_interface import CustomerRepositoryInterface

from src.domains.customer import Customer, CustomerRegistration
from src.services.base import ServiceBase
from src.services.exceptions.customer_exceptions import EmailAlreadyExist

@dataclass
class CustomerService(ServiceBase):
    repository: CustomerRepositoryInterface

    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        if await self.email_already_exists(customer_registration.email):
            raise EmailAlreadyExist()
        return await self.repository.register(customer_registration)

    async def email_already_exists(self, email: str)-> bool:
        return await self.repository.email_already_exists(email) 
    
    async def get_customer_by_id(self, id: UUID) -> Customer:
        return await self.repository.get_customer_by_id(id)