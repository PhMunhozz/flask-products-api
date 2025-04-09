from app.models.product_model import Product

class ProductRepository:
    products = {}

    @staticmethod
    def get_products(name=None, category=None, barcode=None, price=None):
        filtered_products = []

        for product in ProductRepository.products.values():
            if name and name.lower() not in product.name.lower():
                continue
            if price and float(price) != product.price:
                continue
            filtered_products.append(product)

        return filtered_products
    
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