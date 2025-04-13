from app.repositories.product_repository import ProductRepository
from app.exceptions.product_exceptions import ProductNotFoundError, ValidationError


class ProductService:

    @staticmethod
    def get_products(name=None, category=None, barcode=None, price=None):

        try:
            if price is not None:
                price = float(price)
        except ValueError:
            raise ValidationError("PRICE must be a valid number.")
        
        products = ProductRepository.get_products(name, category, barcode, price)
        return [product.to_dict() for product in products]
    
    @staticmethod
    def get_product_by_id(id: int):

        try:
            id = int(id)
            if id <= 0:
                raise ValidationError()

            product = ProductRepository.get_product_by_id(id)
            return product.to_dict()
        
        except ValueError:
            raise ValidationError("ID must be a positive integer.")
        
    @staticmethod
    def insert_product(name: str, category: str, barcode: str, price: float):

        if float(price) <= 0:
            raise ValueError("Price must be over 0.00.")

        product = ProductRepository.insert_product(name, category, barcode, price)
        return product.to_dict()