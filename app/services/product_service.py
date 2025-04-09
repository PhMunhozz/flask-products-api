from app.repositories.product_repository import ProductRepository

class ProductService:

    @staticmethod
    def get_products():
        products = ProductRepository.get_products()
        return [product.to_dict() for product in products]
    
    @staticmethod
    def get_product_by_id(id: int):
        product = ProductRepository.get_product_by_id(id)
        return product.to_dict() if product else None
    
    @staticmethod
    def insert_product(name: str, price: float):

        if float(price) <= 0:
            raise ValueError("Price must be over 0.00.")

        product = ProductRepository.insert_product(name, price)
        return product.to_dict()