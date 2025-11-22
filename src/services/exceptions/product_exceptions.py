class ProductAlreadyExists(Exception):
    def __init__(self, message='Produto already exists'):
        super().__init__(message)

class ProductUnitDontExists(Exception):
    def __init__(self, message = 'UnitOfMeasure invalid'):
        super().__init__(message)