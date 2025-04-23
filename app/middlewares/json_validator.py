from functools import wraps
from flask import request
from werkzeug.exceptions import BadRequest
from app.exceptions.product_exceptions import ValidationError

def validate_json_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            raise ValidationError("Content-Type must be application/json.")
        
        try:
            request_data = request.get_json()
        except BadRequest:
            raise ValidationError("Invalid or malformed JSON in request body.")

        if not request_data:
            raise ValidationError("Invalid or missing JSON in request body.")
        
        kwargs['data'] = request_data

        return func(*args, **kwargs)
    return wrapper