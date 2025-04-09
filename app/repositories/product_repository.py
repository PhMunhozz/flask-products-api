from app.models.product_model import Product

class ProductRepository:
    products = {}

    @staticmethod
    def get_products(name=None, category=None, barcode=None, price=None):
        filtered_products = []

        for product in ProductRepository.products.values():
            if name and name.lower() not in product.name.lower():
                continue
            if category and category.lower() not in product.category.lower():
                continue
            if barcode and barcode.lower() not in product.barcode.lower():
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
    def insert_product(name: str, category: str, barcode: str, price: float):
        id = len(ProductRepository.products) + 1
        product = Product(id, name, category, barcode, price)
        ProductRepository.products[id] = product

        return product