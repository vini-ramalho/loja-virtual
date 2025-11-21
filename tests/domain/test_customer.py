from src.domains.customer import Customer


def test_should_create_customer():
    customer: Customer = Customer(name='Vinicius', email='vini@vini.com')

    assert customer.name == 'Vinicius'
    assert customer.email == 'vini@vini.com'