from src.factories.product_factory import ProductFactory
from src.services.product_service import ProductRegistration
import pytest
from src.services.exceptions.product_exceptions import ProductAlreadyExists, ProductUnitDontExists



@pytest.mark.asyncio
async def test_should_create_product():
    service = ProductFactory.create_mock()

    product = ProductRegistration(
        name = 'MoonBoard',
        description='MoonBoard DIY Kit - 2025',
        price= 27954.76,
        unit='un'
    )

    assert product.name == 'MoonBoard'
    assert product.description == 'MoonBoard DIY Kit - 2025'
    assert product.price == 27954.76
    assert product.unit == 'un'

    response = await service.register(product_registration=product)
    print(response)

@pytest.mark.asyncio
async def test_should_raise_error_when_create_product_duplicated():
    service = ProductFactory.create_mock()

    product_duplicated = ProductRegistration(
        name = 'MoonBoard',
        description='MoonBoard DIY Kit - 2025',
        price= 27954.76,
        unit='un'
    )

    with pytest.raises(ProductAlreadyExists) as error:

        await service.register(product_registration=product_duplicated)
         
    assert str(error.value) == 'Produto already exists'

@pytest.mark.asyncio
async def test_should_raise_error_when_create_product_with_unit_not_registered():
    service = ProductFactory.create_mock()

    product_with_no_unit = ProductRegistration(
        name= 'Pinch Block',
        description='Grip Strength Testing and Training Tool',
        price= 135.0,
        unit='pç'
    )

    with pytest.raises(ProductUnitDontExists) as error:
        await service.register(product_registration=product_with_no_unit)
        
    assert str(error.value) == 'UnitOfMeasure invalid'