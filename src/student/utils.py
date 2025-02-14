from django.utils.crypto import get_random_string

def generate_random_password():
    """
    Function to generate a random password.
    """
    return get_random_string(8)