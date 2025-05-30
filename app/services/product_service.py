from app.repositories.product_repository import ProductRepository
from app.exceptions.product_exceptions import ProductNotFoundError, ValidationError


class ProductService:

    @staticmethod
    def get_products(name=None, category=None, barcode=None, price=None):
        
        products = ProductRepository.get_products(name, category, barcode, price)
        return [product.to_dict() for product in products]
    

    @staticmethod
    def get_product_by_id(id: int):
        
        product = ProductRepository.get_product_by_id(id)
        return product.to_dict()
        
 
    @staticmethod
    def insert_product(name: str, category: str, barcode: str, price: float):

        product = ProductRepository.insert_product(name, category, barcode, price)
        return product.to_dict()
    

    @staticmethod
    def delete_product(id: int):
        ProductRepository.delete_product(id)


    @staticmethod
    def update_product(id: int, name: str, category: str, barcode: str, price: float):
        product = ProductRepository.update_product(id, name, category, barcode, price)
        return product.to_dict()
    

    @staticmethod
    def patch_product(id: int, data: dict):        
        product = ProductRepository.patch_product(id, data)
        return product.to_dict()