from app.exceptions.product_exceptions import ValidationError

def validate_required_fields(data: dict, required_fields: list) -> None:
    for field_name in required_fields:
        if not data.get(field_name):
            raise ValidationError(f"{field_name.upper()} is required and cannot be empty.")
        
def validate_positive_number(value: float, field_name: str, require_integer: bool = False) -> int:
    try:
        number = float(value)

        if require_integer:
            if not number.is_integer():
                raise ValidationError(f"{field_name.upper()} must be an integer.")
            number = int(number)

        if number <= 0:
            raise ValidationError(f"{field_name.upper()} must be a positive {'integer' if require_integer else 'number'}.")
        
        return int(number) if require_integer else number
        
    except (ValueError, TypeError):
        raise ValidationError(f"{field_name.upper()} must be a valid {'integer' if require_integer else 'number'}.")