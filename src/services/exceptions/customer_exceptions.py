class EmailAlreadyExist(Exception):
    def __init__(self, message='E-mail already exists'):
        super().__init__(message)

class CustomerNotFound(Exception):
    def __init__(self, message='Customer not Found'):
        super().__init__(message)