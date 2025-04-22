from app.models.product_model import Product
from app.exceptions.product_exceptions import ProductNotFoundError, DatabaseError

class ProductRepository:
    products = {}

    @staticmethod
    def get_products(name=None, category=None, barcode=None, price=None):
        filtered_products = []
        
        try:
            for product in ProductRepository.products.values():
                if name and name.lower() not in product.name.lower():
                    continue
                if category and category.lower() not in product.category.lower():
                    continue
                if barcode and barcode.lower() not in product.barcode.lower():
                    continue
                if price and price != product.price:
                    continue
                filtered_products.append(product)

            return filtered_products
        except DatabaseError:
            # Placeholder for future DB-related error handling
            raise
    
    @staticmethod
    def get_product_by_id(id: int):
        try:
            product = ProductRepository.products.get(id)

            if product is None:
                raise ProductNotFoundError(id)
            
            return product
        
        except DatabaseError:
            # Placeholder for future DB-related error handling
            raise
    
    @staticmethod
    def insert_product(name: str, category: str, barcode: str, price: float):
        try:
            if ProductRepository.products:
                max_id = max(ProductRepository.products)
            else:
                max_id = 0
            
            id = max_id + 1
            product = Product(id, name, category, barcode, price)
            ProductRepository.products[id] = product

            return product
        
        except DatabaseError:
            # Placeholder for future DB-related error handling
            raise

    @staticmethod
    def delete_product(id: int):
        try:
            del ProductRepository.products[id]
        
        except KeyError:
            raise ProductNotFoundError(id)
        
        except DatabaseError:
            # Placeholder for future DB-related error handling
            raise
    

    @staticmethod
    def update_product(id: int, name: str, category: str, barcode: str, price: float):
        try:

            if id not in ProductRepository.products:
                raise ProductNotFoundError(id)
            
            updated_product = Product(id, name, category, barcode, price)
            ProductRepository.products[id] = updated_product

            return updated_product
        
        except DatabaseError:
            # Placeholder for future DB-related error handling
            raise


    @staticmethod
    def patch_product(id: int, data: dict):
        try:

            if id not in ProductRepository.products:
                raise ProductNotFoundError(id)
            
            product = ProductRepository.products[id]

            for key, value in data.items():
                setattr(product, key, value)

            return product
        
        except DatabaseError:
            # Placeholder for future DB-related error handling
            raise