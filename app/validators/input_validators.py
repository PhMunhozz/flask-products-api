from app.exceptions.product_exceptions import ValidationError

def validate_required_fields(data: dict, required_fields: list) -> None:
    for field_name in required_fields:
        if not data.get(field_name):
            raise ValidationError(f"{field_name.upper()} is required and cannot be empty.")
        
def validate_positive_number(value: float, field_name: str) -> None:
    try:
        number = float(value)
        if number <= 0:
            raise ValidationError(f"{field_name.upper()} must be a positive number.")
        
    except (ValueError, TypeError):
        raise ValidationError(f"{field_name.upper()} must be a valid number.")