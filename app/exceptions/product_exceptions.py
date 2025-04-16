class ProductNotFoundError(Exception):
    def __init__(self, id: int, message: str=None):
        self.id = id

        message = message or f"Product ID {id} not found."
        super().__init__(message)

class ValidationError(Exception):
    def __init__(self, message: str=None):
        super().__init__(message or "Invalid data.")

class DatabaseError(Exception):
    def __init__(self, message: str=None):
        super().__init__(message or "Error connecting to database.")