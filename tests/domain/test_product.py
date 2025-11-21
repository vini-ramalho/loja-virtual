from src.domains.product import Product


def test_should_create_product():


    product: Product = Product(
        name='Notebook',
        description='Notebook accer nitro',
        price=4000,
    )

    

    assert product.name == 'Notebook'
    assert product.description =='Notebook accer nitro'
    assert product.price == 4000
    assert product.unit == 'un'
    print(product)