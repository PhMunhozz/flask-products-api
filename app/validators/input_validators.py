from app.exceptions.product_exceptions import ValidationError

def validate_required_fields(data: dict, required_fields: list, *, partial: bool = False) -> None:
    allowed = set(required_fields)
    for field_name in allowed:
        # all fields validation
        if not partial and not data.get(field_name):
            raise ValidationError(f"{field_name.upper()} is required and cannot be empty.")
        
        # partial fields validation (validates given fields, but does not require all fields)
        if field_name in data and data[field_name] in (None, "", [], {}):
            raise ValidationError(f"{field_name.upper()} cannot be empty or null.")

def validate_possible_fields(data: dict, possible_fields: list) -> None:
    allowed = set(possible_fields)
    for key in data:
        if key not in allowed:
            raise ValidationError(f"{key.upper()} is not a valid possible field.")
        
def validate_positive_number(value: float, field_name: str, *, require_integer: bool = False) -> int:
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