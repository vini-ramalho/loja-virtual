from src.factories.customer_factory import CustomerFactory
from src.domains.customer import CustomerRegistration
import pytest
from src.services.exceptions.customer_exceptions import EmailAlreadyExist

@pytest.mark.asyncio
async def test_should_create_customer():

    service = CustomerFactory.create_mock()

    customer1 = CustomerRegistration(
        name= 'Vinicius',
        email= 'vini@vini.com',
        password='123456',
        confirm_password='123456',
    )

    response = await service.register(customer_registration=customer1)

    print (response)

@pytest.mark.asyncio
async def test_should_raise_error_when_create_customer_duplicated():

    service = CustomerFactory.create_mock()

    customer_duplicated = CustomerRegistration(
        name= 'Vinicius2',
        email= 'vini@vini.com',
        password='123456',
        confirm_password='123456',
    )
    with pytest.raises(EmailAlreadyExist) as error:

        await service.register(customer_registration=customer_duplicated)

    assert str(error.value) == 'E-mail already exists'

@pytest.mark.asyncio
async def test_should_return_customer_by_id():
    service = CustomerFactory.create_mock()

    customer_id = CustomerRegistration(
        name= 'Teste ID',
        email= 'ID@customer.com',
        password='123456',
        confirm_password='123456',
    )

    response_id = await service.register(customer_registration=customer_id)

    found = await service.get_customer_by_id(response_id.id)

    print(found)