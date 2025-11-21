from src.domains.order import Order, OrderStatus, OrderStatusName, OrderItem
from src.domains.product import Product
from src.domains.customer import Customer


def test_should_create_order():

    customer: Customer = Customer(name='Vinicius', email='vini@vini.com')

    status: OrderStatus = OrderStatus() 
 
    assert status.name == OrderStatusName.ACCOMPLISHED

    product1: Product = Product(name='Notebook', description='Notebook accer nitro', price=4000)

    assert product1.name =='Notebook'
    assert product1.description == 'Notebook accer nitro'
    assert product1.price == 4000

    product2: Product = Product(name='Monitor', description='Monitor Gamer AOC', price=1000)

    assert product2.name =='Monitor'
    assert product2.description == 'Monitor Gamer AOC'
    assert product2.price == 1000


    item1: OrderItem = OrderItem(product_id=product1.id, price=product1.price, quantity=1)
    item2: OrderItem = OrderItem(product_id=product2.id, price=product2.price, quantity=2)

    assert item1.product_id == product1.id
    assert item1.price == product1.price
    assert item1.quantity == 1

    assert item2.product_id == product2.id
    assert item2.price == product2.price
    assert item2.quantity == 2

    order: Order = Order(customer=customer)
    order.add_status(status)
    order.add_item(item1)
    order.add_item(item2)

    assert len(order.status) == 1
    assert order.status[0].name == OrderStatusName.ACCOMPLISHED
    assert len(order.itens) ==2


    #Novo status: em preparação

    status2 = OrderStatus(name=OrderStatusName.IN_PREPARATION)
    order.add_status(status2)

    assert len(order.status) ==2
    assert order.status[1].name == OrderStatusName.IN_PREPARATION

    #Novo status: enviado

    status3 = OrderStatus(name=OrderStatusName.SENT)
    order.add_status(status3)

    assert len(order.status) == 3
    assert order.status[2].name == OrderStatusName.SENT


    #Novo status: entregue

    status4 = OrderStatus(name=OrderStatusName.DELIVERED)
    order.add_status(status4)

    assert len(order.status) == 4
    assert order.status[3].name == OrderStatusName.DELIVERED

    #Novo status: finalizado

    status5 = OrderStatus(name=OrderStatusName.FINISHED)
    order.add_status(status5)

    assert len(order.status) == 5
    assert order.status[4].name == OrderStatusName.FINISHED


    #Calculando total

    assert order.total() == 6000.0