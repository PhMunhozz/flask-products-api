class Product:
    def __init__(self, id: int, name: str, category: str, barcode: str, price: float) -> None:
        self.id = id
        self.name = name
        self.category = category
        self.barcode = barcode
        self.price = price
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "barcode": self.barcode,
            "price": self.price
        }