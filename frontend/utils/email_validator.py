import re

def validate_email_format(email: str) -> bool:
    """Validate email format using regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_email(email: str) -> tuple:
    """
    Validate email address format only.
    Returns: (is_valid, error_message)
    """
    if not validate_email_format(email):
        return False, "Invalid email format. Please enter a valid email address."
    return True, ""
