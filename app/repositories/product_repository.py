from app.models.product_model import Product

class ProductRepository:
    products = {}

    @staticmethod
    def get_products():
        return list(ProductRepository.products.values())
    
    @staticmethod
    def get_product_by_id(id: int):
        product = ProductRepository.products.get(id)
        return product
    
    @staticmethod
    def insert_product(name: str, price: float):
        id = len(ProductRepository.products) + 1
        product = Product(id, name, price)
        ProductRepository.products[id] = product

        return product