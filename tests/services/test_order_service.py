from unittest.mock import AsyncMock
from src.factories.order_factory import OrderFactory
from src.domains.order import OrderRegistration, OrderStatus, OrderStatusName, OrderItem
from src.domains.customer import Customer
from uuid import uuid4
import pytest

from src.services.exceptions.order_exceptions import CustomerNotFound

@pytest.mark.asyncio
async def test_should_create_order():

    service = OrderFactory.create_mock()
    
    #mock do customer repositpry
    customer_repo = AsyncMock() 
    mock_id = uuid4()

    #criando um customer com dados mockados
    customer_repo.get_customer_by_id = AsyncMock (return_value= Customer(
        id= mock_id,
        name='Fake Customer',
        email='fake@mail.com'
        )
    )

    item_1 = OrderItem(product_id= uuid4(), price=5.00, quantity=1)
    item_2 = OrderItem(product_id=uuid4(), price=10.0, quantity=2)
                  

    service.customer_repository = customer_repo

    order = OrderRegistration(
        customer_id=mock_id,
        status=[OrderStatus()],
        items=[item_1, item_2]
    )

    await service.create_order(order)

    assert order.customer_id == mock_id
    assert order.items[0].product_id == item_1.product_id
    assert order.items[1].product_id == item_2.product_id

@pytest.mark.asyncio
async def test_should_raise_erro_when_customer_id_not_found():
    service = OrderFactory.create_mock()

    fake_id = uuid4()

    item_1 = OrderItem(product_id= uuid4(), price=5.00, quantity=1)
    item_2 = OrderItem(product_id=uuid4(), price=10.0, quantity=2)

    order = OrderRegistration(
        customer_id=fake_id,
        status=[OrderStatus()],
        items=[item_1, item_2]
    )
    with pytest.raises(CustomerNotFound) as error:

        await service.create_order(order)

    assert str(error.value) == 'Customer not Found'


@pytest.mark.asyncio
async def test_should_create_order_and_set_status_IN_PREPARATION():
    service = OrderFactory.create_mock()

    customer_repo = AsyncMock() 
    mock_id = uuid4()

    customer_repo.get_customer_by_id = AsyncMock (return_value= Customer(
        id= mock_id,
        name='Fake Customer',
        email='fake@mail.com'
        )
    )

    item_1 = OrderItem(product_id= uuid4(), price=5.00, quantity=1)
                  

    service.customer_repository = customer_repo

    order = OrderRegistration(
        customer_id=mock_id,
        status=[OrderStatus()],
        items=[item_1]
    )

    response = await service.create_order(order)

    #Novo status: em preparação
    response.add_status(OrderStatus(name=OrderStatusName.IN_PREPARATION))

    assert len(response.status) ==2
    assert response.status[1].name == OrderStatusName.IN_PREPARATION

@pytest.mark.asyncio
async def test_should_create_order_and_calculate_total():

    service = OrderFactory.create_mock()

    customer_repo = AsyncMock() 
    mock_id = uuid4()

    customer_repo.get_customer_by_id = AsyncMock (return_value= Customer(
        id= mock_id,
        name='Fake Customer',
        email='fake@mail.com'
        )
    )

    item_1 = OrderItem(product_id= uuid4(), price=5.00, quantity=1)
    item_2 = OrderItem(product_id=uuid4(), price=5.00, quantity=1)
    item_3 = OrderItem(product_id=uuid4(), price=5.00, quantity=1)
                  

    service.customer_repository = customer_repo

    order = OrderRegistration(
        customer_id=mock_id,
        status=[OrderStatus()],
        items=[item_1, item_2, item_3]
    )

    response = await service.create_order(order)

    #Calcula o total da Order
    assert response.total() == 15.00

@pytest.mark.asyncio
async def test_should_create_order_and_add_item():

    
    service = OrderFactory.create_mock()

    customer_repo = AsyncMock() 
    mock_id = uuid4()

    customer_repo.get_customer_by_id = AsyncMock (return_value= Customer(
        id= mock_id,
        name='Fake Customer',
        email='fake@mail.com'
        )
    )

    item_1 = OrderItem(product_id= uuid4(), price=1.00, quantity=1)
    item_2 = OrderItem(product_id=uuid4(), price=2.00, quantity=1)
                  

    service.customer_repository = customer_repo

    order = OrderRegistration(
        customer_id=mock_id,
        status=[OrderStatus()],
        items=[item_1, item_2]
    )

    response = await service.create_order(order)

    assert len(response.items) == 2

    item_3 = OrderItem(product_id=uuid4(), price=3.00, quantity=1)

    #Adiciona novo item na Order
    response.add_item(item_3)

    assert len(response.items) == 3
