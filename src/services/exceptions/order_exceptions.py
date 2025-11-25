class CustomerNotFound(Exception):
    def __init__(self, message='Customer not Found'):
        super().__init__(message)